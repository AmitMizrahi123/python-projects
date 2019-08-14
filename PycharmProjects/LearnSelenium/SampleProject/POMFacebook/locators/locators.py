class Locators:

    # login information
    email_textbox_name = 'email'
    password_textbox_name = 'pass'
    button_login_id = 'loginbutton'

    # errors information
    errorUsername_xpath = '//*[@id="globalContainer"]/div[3]/div/div/div'
    errorPassword_xpath = '//*[@id="globalContainer"]/div[3]/div/div/div'
    errorUsernameOrPassword_box_id = 'error_box'

    # forgot password
    forgot_password_linkText = 'שכחת את החשבון?'
    recoverUsername_email_id = 'identify_email'
    search_button_name = 'did_submit'
    NoSearchForEmail_error_xpath = '//*[@id="identify_yourself_flow"]/div/div[2]/div[1]'
    ifItsNotYouButton_linkText = 'לא את/ה?'

    # exit from account
    removeBlackScreen_className = '_3ixn'
    setting_logout_account_id = 'userNavigationLabel'
    logoutAccount_button_linkText = 'Log Out'
