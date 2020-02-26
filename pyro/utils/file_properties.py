import struct
import binascii
from pyrogram.client.ext import utils, FileData
from pyrogram.errors import FileIdInvalid


class CustomFileProperties:
    @staticmethod
    async def get_properties(client, m_message_id, m_chat_id):
        message = await client.get_messages(chat_id=m_chat_id, message_ids=m_message_id)
        available_media = ("audio", "document", "photo", "sticker", "animation", "video", "voice", "video_note")

        for kind in available_media:
            media = getattr(message, kind, None)
            if media is not None:
                break
        else:
            raise ValueError("Invalid Media Type.")

        file_id = media.file_id
        file_name = getattr(media, "file_name", "")
        file_size = getattr(media, "file_size", None)
        mime_type = getattr(media, "mime_type", None)
        date = getattr(media, "date", None)
        file_ref = getattr(media, "file_ref", None)

        data = FileData(
            file_name=file_name,
            file_size=file_size,
            mime_type=mime_type,
            date=date,
            file_ref=file_ref
        )

        def get_existing_attributes() -> dict:
            return dict(filter(lambda x: x[1] is not None, data.__dict__.items()))

        try:
            decoded = utils.decode_file_id(file_id)
            media_type = decoded[0]

            if media_type == 1:
                unpacked = struct.unpack("<iiqqqiiiqi", decoded)
                dc_id, photo_id, _, volume_id, size_type, peer_id, _, peer_access_hash, local_id = unpacked[1:]

                data = FileData(
                    **get_existing_attributes(),
                    media_type=media_type,
                    dc_id=dc_id,
                    peer_id=peer_id,
                    peer_access_hash=peer_access_hash,
                    volume_id=volume_id,
                    local_id=local_id,
                    is_big=size_type == 3
                )
            elif media_type in (0, 2, 14):
                unpacked = struct.unpack("<iiqqqiiii", decoded)
                dc_id, document_id, access_hash, volume_id, _, _, thumb_size, local_id = unpacked[1:]

                data = FileData(
                    **get_existing_attributes(),
                    media_type=media_type,
                    dc_id=dc_id,
                    document_id=document_id,
                    access_hash=access_hash,
                    thumb_size=chr(thumb_size)
                )
            elif media_type in (3, 4, 5, 8, 9, 10, 13):
                unpacked = struct.unpack("<iiqq", decoded)
                dc_id, document_id, access_hash = unpacked[1:]

                data = FileData(
                    **get_existing_attributes(),
                    media_type=media_type,
                    dc_id=dc_id,
                    document_id=document_id,
                    access_hash=access_hash
                )
            else:
                raise ValueError("Unknown media type: {}".format(file_id))
            return data
        except (AssertionError, binascii.Error, struct.error):
            raise FileIdInvalid from None
