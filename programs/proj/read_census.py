# Chapter 14 - Excel Spreadsheets
# (Project 9) - Gather Census Statistics
# read_census.py - Tabulates county population and census tracts

import openpyxl, pprint


def main():
    print('Opening workbook...')
    wb = openpyxl.load_workbook('censuspopdata.xlsx')
    sheet = wb['Population by Census Tract']
    county_data = {}

    # Fill in county_data with each county's population and tracts.
    print('Reading rows...')
    for row in range(2, sheet.max_row + 1):
        # Each row in the spreadsheet has data for one census tract.
        state  = sheet['B' + str(row)].value
        county = sheet['C' + str(row)].value
        pop    = sheet['D' + str(row)].value

        # Make sure the key for this state exists.
        county_data.setdefault(state, {})
        # Make sure the key for this county in this state exists.
        county_data[state].setdefault(county, {'tracts': 0, 'pop': 0})

        # Each row represents one census tract, so increment by one.
        county_data[state][county]['tracts'] += 1
        # Increase the county pop by the pop in this census tract.
        county_data[state][county]['pop'] += int(pop)

        # Open a new text file and write the contents of county_data to it.
        print('Writing results...')
        result_file = open('census2010.py', 'w')
        result_file.write('allData = ' + pprint.pformat(county_data))
        result_file.close()
        print('Done.')


if __name__ == "__main__":
    main()