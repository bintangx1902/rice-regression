"use strict"

let dataBeras = []

document.querySelector("#year-chooser-input").addEventListener("change", (element) => {
	let choosenYear = element.target.value
	document.querySelector("#year-column").textContent = choosenYear

	$("#premium").empty()
	$("#medium").empty()
	$("#luar").empty()

	$("#premium").append("<th>Premium</th>")
	$("#medium").append("<th>Medium</th>")
	$("#luar").append("<th>Luar Kualitas</th>")

	beras.forEach((beras) => {
		if (beras.tahun == choosenYear) {
			if (beras.kualitas == "Premium") {
				$("#premium").append(`
					<td>${beras.harga}</td>
				`)
			}

			if (beras.kualitas == "Medium") {
				$("#medium").append(`
					<td>${beras.harga}</td>
				`)
			}

			if (beras.kualitas == "Luar Kualitas") {
				$("#luar").append(`
					<td>${beras.harga}</td>
				`)
			}
		}
	})
})
