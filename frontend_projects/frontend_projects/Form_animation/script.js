const labels = document.querySelector('.form-control label')

labels.foreach(label=>{
    label.innerHTML = label.innerText
    .split('')
    .map((letter,idx)=>`<span style="transition-delay:${idx
    *50}">${letter}</span>`)
    .join('')
});