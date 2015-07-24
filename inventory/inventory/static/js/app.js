var inventoryApp = angular.module('inventory', [
  'ngRoute',
  'inventoryControllers',
  'ui.bootstrap',
  'inventoryServices'
]);

inventoryApp.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});

inventoryApp.config(['$routeProvider', '$httpProvider',
  function($routeProvider, $httpProvider) {
    $httpProvider.defaults.headers.common['Accept'] = '*/*';
    $routeProvider.
      when('/base-item-list', {
        templateUrl: '/dashboard/base-item-list',
        controller: 'BaseItemListCtrl'
      }).
      when('/category-list', {
        templateUrl: '/dashboard/category-list',
        controller: 'CategoryListCtrl'
      }).
      when('/item-list', {
        templateUrl: '/dashboard/item-list',
        controller: 'ItemListCtrl'
      }).
      when('/category/:id', {
        templateUrl: function (params) {return '/apiv1/categories/' + params.id;}
      }).
      when('/category/create', {
        templateUrl: '/apiv1/categories/1'
      }).
      otherwise({
        redirectTo: '/base-item-list'
      })
  }
]);

inventoryApp.config(['$httpProvider',
  function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
  }]);
