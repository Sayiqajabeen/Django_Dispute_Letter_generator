# from dotenv import load_dotenv
# import os
# import google.generativeai as genai
# import json
# from fpdf import FPDF  # For PDF generation
# import re

# genai.configure(api_key="AIzaSyCOD6opLtT3s23x0r7a7MzoXIzWtg2GgT0")

# def read_parsed_data(file_path):
#     """Read and parse JSON data from a file."""
#     try:
#         with open(file_path, 'r', encoding='utf-8') as file:
#             data = json.load(file)
#         return data
#     except FileNotFoundError:
#         print(f"Error: The file '{file_path}' was not found.")
#         return None
#     except json.JSONDecodeError:
#         print(f"Error: Failed to decode JSON from the file '{file_path}'.")
#         return None

# def clean_text(text):
#     """Remove unwanted symbols from headings."""
#     return re.sub(r'[\*#]', '', text)

# def generate_dispute_letter_google(parsed_data):
#     """Generate a dispute letter using Google's Generative AI model."""
#     parsed_data_str = json.dumps(parsed_data, indent=4)
    
#     prompt = clean_text(f"""
#  Based on the following extracted data, generate a professional dispute letter.
#  Apply these classification rules:  

#  - Do NOT include any '*' symbols around headings.  
#  - Use clear headings without special formatting characters like asterisks.  

#  Generate the following structure:

#  Bankruptcy Dispute Letter Template  

#    [Your Name]  
#    [Your Address]  
#    [City, State, ZIP Code]  
#    [Date]  

#    [Credit Bureau Name] Dispute Department  
#    [Address of Credit Bureau]  

#     Subject: Dispute of Inaccurate Bankruptcy Reporting  
#     Dear [Credit Bureau Name] Dispute Department,  
#     I am writing to formally dispute the inaccurate and/or unverifiable bankruptcy information listed on my credit report. Pursuant to the Fair Credit Reporting Act (FCRA) and Metro-2 Reporting Standards, I am requesting an immediate investigation to ensure that only accurate, complete, and verifiable information is reported.
#     Specific Errors
#     1. Case Information:  
#        - Error(s): Incorrect court name, case number mismatch, improper status as open, incorrect filing or discharge date.  
#        - Supporting Evidence: Court documents showing case resolution or absence of filing.  
#     2. Public Record Reporting:  
#        - Error(s): Record not verified with the appropriate court, incorrect inclusion in report after removal.  
#        - Supporting Evidence: Statement or response from the court or other public record sources.  

#     Requested Action

#      1. Verify with the appropriate court that the reported bankruptcy information is accurate, complete, and up-to-date.  
#      2. Remove the bankruptcy information if it cannot be verified as accurate and complete.  
#      3. Notify me in writing once the investigation is complete and confirm the actions taken regarding the disputed information.  

#      Legal Basis for Dispute
#      Under FCRA Section 611 (15 U.S.C. § 1681i), credit reporting agencies are required to investigate disputes and verify the accuracy of the reported information. Additionally:
#        - FCRA Section 609 (15 U.S.C. § 1681g) provides me with the right to request how this bankruptcy was verified.  
#        - Metro-2 Reporting Standards dictate accurate and timely reporting of bankruptcy status and details.  
#        - Inaccurate or unverifiable public record information violates FCRA Section 623 (15 U.S.C. § 1681s-2).  

#     Supporting Documents
#     I have enclosed the following documents to assist in your investigation:
#      1. Copy of my government-issued ID.  
#      2. Copy of my credit report with the disputed bankruptcy information highlighted.  
#      3. Court records and/or other supporting evidence showing inaccuracies in the reporting.  

#      Additional Notes
#      This information must be verified directly with the court and not with third-party vendors. If this information cannot be verified as accurate and complete, it must be removed under FCRA Section 611(a)(5)(A).  
#      I expect a resolution to this matter within the 30-day period as required by law.  
#      Thank you for your prompt attention to this matter.  

#      Sincerely,  
#     [Your Full Name]  

#      Enclosures
#      1. Copy of Government-issued ID  
#      2. Highlighted Credit Report  
#      3. Court Records/Supporting Documentation  

#     Extract and populate the details from 'parsed_data' where appropriate.
#     """)

#     try:
#         model = genai.GenerativeModel("gemini-pro")
#         response = model.generate_content(prompt)
#         return response.text.strip()
#     except Exception as e:
#         return f"Error generating letter: {str(e)}"

# def save_letter_as_pdf(letter_content, output_path):
#     """Save the generated letter content to a PDF file with reduced font size."""
#     try:
#         pdf = FPDF()
#         pdf.set_auto_page_break(auto=True, margin=10)
#         pdf.add_page()
#         pdf.set_font("Arial", size=6)

#         target_line = "I am writing to formally dispute the inaccurate and/or unverifiable bankruptcy information listed on my credit report. Pursuant to the Fair Credit Reporting Act (FCRA) and Metro-2 Reporting Standards, I am requesting an immediate investigation to ensure that only accurate, complete, and verifiable information is reported."
#         content_parts = clean_text(letter_content).split('\n')

#         for line in content_parts:
#             pdf.multi_cell(0, 3, line.strip())
#             if target_line in line:
#                 pdf.ln(3)
#                 pdf.set_font("Arial", 'B', 6)
#                 pdf.cell(0, 8, "Inaccurate Bankruptcy Information:", ln=True)

#                 # Table Headers
#                 pdf.set_font("Arial", 'B', 6)
#                 table_headers = ["Court Name or Creditor", "Case/Account Number", "Filing/Reporting Date", "Reason for Dispute"]
#                 column_widths = [35, 35, 35, 50]

