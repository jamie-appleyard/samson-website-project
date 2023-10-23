$(".nav-item").hover(function() {
    $(this).find('div').animate({ width: '100%',}, 400);
}, function() {
    $(this).find('div').stop().animate({ width: '0%',}, 400);
});

$(".nav-menu-list-item").hover(function () {
    $(this).find('.sideline').animate({ height: '1.6em',}, 200);
}, function() {
    $(this).find('.sideline').animate({ height: '0em',}, 200);
});

$("#solutionsDropdown").click(function() {
    if ($(this).hasClass("guard_col")) {
        $(this).removeClass("guard_col")
    } else {
        $(this).addClass("guard_col")
    }
    $(".solutions-dropdown").slideToggle(300);
});

$("#aboutDropdown").click(function() {
    if ($(this).hasClass("guard_col")) {
        $(this).removeClass("guard_col")
    } else {
        $(this).addClass("guard_col")
    }
    $(".about-dropdown").slideToggle(300);
});

$("#SecurityGuarding").hover(function() {
    $(".nav-menu-image").attr("src", '/static/images/Website_Images/Guarding.png');
    $("#solGuard").attr("src", '/static/images/Widgets/Colour sheilds/Guarding sheild.png');
}, function() {
    $("#solGuard").attr("src", '/static/images/Widgets/White icons without BG/Guarding sheild.png'); 
});

$("#Monitoring").hover(function() {
    $(".nav-menu-image").attr("src", '/static/images/New_Website_Images/Monitoring_2.png');
    $("#solMonitoring").attr("src", '/static/images/Widgets/Colour sheilds/Monitoring sheild.png');
}, function() {
    $("#solMonitoring").attr("src", '/static/images/Widgets/White icons without BG/Monitoring white icon.png');
});

$("#KeyManagement").hover(function() {
    $(".nav-menu-image").attr("src", '/static/images/Website_Images/Frontline.png');
    $("#solKeys").attr("src", '/static/images/Widgets/Colour sheilds/Keyholding sheild.png');
}, function() {
    $("#solKeys").attr("src", '/static/images/Widgets/White icons without BG/Key management white icon.png');
});

$("#Engineering").hover(function() {
    $(".nav-menu-image").attr("src", '/static/images/Website_Images/Engineering.png');
    $("#solEng").attr("src", '/static/images/Widgets/Colour sheilds/Engineering sheild.png');
}, function() {
    $("#solEng").attr("src", '/static/images/Widgets/White icons without BG/Engineering white icon.png');
});

$("#Helpdesk").hover(function() {
    $(".nav-menu-image").attr("src", '/static/images/Website_Images/Helpdesk.png');
    $("#solHelp").attr("src", '/static/images/Widgets/Colour sheilds/Helpdesk sheild.png');
}, function() {
    $("#solHelp").attr("src", '/static/images/Widgets/White icons without BG/Helpdesk white icon.png');
});

$("#ProfessionalServices").hover(function() {
    $(".nav-menu-image").attr("src", '/static/images/Website_Images/Professional.png');
    $("#solProf").attr("src", '/static/images/Widgets/Colour sheilds/Professional sheild.png');
}, function() {
    $("#solProf").attr("src", '/static/images/Widgets/White icons without BG/Professional sheild white icon.png');
});


$("#solutions").click(function() {
    var open = $(".nav-about").css('display');
    if(open == 'block') {
        $(".nav-about").toggle();
        $("#about").removeClass('highlighted-text');
        $("#about").find('div').removeClass('highlighted-underline');
        $(this).addClass('highlighted-text');
        $(this).find('div').addClass('highlighted-underline');
        $(".nav-menu-image").attr("src", '/static/images/Website_Images/Guarding.png');
        $(".nav-solutions").toggle();
    }
    else {
        $(this).addClass('highlighted-text');
        $(this).find('div').addClass('highlighted-underline');
        $(".nav-menu-image").attr("src", '/static/images/Website_Images/Guarding.png');
        $(".nav-solutions").toggle();
        $(".content").toggle()
    }
});

