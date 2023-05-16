methods: {
  convertToPDF() {
    const element = document.getElementById('your-template-id'); // Replace 'your-template-id' with the ID of your template element

    const opt = {
      margin:       0,
      filename:     'your-filename.pdf', // Replace 'your-filename' with the desired name of the PDF file
      image:        { type: 'jpeg', quality: 0.98 },
      html2canvas:  { scale: 2 },
      jsPDF:        { unit: 'mm', format: 'a4', orientation: 'portrait' }
    };

    html2pdf().from(element).set(opt).save();
  }
}
