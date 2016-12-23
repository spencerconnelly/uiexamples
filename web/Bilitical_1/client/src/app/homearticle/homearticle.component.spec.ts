/* tslint:disable:no-unused-variable */
import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { DebugElement } from '@angular/core';

import { HomearticleComponent } from './homearticle.component';

describe('HomearticleComponent', () => {
  let component: HomearticleComponent;
  let fixture: ComponentFixture<HomearticleComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ HomearticleComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(HomearticleComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
