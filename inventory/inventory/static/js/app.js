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
        controller: 'BaseItemListCtrl',
        activetab: 'baseitem'
      }).
      when('/baseitem/:id', {
        templateUrl: function (params) {return '/apiv1/baseitems/' + params.id;},
        controller: 'BaseItemEditCtrl',
        activetab: 'baseitem'
      }).
      when('/create/baseitem', {
        templateUrl: '/apiv1/baseitems/create ',
        controller: 'BaseItemListCtrl',
        activetab: 'baseitem'
      }).
      when('/item-list', {
        templateUrl: '/dashboard/item-list',
        controller: 'ItemListCtrl',
        activetab: 'item'
      }).
      when('/item/:id', {
        templateUrl: function (params) {return '/apiv1/items/' + params.id;},
        controller: 'ItemEditCtrl',
        activetab: 'item'
      }).
      when('/create/item', {
        templateUrl: '/apiv1/items/create',
        controller: 'ItemListCtrl',
        activetab: 'item'
      }).
      when('/brand-list', {
        templateUrl: '/dashboard/brand-list',
        controller: 'BrandListCtrl',
        activetab: 'brand'
      }).
      when('/brand/:id', {
        templateUrl: function (params) {return '/apiv1/brands/' + params.id;},
        controller: 'BrandEditCtrl',
        activetab: 'brand'
      }).
      when('/create/brand', {
        templateUrl: '/apiv1/brands/create ',
        controller: 'BrandListCtrl',
        activetab: 'brand'
      }).
      when('/category-list', {
        templateUrl: '/dashboard/category-list',
        controller: 'CategoryListCtrl',
        activetab: 'category'
      }).
      when('/category/:id', {
        templateUrl: function (params) {return '/apiv1/categories/' + params.id;},
        controller: 'CategoryEditCtrl',
        activetab: 'category'
      }).
      when('/create/category', {
        templateUrl: '/apiv1/categories/create ',
        controller: 'CategoryListCtrl',
        activetab: 'category'
      }).
      when('/transaction-list', {
        templateUrl: '/dashboard/transaction-list',
        controller: 'TransactionListCtrl',
        activetab: 'transaction'
      }).
      when('/transaction/:id', {
        templateUrl: function (params) {return '/apiv1/transactions/' + params.id;},
        controller: 'TransactionEditCtrl',
        activetab: 'transaction'
      }).
      when('/create/transaction', {
        templateUrl: '/apiv1/transactions/create ',
        controller: 'TransactionListCtrl',
        activetab: 'transaction'
      }).
      when('/location-list', {
        templateUrl: '/dashboard/location-list',
        controller: 'LocationListCtrl',
        activetab: 'location'
      }).
      when('/location/:id', {
        templateUrl: function (params) {return '/apiv1/locations/' + params.id;},
        controller: 'LocationEditCtrl',
        activetab: 'location'
      }).
      when('/create/location', {
        templateUrl: '/apiv1/locations/create ',
        controller: 'LocationListCtrl',
        activetab: 'transaction'
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