$("#nav-exit").click(function() {
    $(".nav-solutions").toggle();
    $(".content").toggle();
    $("#solutions").removeClass('highlighted-text');
    $("#solutions").find('div').removeClass('highlighted-underline');
});

$("#about").click(function() {
    var open = $(".nav-solutions").css('display');
    if(open == 'block') {
        $(".nav-solutions").toggle();
        $("#solutions").removeClass('highlighted-text');
        $("#solutions").find('div').removeClass('highlighted-underline');
        $(this).addClass('highlighted-text');
        $(this).find('div').addClass('highlighted-underline');
        $(".nav-menu-image").attr("src", '/static/images/New_Website_Images/Lion_Head_Cut.png');
        $(".nav-about").toggle();
    }
    else {
        $(this).addClass('highlighted-text');
        $(this).find('div').addClass('highlighted-underline');
        $(".nav-menu-image").attr("src", '/static/images/New_Website_Images/Lion_Head_Cut.png');
        $(".nav-about").toggle();
        $(".content").toggle();
    }
});

$("#nav-exit2").click(function() {
    $(".nav-about").toggle();
    $(".content").toggle();
    $("#about").removeClass('highlighted-text');
    $("#about").find('div').removeClass('highlighted-underline');
});

$("#WhoWeAre").on({
    mouseover: function() {
        $(".nav-menu-image").attr("src", '/static/images/New_Website_Images/Lion_Head_Cut.png');
    },
});

$("#Quality").mouseover(function() {
    $(".nav-menu-image").attr("src", '/static/images/Website_Images/Car_With_Logo.png');
});

$("#Accreditation").mouseover(function() {
    $(".nav-menu-image").attr("src", '/static/images/Website_Images/Accreditations.png');
});

$("#CSR").mouseover(function() {
    $(".nav-menu-image").attr("src", '/static/images/Website_Images/Rainbow_No_BG.png');
});

$("#qSelect li").click(function() {
    var text = $(this).text();
    $("#q-dropdown").text(text);
});

$("#aSelect li").click(function() {
    var a = $(this).text();
    $("#a-dropdown").text(a);
    var q = $("#q-dropdown").text();
});

var sec_position = 1

$(function (){
    $("#sec-" + sec_position.toString()).toggleClass("about-module-hidden");
})

$("#sel-1").click(function(){
    secSelector(this);
});

$("#sel-2").click(function(){
    secSelector(this);
});

$("#sel-3").click(function(){
    secSelector(this);
});

$("#sel-4").click(function(){
    secSelector(this);
});

$("#selLeft").click(function() {
    if (sec_position == 1) {
        $("#sel-4").trigger("click");
    }
    else {
        var sel_int = (sec_position - 1).toString();
        $("#sel-" + sel_int).trigger("click");
    };
})

$("#selRight").click(function() {
    if (sec_position == 4) {
        $("#sel-1").trigger("click");
    }
    else {
        var sel_int = (sec_position + 1).toString();
        $("#sel-" + sel_int).trigger("click");
    };
})

var secSelector = function(selector) {
    var Number = parseInt(selector.id[4]);
    var newSec = (selector.id[4]);
    if (sec_position == Number) {
        sec_position == Number;
    }
    else {
        var prevSec = sec_position.toString();
        $("#sel-" + prevSec).toggleClass('current');
        $("#sec-" + prevSec).toggleClass("about-module-hidden");
        sec_position = Number;
        $("#sel-" + newSec).toggleClass('current');
        $("#sec-" + newSec).toggleClass('about-module-hidden');
        }
}

$(function() {
    $("#guardingWidget").trigger("click");
});

$(".widget-container").click(function() {
    if ($(this).hasClass("expanded")) {
        console.log('expanded')
    }
    else {
        Reverse($(this));
        Expand($(this));
    }
});

