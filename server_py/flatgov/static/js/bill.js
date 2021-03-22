$(document).ready( function () {
    $('#related-bills-table').DataTable({
        sDom: "Rlfrtip",
        bFilter: true,
        iDisplayLength: 100,
        scrollY: '50vh',
        scrollX: true,
        scrollCollapse: true,
        language: {
            paginate: {
                "previous": "<",
                "next": ">",
            },
            info: "_START_ to _END_ of _TOTAL_ Bills",
            lengthMenu: "_MENU_ bills",
        },
        lengthMenu: [100, 50, 20, 5],
    });
    $('#cosponsors-table').DataTable({
        sDom: "Rlfrtip",
        bFilter: true,
        iDisplayLength: 100,
        scrollY: '50vh',
        scrollX: true,
        scrollCollapse: true,
        language: {
            paginate: {
                "previous": "<",
                "next": ">",
            },
            info: "_START_ to _END_ of _TOTAL_ Cosponsors",
            lengthMenu: "_MENU_ cosponsors",
        },
        lengthMenu: [100, 50, 20, 5],
    });
    $('#similar-bills-table').DataTable({
        sDom: "Rlfrtip",
        // order: [[ 3, 'desc' ]],
        columnDefs: [
            { "width": "10%", "targets": 0 },
            { "width": "10%", "targets": 1 },
            { "width": "10%", "targets": 2 },
            { "width": "30%", "targets": 3 },
            { "width": "10%", "targets": 4 },
            { "width": "10%", "targets": 5 },
        ],
        bSort: false,
        bFilter: true,
        iDisplayLength: 100,
        scrollY: '50vh',
        scrollX: true,
        scrollCollapse: true,
        language: {
            paginate: {
                "previous": "<",
                "next": ">",
            },
            info: "_START_ to _END_ of _TOTAL_ Bills",
            lengthMenu: "_MENU_ bills",
        },
        lengthMenu: [100, 50, 20, 5],
    });
} );