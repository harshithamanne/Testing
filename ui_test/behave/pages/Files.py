from ui_test.behave.pages.BasePage import BasePage


class Files(BasePage):
    files_upload_label = 'label.file-upload.file-drop-zone'
    file_upload = 'input[type=file]'
    uploaded_files = '.table-list-row.pointer.unselectable.ng-scope'
