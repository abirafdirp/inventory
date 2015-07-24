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
        templateUrl: function (params) {return '/apiv1/baseitems/' + params.id;},
        controller: 'BaseItemEditCtrl'
      }).
      when('/create/baseitem', {
        templateUrl: '/apiv1/baseitems/create ',
        controller: 'BaseItemListCtrl'
      }).
      when('/item-list', {
        templateUrl: '/dashboard/item-list',
        controller: 'ItemListCtrl'
      }).
      when('/item/:id', {
        templateUrl: function (params) {return '/apiv1/items/' + params.id;},
        controller: 'ItemEditCtrl'
      }).
      when('/create/item', {
        templateUrl: '/apiv1/items/create',
        controller: 'ItemListCtrl'
      }).
      when('/brand-list', {
        templateUrl: '/dashboard/brand-list',
        controller: 'BrandListCtrl'
      }).
      when('/brand/:id', {
        templateUrl: function (params) {return '/apiv1/brands/' + params.id;},
        controller: 'BrandEditCtrl'
      }).
      when('/create/brand', {
        templateUrl: '/apiv1/brands/create ',
        controller: 'BrandListCtrl'
      }).
      when('/category-list', {
        templateUrl: '/dashboard/category-list',
        controller: 'CategoryListCtrl'
      }).
      when('/category/:id', {
        templateUrl: function (params) {return '/apiv1/categories/' + params.id;},
        controller: 'CategoryEditCtrl'
      }).
      when('/create/category', {
        templateUrl: '/apiv1/categories/create ',
        controller: 'CategoryListCtrl'
      }).
      when('/transaction-list', {
        templateUrl: '/dashboard/transaction-list',
        controller: 'TransactionListCtrl'
      }).
      when('/transaction/:id', {
        templateUrl: function (params) {return '/apiv1/transactions/' + params.id;},
        controller: 'TransactionEditCtrl'
      }).
      when('/create/transaction', {
        templateUrl: '/apiv1/transactions/create ',
        controller: 'TransactionListCtrl'
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
