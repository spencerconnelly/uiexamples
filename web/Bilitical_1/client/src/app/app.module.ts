import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { RouterModule, Routes } from '@angular/router';
import { AUTH_PROVIDERS } from 'angular2-jwt';


import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { HomeComponent } from './home/home.component';
import { FooterComponent } from './footer/footer.component';
import { DmcapolicyComponent } from './dmcapolicy/dmcapolicy.component';
import { ContactusComponent } from './contactus/contactus.component';
import { ProfileComponent } from './profile/profile.component';
import { ArticleformComponent } from './articleform/articleform.component';
import { TestComponent } from './test/test.component';
import { HomearticleComponent } from './homearticle/homearticle.component';



const appRoutes: Routes = [
  {path: 'profile', component: ProfileComponent},
  {path: '', component: HomeComponent},
  {path: 'home', component: HomeComponent},
  {path: 'dmca', component: DmcapolicyComponent},
  {path: 'contact', component: ContactusComponent},
  {path: 'articleadd',component: ArticleformComponent},
  {path: 'test', component: TestComponent},
];

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    HomeComponent,
    FooterComponent,
    DmcapolicyComponent,
    ContactusComponent,
    ProfileComponent,
    ArticleformComponent,
    TestComponent,
    HomearticleComponent,
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    RouterModule.forRoot(appRoutes)
  ],
  providers: [AUTH_PROVIDERS],
  bootstrap: [AppComponent]
})


export class AppModule { }

