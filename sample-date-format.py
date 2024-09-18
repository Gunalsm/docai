from datetime import datetime

def convert_date_format(date_str):
    """
    Convert date from 'dd/mm/yyyy' format to 'yyyy-mm-dd' format.

    :param date_str: Date in 'dd/mm/yyyy' format
    :return: Date in 'yyyy-mm-dd' format
    """
    try:
        # Parse the input date string
        date_obj = datetime.strptime(date_str, '%d/%m/%Y')
        # Convert to the desired format
        new_date_str = date_obj.strftime('%Y-%m-%d')
        return new_date_str
    except ValueError:
        # Handle the error if the input date is not in the expected format
        raise ValueError("The date format should be 'dd/mm/yyyy'")

# Example mapping: Adjust this according to your specific API requirements
api_mapped_data = {
    "CaseDetails": {
        "IPPractitionerForename": extracted_data.get("IPPractitionerForename"),
        "IPPractitionerSurname": extracted_data.get("IPPractitionerSurname"),
        "CourtName": extracted_data.get("court-name", {}).get("mentionText"),
        "IPCaseNumber": extracted_data.get("IPCaseNumber"),
        "IVANumber": extracted_data.get("IVANumber", ""),
        "ProposalType": extracted_data.get("proposal-type", {}).get("mentionText"),
        "IsProtocolCompliant": extracted_data.get("IsProtocolCompliant", ""),
        "ProtocolCompliantException": extracted_data.get("ProtocolCompliantException", ""),
        "ProposalStartDate": convert_date_format(extracted_data.get("proposal-date", {}).get("mentionText", "")),
        "CreditorMeetingDate": creditor_meeting_date,
        "TotalLiabilities": total_liabilities,
        "NomineeReport": extracted_data.get("NomineeReport", ""),
        "IVAProposalComment": extracted_data.get("IVAProposalComment", ""),
        "ConsumerHistory": extracted_data.get("ConsumerHistory", "")
    },
    "ConsumerDetails": {
        "Salutation": extracted_data.get("salutation", {}).get("mentionText"),
        "Forename": extracted_data.get("first-name", {}).get("mentionText"),
        "Surname": extracted_data.get("surname", {}).get("mentionText"),
        "DateOfBirth": extracted_data.get("dob", {}).get("mentionText"),
        "MaritalStatus": extracted_data.get("marital-status", {}).get("mentionText"),
        "NumberOfAdultsLivingInHouseHold": numberOfAdultsLivingInHouseHold,
        "ResidentialStatus": extracted_data.get("residential-status", {}).get("mentionText"),
        "EmploymentStatus": extracted_data.get("employment-status", {}).get("mentionText"),
        "Employer": extracted_data.get("employer-name", {}).get("mentionText"),
        "Occupation": extracted_data.get("occupation", {}).get("mentionText"),
        "NumberOfCars": numberOfCars,
        "Dependents": formatted_dependents,
        "OtherNames": [
            {
                "Forename": other.get("Forename", ""),
                "Surname": other.get("Surname", "")
            } for other in other_names
        ],
        "Addresses": formatted_addresses
    }
}