#                 for i, header in enumerate(table_headers):
#                     pdf.cell(column_widths[i], 6, header, border=1, align='C')
#                 pdf.ln()

#                 # Table Data (Placeholder values)
#                 pdf.set_font("Arial", size=6)
#                 row_data = ["[Bankruptcy Court Name]", "[Case Number]", "[Filing Date]", "[incorrect filing date]"]

#                 for i, data in enumerate(row_data):
#                     pdf.cell(column_widths[i], 6, data, border=1, align='C')
#                 pdf.ln(6)

#         pdf.output(output_path)
#         print(f"PDF saved successfully at: {output_path}")
#     except Exception as e:
#         print(f"Error saving PDF: {str(e)}") 


# if __name__ == "__main__":
#     file_path = r"C:\Users\Ali Com\OneDrive\Desktop\django_temple\Ai_output_data.json"
#     output_pdf_path = r"C:\Users\Ali Com\OneDrive\Desktop\django_temple\dispute_generator\generator.pdf"

#     data = read_parsed_data(file_path)

#     if data:
#         letter = generate_dispute_letter_google(data)
#         print("\nGenerated Dispute Letter:\n")
#         print(letter)

#         save_letter_as_pdf(letter, output_pdf_path) 


#########REMOVE FUNCTIONALITY OF PDF
# from dotenv import load_dotenv
# import os
# import google.generativeai as genai
# import json
# import re

# # Configure Google Generative AI
# genai.configure(api_key="AIzaSyCOD6opLtT3s23x0r7a7MzoXIzWtg2GgT0")

# def read_parsed_data(file_path):
#     """Read and parse JSON data from a file."""
#     try:
#         with open(file_path, 'r', encoding='utf-8') as file:
#             data = json.load(file)
#         return data
#     except FileNotFoundError:
#         print(f"Error: The file '{file_path}' was not found.")
#         return None
#     except json.JSONDecodeError:
#         print(f"Error: Failed to decode JSON from the file '{file_path}'.")
#         return None

# def clean_text(text):
#     """Remove unwanted symbols from headings."""
#     return re.sub(r'[\*#]', '', text)

# def generate_dispute_letter_google(parsed_data):
#     """Generate a dispute letter using Google's Generative AI model."""
#     parsed_data_str = json.dumps(parsed_data, indent=4)
    
#     prompt = clean_text(f"""
#  Based on the following extracted data, generate a professional dispute letter.
#  Apply these classification rules:  

#  - Do NOT include any '*' symbols around headings.  
#  - Use clear headings without special formatting characters like asterisks.  

#  Generate the following structure:

#  Bankruptcy Dispute Letter Template  

#    [Your Name]  
#    [Your Address]  
#    [City, State, ZIP Code]  
#    [Date]  

#    [Credit Bureau Name] Dispute Department  
#    [Address of Credit Bureau]  

#     Subject: Dispute of Inaccurate Bankruptcy Reporting  
#     Dear [Credit Bureau Name] Dispute Department,  
#     I am writing to formally dispute the inaccurate and/or unverifiable bankruptcy information listed on my credit report. Pursuant to the Fair Credit Reporting Act (FCRA) and Metro-2 Reporting Standards, I am requesting an immediate investigation to ensure that only accurate, complete, and verifiable information is reported.
    
#     Specific Errors
#     | Court Name or Creditor | Case/Account Number | Filing/Reporting Date | Reason for Dispute |
#     |------------------------|---------------------|----------------------|--------------------|
#     | [Bankruptcy Court Name] | [Case Number] | [Filing Date] | [Incorrect Filing Date] |
    
#     Requested Action

#      1. Verify with the appropriate court that the reported bankruptcy information is accurate, complete, and up-to-date.  
#      2. Remove the bankruptcy information if it cannot be verified as accurate and complete.  
#      3. Notify me in writing once the investigation is complete and confirm the actions taken regarding the disputed information.  

#      Legal Basis for Dispute
#      Under FCRA Section 611 (15 U.S.C. § 1681i), credit reporting agencies are required to investigate disputes and verify the accuracy of the reported information. Additionally:
#        - FCRA Section 609 (15 U.S.C. § 1681g) provides me with the right to request how this bankruptcy was verified.  
#        - Metro-2 Reporting Standards dictate accurate and timely reporting of bankruptcy status and details.  
#        - Inaccurate or unverifiable public record information violates FCRA Section 623 (15 U.S.C. § 1681s-2).  

#     Supporting Documents
#     I have enclosed the following documents to assist in your investigation:
#      1. Copy of my government-issued ID.  
#      2. Copy of my credit report with the disputed bankruptcy information highlighted.  
#      3. Court records and/or other supporting evidence showing inaccuracies in the reporting.  

#      Additional Notes
#      This information must be verified directly with the court and not with third-party vendors. If this information cannot be verified as accurate and complete, it must be removed under FCRA Section 611(a)(5)(A).  
#      I expect a resolution to this matter within the 30-day period as required by law.  
#      Thank you for your prompt attention to this matter.  

#      Sincerely,  
#     [Your Full Name]  

#      Enclosures
#      1. Copy of Government-issued ID  
#      2. Highlighted Credit Report  
#      3. Court Records/Supporting Documentation  

#     Extract and populate the details from 'parsed_data' where appropriate.
#     """)

#     try:
#         model = genai.GenerativeModel("gemini-pro")
#         response = model.generate_content(prompt)
#         return response.text.strip()
#     except Exception as e:
#         return f"Error generating letter: {str(e)}"

# if __name__ == "__main__":
#     file_path = r"C:\Users\Ali Com\OneDrive\Desktop\django_temple\Ai_output_data.json"
    
#     data = read_parsed_data(file_path)

