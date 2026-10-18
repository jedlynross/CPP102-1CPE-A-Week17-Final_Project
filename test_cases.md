# Test Cases – Simulated Device Monitoring and Alert System

Tested by: (Jedlyn Ross D. Quejada)        Date: (October 17, 2026)
 
| Test Case | Input or Action | Expected Result | Actual Result | Pass Fail |
|---|---|---|---|---|
| TC01 | Choose 1 | Five readings: 28, 31, 35, 37, 29 | The terminal displayed all of the listed readings. | Pass |
| TC02 | Choose 2, enter 33 | Reading added successfully | The new reading was added into the list of the initial readings. | Pass |
| TC03 | Choose 2, enter abc | Rejected; list unchanged | The input was not accepted and the list did not change. | Pass |
| TC04 | Choose 2, enter -5	| Rejected; list unchanged | TThe input of negative values was not accepted and was not added to the list. | Pass |
| TC05 | Choose 2, enter 200 | Rejected; list unchanged | The input of a value above 100 was also rejected. | Pass |
| TC06 | Add 30, then choose 3 | 30 °C -> WARNING  | The value of 30 was entered and accepted. After checking the Option 1, the new reading of 30 °C was added on the current list and classified as 'WARNING' | Pass |
| TC07 | Choose 3 | 35 °C -> WARNING | The value of 35 was entered and accepted. After checking the Option 1, the new reading of 35 °C was added on the current list and classified as 'WARNING' | Pass |
| TC08 | Choose 4 (initial data) | Total 160, Avg 32.00, Min 28, Max 37, status ATTENTION REQUIRED | All the expected outputs were displayed. | Pass |
| TC09 | Enter 9 | Error message; menu shown again | There is an error message displayed in the terminal after enetring 9 and the menu was shown again after it. | Pass |
| TC010 | Choose 5 | Exit message; program ends | The program ends when 5 was input. | Pass |

## Bugs Found and Fixed
- Bug: The bug occurred in the add_reading() function because the program accepted valid temperature readings and displayed a success message, but the list of readings was not updated. This happened because the function used a different approach to validate and process the input without properly updating the existing list of readings used by the other program functions.
- Solution: The bug was fixed by using readings.append(value) after validating the input. This adds the accepted temperature reading to the existing readings list, allowing the new value to appear when the user selects View Readings or other options that use the list. The solution also validates the input to ensure that only whole numbers from 0°C to 100°C are accepted.
- The hardest part for me was figuring out how to arrange the code properly and deciding which line of code I needed to write first to fix the bug.