var Expand = function(selector) {
    $(selector).addClass("expanded");
    $(selector).find(".widget-name").toggle();
    $(selector).animate({
        width: "40%",
    }, 500);
    $(selector).find(".widget").animate({
        width: "26%",
    }, 100);
    $(selector).find(".widget-description").toggle();
    $(selector).find(".widget-description").animate({
        opacity: 1,
    })
}

var Reverse = function(selector) {
    var selection = $(selector).siblings().hasClass("expanded");
    if (selection == true) {
        $(".expanded").find(".widget-description").animate({
            opacity: 0,
        });
        $(".expanded").find(".widget-description").toggle();
        $(".expanded").find(".widget").animate({
            width: "100%",
        });
        $(".expanded").animate({
            width: "10%",
        });
        $(".expanded").find(".widget-name").toggle();
        $(".expanded").removeClass("expanded");
    }
    else {
        console.log("n-expanded");
    }  
}



var num_slides = $(".sc-text-slides").children().length
var max_deviation = (num_slides * 100 - 100)
var current_deviation = 0
var image_deviation = 0

$(".btn-next").click(function() {
    if (current_deviation != max_deviation) {
        current_deviation += 100;
        $(".sc-text-slides").animate({
            top: "-" + current_deviation.toString() + "%",
        }, 500);
    }
    else {
        var text_slides = $(".sc-text-slides").html()
        $(".sc-text-slide").attr("id", "old-slide");
        $(".sc-text-slides").append(text_slides)
        current_deviation += 100;
        $(".sc-text-slides").animate({
            top: "-" + current_deviation.toString() + "%",
        }, 500).promise().done(function() {
            for (var i=0; i<num_slides; i++) {
                $(".sc-text-slides").find("#old-slide").remove();
            };
        });
        current_deviation = 0;
        $(".sc-text-slides").animate({
            top: "-" + current_deviation.toString() + "%",
        }, 0);
    }
});

$(".btn-prev").click(function() {
    if (current_deviation != 0) {
        current_deviation -= 100;
        $(".sc-text-slides").animate({
            top: "-" + current_deviation.toString() + "%",
        }, 500);
    }
    else {
        var text_slides = $(".sc-text-slides").html()
        $(".sc-text-slide").attr("id", "old-slide");
        $(".sc-text-slides").prepend(text_slides);
        current_deviation += 100;
        $(".sc-text-slides").animate({
            top: current_deviation.toString() + "%",
        }, 500).promise().done(function() {
            for (var i=0; i<num_slides; i++) {
                $(".sc-text-slides").find("#old-slide").remove();
            };
        });
        current_deviation = max_deviation;
        $(".sc-text-slides").animate({
            top: "-" + current_deviation.toString() + "%",
        }, 0);
    }
})

$(".btn-next").click(function() {
    if (image_deviation != max_deviation) {
        image_deviation += 100;
        $(".sc-image-slides").animate({
            top: "-" + image_deviation.toString() + "%",
        }, 500);
    }
    else {
        var text_slides = $(".sc-image-slides").html()
        $(".sc-image-slide").attr("id", "old-slide");
        $(".sc-image-slides").append(text_slides)
        image_deviation += 100;
        $(".sc-image-slides").animate({
            top: "-" + image_deviation.toString() + "%",
        }, 500).promise().done(function() {
            for (var i=0; i<num_slides; i++) {
                $(".sc-image-slides").find("#old-slide").remove();
            };
        });
        image_deviation = 0;
        $(".sc-image-slides").animate({
            top: "-" + image_deviation.toString() + "%",
        }, 0);
    }
});

