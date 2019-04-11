# each time you crawl, clear out your database and start over:
conn = helpers.create_or_replace_table()

# write everything to a file:
file_path = helpers.get_file_path(search_term.replace(' ', '_') + '.html', subdirectory='results')
absolute_path = os.path.abspath(file_path)

f = open(file_path, 'w')
f.write(template)
f.close()

print('Copy this link into your web browser to see the results:')
print('file://' + absolute_path)
try:
    # open web browser with the results:
    browser= webbrowser.get('chrome')
    browser.open('file://' + absolute_path)
except:
    print('Your web page did not open automatically.')