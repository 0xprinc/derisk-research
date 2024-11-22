"""
This module contains the logic to parse the nostra data to human-readable format.
"""
from typing import Any
from data_handler.handler_tools.data_parser.serializers import (
    DebtMintEventData,
    DebtBurnEventData,
    InterestRateModelEventData,
    DebtTransferEventData,
    BearingCollateralMintEventData,
    BearingCollateralBurnEventData
)


class NostraDataParser:
    """
    Parses the nostra data to human-readable format.
    """
    def parse_interest_rate_model_event(
        cls, event_data: List[Any]
    ) -> InterestRateModelEventData:
        """
        Parses the interest rate model event data into a human-readable format.

        The event data is fetched from on-chain logs and is structured in the following way:
        - event_data[0]: The debt token address (as a hexadecimal string).
        - event_data[5]: The lending interest rate index (as a hexadecimal in 18 decimal places). 
        - event_data[7]: The borrow interest rate index (as a hexadecimal in 18 decimal places).

        Args:
            event_data (List[Any]): A list containing the raw event data.
                Expected order: [debt_token, lending_rate, _, borrow_rate, _, 
                                 lending_index, _, borrow_index, _]

        Returns:
            InterestRateModelEventData: A model with the parsed event data.
        """
        return InterestRateModelEventData(
            debt_token=event_data[0],
            lending_index=event_data[5],
            borrow_index=event_data[7]
        )

    def parse_non_interest_bearing_collateral_mint_event(self):
        pass

    def parse_non_interest_bearing_collateral_burn_event(self):
        pass

    def parse_interest_bearing_collateral_mint_event(self, event_data: list[Any]) -> BearingCollateralMintEventData:
        """
        Parses the BearingCollateralMint event data into a human-readable format using the BearingCollateralMintEventData serializer.
        
        The event data is fetched from on-chain logs and is structured in the following way:
        - event_data[0]: The user address (as a hexadecimal string).
        - event_data[1]: TODO(baitcode): somehow fill that

        Args:
            event_data (list[Any]): A list containing the raw event data, typically with 3 or more elements:
                user address, amount TODO(baitcode): somehow fill that
        Returns:
            BearingCollateralMintEventData: A Pydantic model with the parsed and validated event data in a human-readable format.

        """
        return BearingCollateralMintEventData(
            user=event_data[0],
            amount=event_data[1],
        )

    def parse_interest_bearing_collateral_burn_event(self, event_data: list[Any]) -> BearingCollateralBurnEventData:
        """
        Parses the BearingCollateralMint event data into a human-readable format using the BearingCollateralMintEventData serializer.
        
        The event data is fetched from on-chain logs and is structured in the following way:
        - event_data[0]: The user address (as a hexadecimal string).
        - event_data[1]: TODO(baitcode): somehow fill that

        Args:
            event_data (list[Any]): A list containing the raw event data, typically with 3 or more elements:
                user address, amount TODO(baitcode): somehow fill that
        Returns:
            BearingCollateralMintEventData: A Pydantic model with the parsed and validated event data in a human-readable format.

        """
        return BearingCollateralBurnEventData(
            user=event_data[0],
            amount=event_data[1],
        )

    def parse_debt_transfer_event(
        cls, event_data: List[Any], from_address: str
    ) -> DebtTransferEventData:
        """
        Parses the debt transfer event data into a human-readable format using the
        DebtBurnEventData serializer.

        Args:
            event_data (List[Any]): A list containing the raw event data.
                Expected order: [sender, recipient, value, _]
            from_address (str): The address of the token contract

        Returns:
            DebtTransferEventData: A model with the parsed event data.
        """
        return DebtTransferEventData(
            sender=event_data[0],
            recipient=event_data[1],
            amount=event_data[2],
            token=from_address
        )

    def parse_debt_mint_event(self, event_data: list[Any]) -> DebtMintEventData:
        """
        Parses the debt mint event data into a human-readable format using the
        DebtMintEventData serializer.

        Args:
            event_data (List[Any]): A list containing the raw debt mint event data,
                                    typically with 2 elements: user and amount.

        Returns:
            DebtMintEventData: A Pydantic model with the parsed and validated event data in a human-readable format.
        """
        return DebtMintEventData(
            user=event_data[0],
            token=event_data[1]
        )

    def parse_debt_burn_event(self, event_data: list[Any]) -> DebtBurnEventData:
        """
        Parses the debt burn event data into a human-readable format using the
        DebtBurnEventData serializer.

        Args:
            event_data (List[Any]): A list containing the raw debt burn event data,
                                    typically with 2 elements: user and amount.

        Returns:
            DebtBurnEventData: A Pydantic model with the parsed and validated event data in a human-readable format.
        """
        return DebtBurnEventData(
            user=event_data[0],
            amount=event_data[1]
        )
