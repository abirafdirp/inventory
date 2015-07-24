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
      when('/baseitem-list', {
        templateUrl: '/dashboard/base-item-list',
        controller: 'BaseItemListCtrl'
      }).
      when('/baseitem/:id', {
        templateUrl: function (params) {return '/apiv1/baseitems/' + params.id;}
      }).
      when('/create/baseitem', {
        templateUrl: '/apiv1/baseitems/create '
      }).
      when('/item-list', {
        templateUrl: '/dashboard/item-list',
        controller: 'ItemListCtrl'
      }).
      when('/brand-list', {
        templateUrl: '/dashboard/brand-list',
        controller: 'BrandListCtrl'
      }).
      when('/brand/:id', {
        templateUrl: function (params) {return '/apiv1/brands/' + params.id;}
      }).
      when('/create/brand', {
        templateUrl: '/apiv1/brands/create '
      }).
      when('/category-list', {
        templateUrl: '/dashboard/category-list',
        controller: 'CategoryListCtrl'
      }).
      when('/category/:id', {
        templateUrl: function (params) {return '/apiv1/categories/' + params.id;}
      }).
      when('/create/category', {
        templateUrl: '/apiv1/categories/create '
      }).
      otherwise({
        redirectTo: '/baseitem-list'
      })
  }
]);

inventoryApp.config(['$httpProvider',
  function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
  }]);
