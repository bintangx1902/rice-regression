"use strict"

let chart

document.querySelector("#year-chooser-input").addEventListener("change", (element) => {
	let choosenYear = element.target.value
	document.querySelector("#year-column").textContent = choosenYear

	$("#premium").empty()
	$("#medium").empty()
	$("#luar").empty()

	$("#premium").append("<th>Premium</th>")
	$("#medium").append("<th>Medium</th>")
	$("#luar").append("<th>Luar Kualitas</th>")

	beras[choosenYear].premium.forEach((hargaBeras) => {
		$("#premium").append(`
			<td>${hargaBeras}</td>
		`)
	})

	beras[choosenYear].medium.forEach((hargaBeras) => {
		$("#medium").append(`
			<td>${hargaBeras}</td>
		`)
	})

	beras[choosenYear].luarKualitas.forEach((hargaBeras) => {
		$("#luar").append(`
			<td>${hargaBeras}</td>
		`)
	})
})

document.querySelector("#diagram-year-chooser-input").addEventListener("change", (element) => {
	chart?.destroy()
	let choosenYear = element.target.value
	let ctx = document.getElementById("ricePriceChart").getContext("2d")

	chart = chart = new Chart(ctx, {
		type: "bar",
		data: {
			labels: ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
			datasets: [
				{
					label: "Premium",
					data: beras[choosenYear].premium,
					backgroundColor: "rgba(255, 99, 132, 0.5)",
					borderColor: "rgba(255, 99, 132, 1)",
					borderWidth: 1,
				},
				{
					label: "Medium",
					data: beras[choosenYear].medium,
					backgroundColor: "rgba(54, 162, 235, 0.5)",
					borderColor: "rgba(54, 162, 235, 1)",
					borderWidth: 1,
				},
				{
					label: "Luar kualitas",
					data: beras[choosenYear].luarKualitas,
					backgroundColor: "rgba(75, 192, 192, 0.5)",
					borderColor: "rgba(75, 192, 192, 1)",
					borderWidth: 1,
				},
			],
		},
		options: {
			responsive: true,
			title: {
				display: true,
				text: "Rise in Rice Prices (2023)",
			},
			scales: {
				y: {
					beginAtZero: true,
					title: {
						display: true,
						text: "Price (in Rupiah)",
					},
				},
			},
		},
	})
})

// var ctx = document.getElementById("ricePriceChart").getContext("2d")
// var chart = new Chart(ctx, {
// 	type: "bar",
// 	data: {
// 		labels: ["June", "July", "August", "September", "October", "November", "December"],
// 		datasets: [
// 			{
// 				label: "Premium",
// 				data: [15000, 16000, 16500, 17000, 17500, 18000, 19000],
// 				backgroundColor: "rgba(255, 99, 132, 0.5)",
// 				borderColor: "rgba(255, 99, 132, 1)",
// 				borderWidth: 1,
// 			},
// 			{
// 				label: "Medium",
// 				data: [13000, 14000, 14500, 15000, 15500, 16000, 16500],
// 				backgroundColor: "rgba(54, 162, 235, 0.5)",
// 				borderColor: "rgba(54, 162, 235, 1)",
// 				borderWidth: 1,
// 			},
// 			{
// 				label: "Luar kualitas",
// 				data: [10000, 10500, 11000, 11500, 12000, 12500, 13000],
// 				backgroundColor: "rgba(75, 192, 192, 0.5)",
// 				borderColor: "rgba(75, 192, 192, 1)",
// 				borderWidth: 1,
// 			},
// 		],
// 	},
// 	options: {
// 		responsive: true,
// 		title: {
// 			display: true,
// 			text: "Rise in Rice Prices (2023)",
// 		},
// 		scales: {
// 			y: {
// 				beginAtZero: true,
// 				title: {
// 					display: true,
// 					text: "Price (in Rupiah)",
// 				},
// 			},
// 		},
// 	},
// })