#     if data:
#         letter = generate_dispute_letter_google(data)
#         print("\nGenerated Dispute Letter:\n")
#         print(letter)

###Convert MARKDOWN to pdf:

# from dotenv import load_dotenv 
# import os
# import google.generativeai as genai
# import json
# import re
# from fpdf import FPDF

# # Configure Google Generative AI
# genai.configure(api_key="AIzaSyCOD6opLtT3s23x0r7a7MzoXIzWtg2GgT0")

# def read_parsed_data(file_path):
#     """Read and parse JSON data from a file."""
#     try:
#         with open(file_path, 'r', encoding='utf-8') as file:
#             data = json.load(file)
#         return data
#     except FileNotFoundError:
#         print(f"Error: The file '{file_path}' was not found.")
#         return None
#     except json.JSONDecodeError:
#         print(f"Error: Failed to decode JSON from the file '{file_path}'.")
#         return None

# def clean_text(text):
#     """Remove unwanted symbols from headings."""
#     return re.sub(r'[\*#]', '', text)

# def generate_dispute_letter_google(parsed_data):
#     """Generate a dispute letter using Google's Generative AI model."""
#     parsed_data_str = json.dumps(parsed_data, indent=4)
    
#     prompt = clean_text(f"""
#     Based on the following extracted data, generate a professional dispute letter.
#     Apply these classification rules:  

#     - Do NOT include any '*' symbols around headings.  
#     - Use clear headings without special formatting characters like asterisks.  

#     Generate the following structure:

#     Bankruptcy Dispute Letter Template  

#       [Your Name]  
#       [Your Address]  
#       [City, State, ZIP Code]  
#       [Date]  

#       [Credit Bureau Name] Dispute Department  
#       [Address of Credit Bureau]  

#       Subject: Dispute of Inaccurate Bankruptcy Reporting  
#       Dear [Credit Bureau Name] Dispute Department,  
#       I am writing to formally dispute the inaccurate and/or unverifiable bankruptcy information listed on my credit report. Pursuant to the Fair Credit Reporting Act (FCRA) and Metro-2 Reporting Standards, I am requesting an immediate investigation to ensure that only accurate, complete, and verifiable information is reported.
    
#       Specific Errors:
#       | Court Name or Creditor | Case/Account Number | Filing/Reporting Date | Reason for Dispute |
#       |------------------------|---------------------|----------------------|--------------------|
#       | [Bankruptcy Court Name] | [Case Number] | [Filing Date] | [Incorrect Filing Date] |
    
#       Requested Action:

#       1. Verify with the appropriate court that the reported bankruptcy information is accurate, complete, and up-to-date.  
#       2. Remove the bankruptcy information if it cannot be verified as accurate and complete.  
#       3. Notify me in writing once the investigation is complete and confirm the actions taken regarding the disputed information.  

#       Legal Basis for Dispute:
#       Under FCRA Section 611 (15 U.S.C. § 1681i), credit reporting agencies are required to investigate disputes and verify the accuracy of the reported information. Additionally:
#         - FCRA Section 609 (15 U.S.C. § 1681g) provides me with the right to request how this bankruptcy was verified.  
#         - Metro-2 Reporting Standards dictate accurate and timely reporting of bankruptcy status and details.  
#         - Inaccurate or unverifiable public record information violates FCRA Section 623 (15 U.S.C. § 1681s-2).  

#       Supporting Documents:
#       I have enclosed the following documents to assist in your investigation:
#       1. Copy of my government-issued ID.  
#       2. Copy of my credit report with the disputed bankruptcy information highlighted.  
#       3. Court records and/or other supporting evidence showing inaccuracies in the reporting.  

#       Additional Notes:
#       This information must be verified directly with the court and not with third-party vendors. If this information cannot be verified as accurate and complete, it must be removed under FCRA Section 611(a)(5)(A).  
#       I expect a resolution to this matter within the 30-day period as required by law.  
#       Thank you for your prompt attention to this matter.  

#       Sincerely,  
#       [Your Full Name]  

#       Enclosures:
#       1. Copy of Government-issued ID  
#       2. Highlighted Credit Report  
#       3. Court Records/Supporting Documentation  

#       Extract and populate the details from 'parsed_data' where appropriate.
#     """)

#     try:
#         model = genai.GenerativeModel("gemini-pro")
#         response = model.generate_content(prompt)
#         return response.text.strip()
#     except Exception as e:
#         return f"Error generating letter: {str(e)}"

# def save_letter_as_pdf(letter_content, output_path):
#     """Save the generated letter content to a PDF file with a properly formatted table."""
#     try:
#         pdf = FPDF()
#         pdf.set_auto_page_break(auto=True, margin=10)
#         pdf.add_page()
#         pdf.set_font("Arial", size=10)

#         content_parts = clean_text(letter_content).split('\n')

#         for line in content_parts:
#             if "|" in line and "-" not in line:  # Table Data Row (ignoring separator lines)
#                 columns = [col.strip() for col in line.split('|')[1:-1]]  # Remove empty leading/trailing parts
                
#                 if len(columns) == 4:  # Ensure it's a valid row
#                     column_widths = [50, 50, 50, 50]
#                     for i, column in enumerate(columns):
#                         pdf.cell(column_widths[i], 6, column, border=1, align='C')
#                     pdf.ln()
#                 else:
#                     pdf.multi_cell(0, 6, line.strip())  # Add non-table text
#                     pdf.ln(2)

#             elif "|---" not in line:  # Ignore separator lines
#                 pdf.multi_cell(0, 6, line.strip())  
#                 pdf.ln(2)
        
#         pdf.output(output_path)
#         print(f"PDF saved successfully at: {output_path}")
#     except Exception as e:
#         print(f"Error saving PDF: {str(e)}")