$(".btn-prev").click(function() {
    if (image_deviation != 0) {
        image_deviation -= 100;
        $(".sc-image-slides").animate({
            top: "-" + image_deviation.toString() + "%",
        }, 500);
    }
    else {
        var text_slides = $(".sc-image-slides").html()
        $(".sc-image-slide").attr("id", "old-slide");
        $(".sc-image-slides").prepend(text_slides);
        image_deviation += 100;
        $(".sc-image-slides").animate({
            top: image_deviation.toString() + "%",
        }, 500).promise().done(function() {
            for (var i=0; i<num_slides; i++) {
                $(".sc-image-slides").find("#old-slide").remove();
            };
        });
        image_deviation = max_deviation;
        $(".sc-image-slides").animate({
            top: "-" + image_deviation.toString() + "%",
        }, 0);
    }
});

var credsCarousel = function(creds) {
    $(creds).animate({
        left : "-500%"}, 120000, 'linear')
}

var clientCarousel = function(creds) {
    $(creds).animate({
        right : "-500%"}, 120000, 'linear')
}

credsCarousel(".creds-container");
clientCarousel(".client-container");

$(document).ready(function() {
    var solutionEnquiry = $(".enquiry-form")
    var solutionSuccess = $(".success-display")
    var form = $("#enquiryForm")

    var name = $("#id_name")
    var contact_number = $("#id_contact_number")
    var email = $("#id_email")
    var message = $("#id_message")
    var csrf = $("[name='csrfmiddlewaretoken']")
    var url = window.location.pathname

    $("#enquiryForm").submit(function() {
        event.preventDefault();

        var fd = new FormData()
        fd.append('csrfmiddlewaretoken', csrf[0].value)
        fd.append('name', name.val())
        fd.append('contact_number', contact_number.val())
        fd.append('email', email.val())
        fd.append('message', message.val())

        $.ajax({
            type: "post",
            url: url,
            data: fd,
            success: function(response) {
                $("#enquirySubmit").toggle();
                $(".success-display").toggle();
                setTimeout(function() {
                    form.each(function() {
                        this.reset();
                    });
                    $("#enquirySubmit").toggle();
                    $(".success-display").toggle();
                }, 2000),
                console.log(response)
            },
            error: function(error) {
                $(".failed-display").toggle();
            },
            cache: false,
            contentType: false,
            processData: false,
        });
    });
});


$(".news").hover(function() {
    $(this).find(".news-info").animate({top: "0%"}, 500);
}, function() {
    $(this).find(".news-info").stop().animate({top: "75%"}, 250);
});

$(".prev-news-row").on({
    mouseenter: function() {
        $(this).find(".news-info").animate({top: "0%"}, 500);
    },
    mouseleave: function() {
        $(this).find(".news-info").stop().animate({top: "75%"}, 250);
    }
}, ".news-page");

$(".load-more-button").click(function() {
    var current_total = $(".news-page").length
    var data_limit = $(this).attr('data-limit');
    var data_total = $(this).attr('data-total');
    $.ajax({
        url: "/news/load-articles",
        data: {
            limit: data_limit,
            offset: current_total,
        },
        dataType: 'json',
        beforeSend: function(){
            $(".load-more-button").attr('disabled', true);
        },
        success: function(res){
            $(".prev-news-row").append(res.new_articles);
            $(".load-more-button").attr('disabled', false);
            var totalShowing = $(".news-page").length;
            if (totalShowing == data_total) {
                $(".load-more-button").remove();
            }
        },
    })
})

// var aboutNav = $(".about-nav")
// var aboutNavCon = '#whoweare'

// $(".about-nav").click(function() {
//     console.log('triggered')
//     $(aboutNav).removeClass('selected-nav');
//     $(aboutNavCon).toggle();
//     $(this).addClass("selected-nav");
//     var id = "#" + $(this).attr("id").slice(0, -4);
//     $(id).toggle();
//     aboutNav = $(this)
//     aboutNavCon = id
// })

