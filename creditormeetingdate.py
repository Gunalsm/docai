from datetime import datetime

def convert_meeting_date_time(date_str, time_str):
    """
    Convert date from 'dd/mm/yyyy' and time from 'hh:mm' format to 'yyyy-mm-ddThh:mm:ss' format.

    :param date_str: Date in 'dd/mm/yyyy' format
    :param time_str: Time in 'hh:mm' format
    :return: Combined datetime in 'yyyy-mm-ddThh:mm:ss' format
    """
    try:
        # Remove any trailing dots from the time string
        time_str = time_str.rstrip('.')

        # Convert date from 'dd/mm/yyyy' to 'yyyy-mm-dd'
        date_obj = datetime.strptime(date_str, '%d/%m/%Y')
        formatted_date = date_obj.strftime('%Y-%m-%d')

        # Combine the date and time
        combined_datetime_str = f"{formatted_date}T{time_str}:00"
        return combined_datetime_str
    except ValueError as e:
        raise ValueError(f"Error in converting date/time: {e}")

# Assuming you are extracting these values from the JSON
meeting_date = extracted_data.get("meeting-of-creditors-date", {}).get("mentionText", "")
meeting_time = extracted_data.get("meeting-of-creditors-time", {}).get("mentionText", "")

# Combine the date and time
creditor_meeting_date = convert_meeting_date_time(meeting_date, meeting_time)

# Example mapping, including the combined CreditorMeetingDate
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
        "CreditorMeetingDate": creditor_meeting_date,  # Combined date and time
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
