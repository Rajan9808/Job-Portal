
$(document).ready(function() {
	'use strict';


  var progress = document.querySelectorAll('.form-steps');
  var progressUnit = 100 / progress.length;
  var progressWidth = 20;
  var currentStep = 1;

  $('.total-step').html(progress.length);
  $('.current-step').html(currentStep);

  $('.progress-bar').width(progressWidth + '%');

  $('.form-steps .step-btn').on('click', function(e) {
    e.preventDefault();
    $(this).parents('.form-steps').next().addClass('active');
    $(this).parents('.form-steps').removeClass('active');
    progressWidth += progressUnit;

    $('.progress-bar').width(progressWidth + '%');

    currentStep++;
    $('.current-step').html(currentStep);

  })

  $('.form-steps .prev').on('click', function(e) {
    e.preventDefault();
    $(this).parents('.form-steps').prev().addClass('active');
    $(this).parents('.form-steps').removeClass('active');

    progressWidth -= progressUnit;

    $('.progress-bar').width(progressWidth + '%');

    currentStep--;
    $('.current-step').html(currentStep);

  })


})