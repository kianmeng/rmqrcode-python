from abc import ABC, abstractmethod


class EncoderBase(ABC):
    """An abstract class for encoders"""

    @classmethod
    @abstractmethod
    def mode_indicator(cls):
        """Mode indicator defined in the Table 2.

        Returns:
            str: Mode indicator like "001".

        """
        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def encode(cls, data, character_count_indicator_length):
        """Encodes data and returns it.

        Args:
            data (str): Data to encode.
            character_count_indicator_length: (int): Number of bits of character
                count indicator defined in the Table 3.

        Returns:
            str: Encoded binary as string.

        Raises:
            IllegalCharacterError: If the data includes illegal character.

        """
        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def _encoded_bits(cls, data):
        """Encodes data and returns it.

        This method encodes the raw data without the meta data like the mode
        indicator, the number of data characters and so on.

        Args:
            data (str): Data to encode.

        Returns:
            str: Encoded binary as string.

        """
        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def length(cls, data):
        """Compute the length of the encoded bits.

        Args:
            data (str): Data to encode.

        Returns:
            int: The length of the encoded bits.

        """
        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def is_valid_characters(cls, data):
        """Checks wether the data does not include invalid character.

        Args:
            data (str): Data to validate.

        Returns:
            bool: Validation result.

        """
        raise NotImplementedError()


class IllegalCharacterError(ValueError):
    "A class represents an error raised when the given data includes illegal character."
    pass