# if __name__ == "__main__":
#     file_path = r"C:\Users\Ali Com\OneDrive\Desktop\django_temple\Ai_output_data.json"
#     output_pdf_path = r"C:\Users\Ali Com\OneDrive\Desktop\django_temple\dispute_generator\generator.pdf"
    
#     data = read_parsed_data(file_path)

#     if data:
#         letter = generate_dispute_letter_google(data)
#         print("\nGenerated Dispute Letter:\n")
#         print(letter)

#         save_letter_as_pdf(letter, output_pdf_path)
##reduce font size:
# from dotenv import load_dotenv  
# import os
# import google.generativeai as genai
# import json
# import re
# from fpdf import FPDF

# # Configure Google Generative AI
# genai.configure(api_key="AIzaSyCOD6opLtT3s23x0r7a7MzoXIzWtg2GgT0")

# def read_parsed_data(file_path):
#     """Read and parse JSON data from a file."""
#     try:
#         with open(file_path, 'r', encoding='utf-8') as file:
#             data = json.load(file)
#         return data
#     except FileNotFoundError:
#         print(f"Error: The file '{file_path}' was not found.")
#         return None
#     except json.JSONDecodeError:
#         print(f"Error: Failed to decode JSON from the file '{file_path}'.")
#         return None

# def clean_text(text):
#     """Remove unwanted symbols from headings."""
#     return re.sub(r'[\*#]', '', text)

# def generate_dispute_letter_google(parsed_data):
#     """Generate a dispute letter using Google's Generative AI model."""
#     parsed_data_str = json.dumps(parsed_data, indent=4)
    
#     prompt = clean_text(f"""
#     Based on the following extracted data, generate a professional dispute letter.
#     Apply these classification rules:  

#     - Do NOT include any '*' symbols around headings.  
#     - Use clear headings without special formatting characters like asterisks.  

#     Generate the following structure:

#     Bankruptcy Dispute Letter Template  

#       [Your Name]  
#       [Your Address]  
#       [City, State, ZIP Code]  
#       [Date]  

#       [Credit Bureau Name] Dispute Department  
#       [Address of Credit Bureau]  

#       Subject: Dispute of Inaccurate Bankruptcy Reporting  
#       Dear [Credit Bureau Name] Dispute Department,  
#       I am writing to formally dispute the inaccurate and/or unverifiable bankruptcy information listed on my credit report. Pursuant to the Fair Credit Reporting Act (FCRA) and Metro-2 Reporting Standards, I am requesting an immediate investigation to ensure that only accurate, complete, and verifiable information is reported.
    
#       Inaccurate Bankruptcy Information:
                        
#       | Court Name or Creditor | Case/Account Number | Filing/Reporting Date | Reason for Dispute |
#       |------------------------|---------------------|----------------------|--------------------|
#       | [Bankruptcy Court Name] | [Case Number] | [Filing Date] | [Incorrect Filing Date] |

#       Specific Errors
#           1. Case Information:  
#             - Error(s): Incorrect court name, case number mismatch, improper status as open, incorrect filing or discharge date.  
#             - Supporting Evidence: Court documents showing case resolution or absence of filing.  
#           2. Public Record Reporting:  
#            - Error(s): Record not verified with the appropriate court, incorrect inclusion in report after removal.  
#            - Supporting Evidence: Statement or response from the court or other public record sources.                    

#       Requested Action:

#       1. Verify with the appropriate court that the reported bankruptcy information is accurate, complete, and up-to-date.  
#       2. Remove the bankruptcy information if it cannot be verified as accurate and complete.  
#       3. Notify me in writing once the investigation is complete and confirm the actions taken regarding the disputed information.  

#       Legal Basis for Dispute:
#       Under FCRA Section 611 (15 U.S.C. § 1681i), credit reporting agencies are required to investigate disputes and verify the accuracy of the reported information. Additionally:
#         - FCRA Section 609 (15 U.S.C. § 1681g) provides me with the right to request how this bankruptcy was verified.  
#         - Metro-2 Reporting Standards dictate accurate and timely reporting of bankruptcy status and details.  
#         - Inaccurate or unverifiable public record information violates FCRA Section 623 (15 U.S.C. § 1681s-2).  

#       Supporting Documents:
#       I have enclosed the following documents to assist in your investigation:
#       1. Copy of my government-issued ID.  
#       2. Copy of my credit report with the disputed bankruptcy information highlighted.  
#       3. Court records and/or other supporting evidence showing inaccuracies in the reporting.  

#       Additional Notes:
#       This information must be verified directly with the court and not with third-party vendors. If this information cannot be verified as accurate and complete, it must be removed under FCRA Section 611(a)(5)(A).  
#       I expect a resolution to this matter within the 30-day period as required by law.  
#       Thank you for your prompt attention to this matter.  

#       Sincerely,  
#       [Your Full Name]  

#       Enclosures:
#       1. Copy of Government-issued ID  
#       2. Highlighted Credit Report  
#       3. Court Records/Supporting Documentation  

#       Extract and populate the details from 'parsed_data' where appropriate.
#     """)

#     try:
#         model = genai.GenerativeModel("gemini-pro")
#         response = model.generate_content(prompt)
#         return response.text.strip()
#     except Exception as e:
#         return f"Error generating letter: {str(e)}"

# def save_letter_as_pdf(letter_content, output_path):
#     """Save the generated letter content to a PDF file with a properly formatted table."""
#     try:
#         pdf = FPDF()
#         pdf.set_auto_page_break(auto=True, margin=10)
#         pdf.add_page()
#         pdf.set_font("Arial", size=8)  # Reduced font size to 8