// function aboutTabChange(id) {
//     console.log('triggered')
//     $(aboutNav).removeClass('selected-nav');
//     $(aboutNavCon).toggle();
//     $(this).addClass("selected-nav");
//     $(id).toggle();
//     aboutNav = $(this)
//     aboutNavCon = id
// }

var groupASelected = 0
var groupBSelected = 0
var groupARequired = 2
var groupBRequired = 5
var requiredSets = new Array(5,2,0)
var requiredB = 5

$(".group_a div div .custom-control").on("click", "input", function() {
    if ($(this).hasClass("selected")) {
        $(this).removeClass("selected");
        groupASelected -= 1;
        if (groupASelected >= 3) {
            requiredB = requiredSets[2] 
        }
        else {
            requiredB = requiredSets[groupASelected]
        }
        $("#groupATotal").empty()
        $("#groupATotal").html("0" + groupASelected.toString() + "/0" + groupASelected.toString())
        $("#groupBTotal").empty()
        $("#groupBTotal").html("0" + groupBSelected.toString() + "/0" + requiredB.toString())
        if (groupBSelected >= requiredB) {
            $("#groupBTotal").addClass("completed");
            $("#groupATotal").addClass("completed");
        }
        else {
            $("#groupBTotal").removeClass("completed");
            $("#groupATotal").removeClass("completed");
        }
    }
    else {
        $(this).addClass("selected");
        groupASelected += 1;
        if (groupASelected >= 3) {
            requiredB = requiredSets[2] 
        }
        else {
            requiredB = requiredSets[groupASelected]
        }
        $("#groupATotal").empty()
        $("#groupATotal").html("0" + groupASelected.toString() + "/0" + groupASelected.toString())
        $("#groupBTotal").empty()
        $("#groupBTotal").html("0" + groupBSelected.toString() + "/0" + requiredB.toString())
        if (groupBSelected >= requiredB) {
            $("#groupBTotal").addClass("completed");
            $("#groupATotal").addClass("completed");
        }
        else {
            $("#groupBTotal").removeClass("completed");
            $("#groupATotal").removeClass("completed");
        }
    };
});

$(".group_b div div .custom-control").on("click", "input", function() {
    if ($(this).hasClass("selected")) {
        $(this).removeClass("selected");
        groupBSelected -= 1;
        if (groupBSelected < requiredB) {
            $("#groupATotal").removeClass("completed");
            $("#groupBTotal").removeClass("completed");
        }
        $("#groupBTotal").empty();
        $("#groupBTotal").html("0" + groupBSelected.toString() + "/0" + requiredB.toString());
    }
    else {
        $(this).addClass("selected");
        groupBSelected += 1;
        if (groupBSelected >= requiredB) {
            $("#groupBTotal").addClass("completed");
            $("#groupATotal").addClass("completed");
        }
        $("#groupBTotal").empty();
        $("#groupBTotal").html("0" + groupBSelected.toString() + "/0" + requiredB.toString());
    }
});

$(".sia_badges div .custom-control").on("click", "input", function() {
    if ($(this).hasClass("sia-selected")) {
        $(this).removeClass("sia-selected");
    } else {
        $(this).addClass("sia-selected");
    }
});

