Dropzone.autoDiscover=false;
const myDropzone= new Dropzone('#my-dropzone',{
    url:'upload/',
    maxFiles:30,
    maxFilesize:10,
    acceptedFiles: 'application/xls,application/excel,application/vnd.ms-excel,application/vnd.ms-excel; charset=binary,application/msexcel,application/x-excel,application/x-msexcel,application/x-ms-excel,application/x-dos_ms_excel,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
})