#         content_parts = clean_text(letter_content).split('\n')

#         for line in content_parts:
#             if "|" in line and "-" not in line:  # Table Data Row (ignoring separator lines)
#                 columns = [col.strip() for col in line.split('|')[1:-1]]  # Remove empty leading/trailing parts
                
#                 if len(columns) == 4:  # Ensure it's a valid row
#                     column_widths = [50, 50, 50, 50]
#                     for i, column in enumerate(columns):
#                         pdf.cell(column_widths[i], 5, column, border=1, align='C')  # Reduced row height
#                     pdf.ln()
#                 else:
#                     pdf.multi_cell(0, 5, line.strip())  # Add non-table text with reduced spacing
#                     pdf.ln(1)

#             elif "|---" not in line:  # Ignore separator lines
#                 pdf.multi_cell(0, 5, line.strip())  
#                 pdf.ln(1)
        
#         pdf.output(output_path)
#         print(f"PDF saved successfully at: {output_path}")
#     except Exception as e:
#         print(f"Error saving PDF: {str(e)}")

# if __name__ == "__main__":
#     file_path = r"C:\Users\Ali Com\OneDrive\Desktop\django_temple\Ai_output_data.json"
#     output_pdf_path = r"C:\Users\Ali Com\OneDrive\Desktop\django_temple\dispute_generator\generator.pdf"
    
#     data = read_parsed_data(file_path)

#     if data:
#         letter = generate_dispute_letter_google(data)
#         print("\nGenerated Dispute Letter:\n")
#         print(letter)

#         save_letter_as_pdf(letter, output_pdf_path)


###fontsize #corrrect
# from dotenv import load_dotenv  
# import os
# import google.generativeai as genai
# import json
# import re
# from fpdf import FPDF

# # Configure Google Generative AI
# genai.configure(api_key="AIzaSyCOD6opLtT3s23x0r7a7MzoXIzWtg2GgT0")

# def read_parsed_data(file_path):
#     """Read and parse JSON data from a file."""
#     try:
#         with open(file_path, 'r', encoding='utf-8') as file:
#             data = json.load(file)
#         return data
#     except FileNotFoundError:
#         print(f"Error: The file '{file_path}' was not found.")
#         return None
#     except json.JSONDecodeError:
#         print(f"Error: Failed to decode JSON from the file '{file_path}'.")
#         return None

# def clean_text(text):
#     """Remove unwanted symbols from headings."""
#     return re.sub(r'[\*#]', '', text)

# def generate_dispute_letter_google(parsed_data):
#     """Generate a dispute letter using Google's Generative AI model."""
#     parsed_data_str = json.dumps(parsed_data, indent=4)
    
#     prompt = clean_text(f"""
#     Based on the following extracted data, generate a professional dispute letter.
#     Apply these classification rules:  

#     - Do NOT include any '*' symbols around headings.  
#     - Use clear headings without special formatting characters like asterisks.  

#     Generate the following structure:

#     Bankruptcy Dispute Letter Template  

#       [Your Name]  
#       [Your Address]  
#       [City, State, ZIP Code]  
#       [Date]  

#       [Credit Bureau Name] Dispute Department  
#       [Address of Credit Bureau]  

#       Subject: Dispute of Inaccurate Bankruptcy Reporting  
#       Dear [Credit Bureau Name] Dispute Department,  
#       I am writing to formally dispute the inaccurate and/or unverifiable bankruptcy information listed on my credit report. Pursuant to the Fair Credit Reporting Act (FCRA) and Metro-2 Reporting Standards, I am requesting an immediate investigation to ensure that only accurate, complete, and verifiable information is reported.
    
#       Inaccurate Bankruptcy Information:
                        
#       | Court Name or Creditor | Case/Account Number | Filing/Reporting Date | Reason for Dispute |
#       |------------------------|---------------------|----------------------|--------------------|
#       | [Bankruptcy Court Name] | [Case Number] | [Filing Date] | [Incorrect Filing Date] |

#       Specific Errors
#           1. Case Information:  
#             - Error(s): Incorrect court name, case number mismatch, improper status as open, incorrect filing or discharge date.  
#             - Supporting Evidence: Court documents showing case resolution or absence of filing.  
#           2. Public Record Reporting:  
#            - Error(s): Record not verified with the appropriate court, incorrect inclusion in report after removal.  
#            - Supporting Evidence: Statement or response from the court or other public record sources.                    

#       Requested Action:

#       1. Verify with the appropriate court that the reported bankruptcy information is accurate, complete, and up-to-date.  
#       2. Remove the bankruptcy information if it cannot be verified as accurate and complete.  
#       3. Notify me in writing once the investigation is complete and confirm the actions taken regarding the disputed information.  

#       Legal Basis for Dispute:
#       Under FCRA Section 611 (15 U.S.C. § 1681i), credit reporting agencies are required to investigate disputes and verify the accuracy of the reported information. Additionally:
#         - FCRA Section 609 (15 U.S.C. § 1681g) provides me with the right to request how this bankruptcy was verified.  
#         - Metro-2 Reporting Standards dictate accurate and timely reporting of bankruptcy status and details.  
#         - Inaccurate or unverifiable public record information violates FCRA Section 623 (15 U.S.C. § 1681s-2).  

#       Supporting Documents:
#       I have enclosed the following documents to assist in your investigation:
#       1. Copy of my government-issued ID.  
#       2. Copy of my credit report with the disputed bankruptcy information highlighted.  
#       3. Court records and/or other supporting evidence showing inaccuracies in the reporting.  