$(document).ready(function() {

    var applicationForm = $("#applicationForm")
    var applicationSuccess = $(".application-submitted")

    var csrf = $("[name='csrfmiddlewaretoken']")
    var url = window.location.pathname

    applicationForm.submit(function() {
        event.preventDefault();

        if ($("#groupATotal").hasClass("completed") && $("#groupBTotal").hasClass("completed")) {
            var fd = new FormData()
            $("#applicationForm").find("input").each(function() {
                id = $(this).attr("id")
                if (typeof id === 'undefined') {
                    return true
                }
                if (id == "id_cv") {
                    return true
                }
                if (id =="submit-id-submit") {
                    return true
                }
                if (id.search("group_a") != -1) {
                    return true
                }
                if (id.search("group_b") != -1) {
                    return true
                }
                if (id.search("sia_badges") != -1) {
                    return true
                }
                var name = id.slice(3)
                var value = $("#" + id).val()
                fd.append(name, value)
            });

            $(".sia_badges").find(".sia-selected").each(function() {
                fd.append("sia_badges", $(this).val())
            });

            $(".group_a").find(".selected").each(function() {
                fd.append("group_a", $(this).val())
            });

            $(".group_b").find(".selected").each(function() {
                fd.append("group_b", $(this).val())
            });

            var cv = $("#id_cv")
            fd.append('cv', cv[0].files[0])
            fd.append('csrfmiddlewaretoken', csrf[0].value)

            $.ajax({
                type: "post",
                url: url,
                data: fd,
                success: function(data) {
                    if (!(data['success'])) {
                        console.log("replaced")
                        applicationForm.replaceWith(data['form_html']);
                    }
                    else {
                        applicationSuccess.toggle();
                        setTimeout(function() {
                            applicationForm.trigger("reset");
                        }, 500)
                        applicationForm.slideUp(1000).promise().done(function() {
                            applicationSuccess.slideDown(500)
                        });
                    }
                },
                error: function(error) {
                    $("#application-failed").toggle()
                    applicationForm.find('.error-message').show()  
                },
                cache: false,
                contentType: false,
                processData: false,
            });
        }
        else {
            $(".identity-error").toggle()
        }
    });
});

$(document).ready(function() {
    var TrainingForm = $("#TrainingInterestForm")
    var trainingSubmit = $(".ti-submit-success")

    var csrf = $("[name='csrfmiddlewaretoken']")
    var url = window.location.pathname

    var t_name = $("#id_name")
    var t_email = $("#id_email")
    var t_course = $("#id_course")

    

    TrainingForm.submit(function() {
        event.preventDefault();
        var fd = new FormData()
        fd.append('csrfmiddlewaretoken', csrf[0].value)
        fd.append('name', t_name.val())
        fd.append('email', t_email.val())
        fd.append('course', t_course.val())

        $.ajax({
            type: "post",
            url: url,
            data: fd,
            success: function(response) {
                if (!(response['success'])) {
                    $(".failed-display").toggle();
                }
                else {
                    $(".ti-submit-success").toggle();
                    setTimeout(function() {
                        TrainingForm.trigger("reset")
                    }, 200)
                }
            },
            error: function(error) {
                console.log(error)
            },
            cache: false,
            contentType: false,
            processData: false,
        })
    })
});

$(document).ready(function() {
    var form = $("#EnquiryForm")

    var name = $("#id_name")
    var contact_number = $("#id_contact_number")
    var email = $("#id_email")
    var message = $("#id_message")
    var csrf = $("[name='csrfmiddlewaretoken']")
    var url = window.location.pathname

    $("#enquiryForm").submit(function() {
        event.preventDefault();

        var fd = new FormData()
        fd.append('csrfmiddlewaretoken', csrf[0].value)
        fd.append('name', name.val())
        fd.append('contact_number', contact_number.val())
        fd.append('email', email.val())
        fd.append('message', message.val())

        $.ajax({
            type: "post",
            url: url,
            data: fd,
            success: function(response) {
                $("#enquirySubmit").toggle();
                $(".success-display").toggle();
                setTimeout(function() {
                    form.each(function() {
                        this.reset();
                    });
                    $("#enquirySubmit").toggle();
                    $(".success-display").toggle();
                }, 2000),
                console.log(response)
            },
            error: function(error) {
                $(".failed-display").toggle();
            },
            cache: false,
            contentType: false,
            processData: false,
        });
    });
});

$(".service-logo-link a h3").hover(function() {
    var logo = $(this).attr("attr")
    $("#sl-full").toggle()
    $("#" + logo).toggle()
}, function() {
    var logo = $(this).attr("attr")
    $("#" + logo).toggle()
    $("#sl-full").toggle()
});