#       Additional Notes:
#       This information must be verified directly with the court and not with third-party vendors. If this information cannot be verified as accurate and complete, it must be removed under FCRA Section 611(a)(5)(A).  
#       I expect a resolution to this matter within the 30-day period as required by law.  
#       Thank you for your prompt attention to this matter.  

#       Sincerely,  
#       [Your Full Name]  

#       Enclosures:
#       1. Copy of Government-issued ID  
#       2. Highlighted Credit Report  
#       3. Court Records/Supporting Documentation  

#       Extract and populate the details from 'parsed_data' where appropriate.
#     """)

#     try:
#         model = genai.GenerativeModel("gemini-pro")
#         response = model.generate_content(prompt)
#         return response.text.strip()
#     except Exception as e:
#         return f"Error generating letter: {str(e)}"

# from fpdf import FPDF

# def save_letter_as_pdf(letter_content, output_path):
#     """Save the generated letter content to a PDF file with a properly formatted table."""
#     try:
#         pdf = FPDF()
#         pdf.set_auto_page_break(auto=True, margin=5)
#         pdf.add_page()
#         pdf.set_font("Arial", size=7)  # Increased font size to 7

#         content_parts = clean_text(letter_content).split('\n')

#         for line in content_parts:
#             line = line.strip()
#             if line:  # Remove blank lines
#                 if "|" in line and "-" not in line:  # Table Data Row (ignoring separator lines)
#                     columns = [col.strip() for col in line.split('|')[1:-1]]  # Remove empty leading/trailing parts
                    
#                     if len(columns) == 4:  # Ensure it's a valid row
#                         column_widths = [40, 40, 40, 40]
#                         for i, column in enumerate(columns):
#                             pdf.cell(column_widths[i], 5, column, border=1, align='C')  # Increased row height
#                         pdf.ln()
#                     else:
#                         pdf.multi_cell(0, 5, line)  # Adjusted spacing
#                 elif "|---" not in line:  # Ignore separator lines
#                     pdf.multi_cell(0, 5, line)
        
#         pdf.output(output_path)
#         print(f"PDF saved successfully at: {output_path}")
#     except Exception as e:
#         print(f"Error saving PDF: {str(e)}")

# if __name__ == "__main__":
#     file_path = r"C:\Users\Ali Com\OneDrive\Desktop\django_temple\Ai_output_data.json"
#     output_pdf_path = r"C:\Users\Ali Com\OneDrive\Desktop\django_temple\dispute_generator\generator.pdf"
    
#     data = read_parsed_data(file_path)

#     if data:
#         letter = generate_dispute_letter_google(data)
#         print("\nGenerated Dispute Letter:\n")
#         print(letter)

#         save_letter_as_pdf(letter, output_pdf_path) 

###bold heading :
from dotenv import load_dotenv  
import os
import google.generativeai as genai
import json
import re
from fpdf import FPDF

# Configure Google Generative AI
genai.configure(api_key="AIzaSyCOD6opLtT3s23x0r7a7MzoXIzWtg2GgT0")

def read_parsed_data(file_path):
    """Read and parse JSON data from a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from the file '{file_path}'.")
        return None

def clean_text(text):
    """Remove unwanted symbols from headings."""
    return re.sub(r'[\*#]', '', text)

def generate_dispute_letter_google(parsed_data):
    """Generate a dispute letter using Google's Generative AI model."""
    parsed_data_str = json.dumps(parsed_data, indent=4)
    
    prompt = clean_text(f"""
    Based on the following extracted data, generate a professional dispute letter.
    Apply these classification rules:  

    - Do NOT include any '*' symbols around headings.  
    - Use clear headings without special formatting characters like asterisks.  

    Generate the following structure:

      [Your Name]  
      [Your Address]  
      [City, State, ZIP Code]  
      [Date]  

      [Credit Bureau Name] Dispute Department  
      [Address of Credit Bureau]  

      Subject: Dispute of Inaccurate Bankruptcy Reporting  
      Dear [Credit Bureau Name] Dispute Department,  
      I am writing to formally dispute the inaccurate and/or unverifiable bankruptcy information listed on my credit report. Pursuant to the Fair Credit Reporting Act (FCRA) and Metro-2 Reporting Standards, I am requesting an immediate investigation to ensure that only accurate, complete, and verifiable information is reported.
    
      Inaccurate Bankruptcy Information:
                        
      | Court Name or Creditor | Case/Account Number | Filing/Reporting Date | Reason for Dispute |
      |------------------------|---------------------|----------------------|--------------------|
      | [Bankruptcy Court Name] | [Case Number] | [Filing Date] | [Incorrect Filing Date] |

      Specific Errors:
          1. Case Information:  
            - Error(s): Incorrect court name, case number mismatch, improper status as open, incorrect filing or discharge date.  
            - Supporting Evidence: Court documents showing case resolution or absence of filing.  
          2. Public Record Reporting:  
           - Error(s): Record not verified with the appropriate court, incorrect inclusion in report after removal.  
           - Supporting Evidence: Statement or response from the court or other public record sources.                    

      Requested Action:

      1. Verify with the appropriate court that the reported bankruptcy information is accurate, complete, and up-to-date.  
      2. Remove the bankruptcy information if it cannot be verified as accurate and complete.  
      3. Notify me in writing once the investigation is complete and confirm the actions taken regarding the disputed information.  

      Legal Basis for Dispute:
      Under FCRA Section 611 (15 U.S.C. § 1681i), credit reporting agencies are required to investigate disputes and verify the accuracy of the reported information. Additionally:
        - FCRA Section 609 (15 U.S.C. § 1681g) provides me with the right to request how this bankruptcy was verified.  
        - Metro-2 Reporting Standards dictate accurate and timely reporting of bankruptcy status and details.  
        - Inaccurate or unverifiable public record information violates FCRA Section 623 (15 U.S.C. § 1681s-2).  

      Supporting Documents:
      I have enclosed the following documents to assist in your investigation:
      1. Copy of my government-issued ID.  
      2. Copy of my credit report with the disputed bankruptcy information highlighted.  
      3. Court records and/or other supporting evidence showing inaccuracies in the reporting.  

      Additional Notes:
      This information must be verified directly with the court and not with third-party vendors. If this information cannot be verified as accurate and complete, it must be removed under FCRA Section 611(a)(5)(A).  
      I expect a resolution to this matter within the 30-day period as required by law.  
      Thank you for your prompt attention to this matter.  

      Sincerely,  
      [Your Full Name]  

      Enclosures:
      1. Copy of Government-issued ID  
      2. Highlighted Credit Report  
      3. Court Records/Supporting Documentation  

      Extract and populate the details from 'base_knowleged' where appropriate.
    """)

    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error generating letter: {str(e)}"


from fpdf import FPDF

def save_letter_as_pdf(letter_content, output_path):
    """Save the generated letter content to a PDF file with a properly formatted table."""
    try:
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=5)
        pdf.add_page()
        
        # Set font for the title
        pdf.set_font("Arial", style='B', size=8)  # Increased font size by 1 digit (from 7 to 8)
        
        # Center the "Bankruptcy Dispute Letter Template" at the top
        pdf.cell(0, 10, "Bankruptcy Dispute Letter Template", ln=True, align='C')  # Align to center
        
        # Add a small line break after the title
        pdf.ln(10)  # Line break
        
        # Set the regular font for the body text
        pdf.set_font("Arial", size=7)  # Regular font for content

        content_parts = clean_text(letter_content).split('\n')

        for line in content_parts:
            line = line.strip()
            if line:  # Remove blank lines
                # Bold the heading
                if line.endswith(":"):  # Assuming headings end with a colon
                    pdf.set_font("Arial", style='B', size=7)  # Set bold for headings
                    pdf.multi_cell(0, 5, line)  # Add a line space after each heading
                    pdf.set_font("Arial", size=7)  # Reset font to regular for body content
                elif "|" in line and "-" not in line:  # Table Data Row (ignoring separator lines)
                    columns = [col.strip() for col in line.split('|')[1:-1]]  # Remove empty leading/trailing parts
                    
                    if len(columns) == 4:  # Ensure it's a valid row
                        column_widths = [40, 40, 40, 40]
                        for i, column in enumerate(columns):
                            pdf.cell(column_widths[i], 5, column, border=1, align='C')  # Increased row height
                        pdf.ln()
                    else:
                        pdf.multi_cell(0, 5, line)  # Adjusted spacing
                elif "|---" not in line:  # Ignore separator lines
                    pdf.multi_cell(0, 5, line)
        
        pdf.output(output_path)
        print(f"PDF saved successfully at: {output_path}")
    except Exception as e:
        print(f"Error saving PDF: {str(e)}")


if __name__ == "__main__":
    file_path = r"C:\Users\Ali Com\OneDrive\Desktop\django_temple\Ai_output_data.json"
    output_pdf_path = r"C:\Users\Ali Com\OneDrive\Desktop\django_temple\dispute_generator\generator.pdf"
    
    data = read_parsed_data(file_path)

    if data:
        letter = generate_dispute_letter_google(data)
        print("\nGenerated Dispute Letter:\n")
        print(letter)

        save_letter_as_pdf(letter, output_pdf_path) 

#fecthing data from database:
# from dotenv import load_dotenv  
# import os
# import google.generativeai as genai
# import json
# import re
# from fpdf import FPDF

# # Configure Google Generative AI
# genai.configure(api_key="AIzaSyCOD6opLtT3s23x0r7a7MzoXIzWtg2GgT0")

# def read_parsed_data(file_path):
#     """Read and parse JSON data from a file."""
#     try:
#         with open(file_path, 'r', encoding='utf-8') as file:
#             data = json.load(file)
#         return data
#     except FileNotFoundError:
#         print(f"Error: The file '{file_path}' was not found.")
#         return None
#     except json.JSONDecodeError:
#         print(f"Error: Failed to decode JSON from the file '{file_path}'.")
#         return None

# def clean_text(text):
#     """Remove unwanted symbols from headings."""
#     return re.sub(r'[\*#]', '', text)

# def generate_dispute_letter_google(parsed_data):
#     """Generate a dispute letter using Google's Generative AI model."""
#     parsed_data_str = json.dumps(parsed_data, indent=4)

#     # Fetching data from 'base_knowledge' to populate the table
#     base_knowledge = parsed_data.get('base_knowledge', {})
#     court_name = base_knowledge.get('court_name', '[Court Name]')
#     case_number = base_knowledge.get('case_number', '[Case Number]')
#     filing_date = base_knowledge.get('filing_date', '[Filing Date]')
#     incorrect_filing_date = base_knowledge.get('incorrect_filing_date', '[Incorrect Filing Date]')

#     # Prompt for the dispute letter
#     prompt = clean_text(f"""
#     Based on the following extracted data, generate a professional dispute letter.
#     Apply these classification rules:  

#     - Do NOT include any '*' symbols around headings.  
#     - Use clear headings without special formatting characters like asterisks.  

#     Generate the following structure:

#       [Your Name]  
#       [Your Address]  
#       [City, State, ZIP Code]  
#       [Date]  

#       [Credit Bureau Name] Dispute Department  
#       [Address of Credit Bureau]  

#       Subject: Dispute of Inaccurate Bankruptcy Reporting  
#       Dear [Credit Bureau Name] Dispute Department,  
#       I am writing to formally dispute the inaccurate and/or unverifiable bankruptcy information listed on my credit report. Pursuant to the Fair Credit Reporting Act (FCRA) and Metro-2 Reporting Standards, I am requesting an immediate investigation to ensure that only accurate, complete, and verifiable information is reported.
    
#       Inaccurate Bankruptcy Information:
                        
#       | Court Name or Creditor | Case/Account Number | Filing/Reporting Date | Reason for Dispute |
#       |------------------------|---------------------|----------------------|--------------------|
#       | {court_name} | {case_number} | {filing_date} | {incorrect_filing_date} |

#       Specific Errors:
#           1. Case Information:  
#             - Error(s): Incorrect court name, case number mismatch, improper status as open, incorrect filing or discharge date.  
#             - Supporting Evidence: Court documents showing case resolution or absence of filing.  
#           2. Public Record Reporting:  
#            - Error(s): Record not verified with the appropriate court, incorrect inclusion in report after removal.  
#            - Supporting Evidence: Statement or response from the court or other public record sources.                    

#       Requested Action:

#       1. Verify with the appropriate court that the reported bankruptcy information is accurate, complete, and up-to-date.  
#       2. Remove the bankruptcy information if it cannot be verified as accurate and complete.  
#       3. Notify me in writing once the investigation is complete and confirm the actions taken regarding the disputed information.  

#       Legal Basis for Dispute:
#       Under FCRA Section 611 (15 U.S.C. § 1681i), credit reporting agencies are required to investigate disputes and verify the accuracy of the reported information. Additionally:
#         - FCRA Section 609 (15 U.S.C. § 1681g) provides me with the right to request how this bankruptcy was verified.  
#         - Metro-2 Reporting Standards dictate accurate and timely reporting of bankruptcy status and details.  
#         - Inaccurate or unverifiable public record information violates FCRA Section 623 (15 U.S.C. § 1681s-2).  

#       Supporting Documents:
#       I have enclosed the following documents to assist in your investigation:
#       1. Copy of my government-issued ID.  
#       2. Copy of my credit report with the disputed bankruptcy information highlighted.  
#       3. Court records and/or other supporting evidence showing inaccuracies in the reporting.  

#       Additional Notes:
#       This information must be verified directly with the court and not with third-party vendors. If this information cannot be verified as accurate and complete, it must be removed under FCRA Section 611(a)(5)(A).  
#       I expect a resolution to this matter within the 30-day period as required by law.  
#       Thank you for your prompt attention to this matter.  

#       Sincerely,  
#       [Your Full Name]  

#       Enclosures:
#       1. Copy of Government-issued ID  
#       2. Highlighted Credit Report  
#       3. Court Records/Supporting Documentation  

#       Extract and populate the details from 'base_knowleged' where appropriate.
#     """)

#     try:
#         model = genai.GenerativeModel("gemini-pro")
#         response = model.generate_content(prompt)
#         return response.text.strip()
#     except Exception as e:
#         return f"Error generating letter: {str(e)}"


# from fpdf import FPDF

# def save_letter_as_pdf(letter_content, output_path):
#     """Save the generated letter content to a PDF file with a properly formatted table."""
#     try:
#         pdf = FPDF()
#         pdf.set_auto_page_break(auto=True, margin=5)
#         pdf.add_page()
        
#         # Set font for the title
#         pdf.set_font("Arial", style='B', size=9)  # Increased font size by 1 digit (from 7 to 8)
        
#         # Center the "Bankruptcy Dispute Letter Template" at the top
#         pdf.cell(0, 10, "Bankruptcy Dispute Letter Template", ln=True, align='C')  # Align to center
        
#         # Add a small line break after the title
#         pdf.ln(10)  # Line break
        
#         # Set the regular font for the body text
#         pdf.set_font("Arial", size=7)  # Regular font for content

#         content_parts = clean_text(letter_content).split('\n')

#         for line in content_parts:
#             line = line.strip()
#             if line:  # Remove blank lines
#                 # Bold the heading
#                 if line.endswith(":"):  # Assuming headings end with a colon
#                     pdf.set_font("Arial", style='B', size=7)  # Set bold for headings
#                     pdf.multi_cell(0, 5, line)  # Add a line space after each heading
#                     pdf.set_font("Arial", size=7)  # Reset font to regular for body content
#                 elif "|" in line and "-" not in line:  # Table Data Row (ignoring separator lines)
#                     columns = [col.strip() for col in line.split('|')[1:-1]]  # Remove empty leading/trailing parts
                    
#                     if len(columns) == 4:  # Ensure it's a valid row
#                         column_widths = [40, 40, 40, 40]
#                         for i, column in enumerate(columns):
#                             pdf.cell(column_widths[i], 5, column, border=1, align='C')  # Increased row height
#                         pdf.ln()
#                     else:
#                         pdf.multi_cell(0, 5, line)  # Adjusted spacing
#                 elif "|---" not in line:  # Ignore separator lines
#                     pdf.multi_cell(0, 5, line)
        
#         pdf.output(output_path)
#         print(f"PDF saved successfully at: {output_path}")
#     except Exception as e:
#         print(f"Error saving PDF: {str(e)}")


# if __name__ == "__main__":
#     file_path = r"C:\Users\Ali Com\OneDrive\Desktop\django_temple\Ai_output_data.json"
#     output_pdf_path = r"C:\Users\Ali Com\OneDrive\Desktop\django_temple\dispute_generator\generator.pdf"
    
#     data = read_parsed_data(file_path)

#     if data:
#         letter = generate_dispute_letter_google(data)
#         print("\nGenerated Dispute Letter:\n")
#         print(letter)

#         save_letter_as_pdf(letter, output_pdf_path)   


