
# __The Fourier Transform and Conjugate Symmetry__

## Introduction

The Fourier transform converts the involution of the functions into a reflection followed by a conjugation.
Precisely,
$$
\widehat{\bar f}(\xi)=\overline{\hat f(-\xi)},
$$
so that conjugating a function conjugates its transform and reflects the frequency; a real function is
therefore characterised by the **conjugate symmetry** of its transform,
$$
f=\bar f\ \Longleftrightarrow\ \hat f(-\xi)=\overline{\hat f(\xi)},
$$
and the even and odd parts of a real function are read off from the real and imaginary parts of its
transform. The same identity underlies the **conjugate Fourier integral**: the conjugate function of a real
function has transform $-i\operatorname{sgn}(\xi)$ times the transform of the function, so that the pairing
of a function with its conjugate is the decomposition of its spectrum into the positive and negative
frequencies, and it is the reason the analytic representation — the function whose spectrum is confined to the
positive frequencies — is built from a function and its Hilbert transform. This article develops the
conjugate symmetry of the transform, the parity decomposition that comes with it, and the algebra
statement that the transform is a star-isomorphism: it carries the involution $f^{*}(x)=\overline{f(-x)}$
of the convolution algebra to the pointwise conjugation of the transforms.

This article is the fourth of the `*` group of *Foundations of Analysis*. Its prerequisites are *Fourier
Analysis on Euclidean Spaces* for the transform, the inversion and Plancherel theorems, the reflection
$\tilde f(x)=f(-x)$ and the identity $\mathcal F^2=\text{reflection}$, the multiplication formula and the
Hilbert transform with symbol $-i\operatorname{sgn}(\xi)$; and *Hermitian Measures and Complex Measures*,
the previous article of this group, for the involution on the measures and its compatibility with the
Fourier–Stieltjes transform. The transform is treated in the $L^1\cap L^2$ setting of the Fourier article,
the Schwartz class and the tempered distributions being *Distributions and Fundamental Solutions*, later in
this Part. The general singular-integral theory of the conjugate function and its maximal operator belongs
to *Real Harmonic Analysis*, in a later Part, and to *Fourier Analysis on Euclidean Spaces*; the conjugate
Poisson integral belongs to harmonic function theory, later in this Part, and is named only. The
Clifford-algebra analogue of the present symmetry is *The Clifford–Fourier Transform and Conjugate
Symmetry*, in the Clifford analysis of a later Part. The convolution operators are the previous group of
this category, and the transform acts on them as multiplication by the symbol. No geometry is invoked.

## The Involution and the Transform

### The Conjugate Symmetry Identity

**Theorem (the transform of the conjugate).** For $f\in L^1(\mathbb R^n)$,
$$
\widehat{\bar f}(\xi)=\overline{\hat f(-\xi)},\qquad \widehat{\bar f}=\widetilde{\overline{\hat f}},
$$
where $\tilde g(x)=g(-x)$ is the reflection; equivalently, in the notation of the Fourier article,
$\mathcal F(\bar f)=\overline{\mathcal F f}\circ(-1)$.

**Proof.** $\widehat{\bar f}(\xi)=\int\overline{f(x)}e^{-2\pi ix\cdot\xi}dx
=\overline{\int f(x)e^{2\pi ix\cdot\xi}dx}=\overline{\hat f(-\xi)}$, by the conjugation of the integral and
the substitution $x\mapsto-x$. $\blacksquare$

The reflection commutes with the transform, $\widehat{\tilde f}=\widetilde{\hat f}$, as recorded in the
Fourier article, where it is also proved that $\mathcal F^2$ is the reflection and $\mathcal F^4=1$; the
conjugate symmetry identity is therefore the statement that conjugation is carried by the transform to
conjugation after the reflection, and, because $\mathcal F^2$ is the reflection,
$$
\mathcal F\circ(\text{conjugation})\circ\mathcal F^{-1}=(\text{conjugation})\circ\mathcal F^2 ,
$$
so that conjugation and the transform fail to commute by exactly the reflection of order two.

### Real Functions and Conjugate-Symmetric Spectra

**Theorem (the conjugate-symmetry criterion).** A function $f\in L^1\cap L^2$ is real up to equality almost
everywhere if and only if its transform obeys the conjugate symmetry
$$
\hat f(-\xi)=\overline{\hat f(\xi)}
$$
for almost every $\xi$; equivalently, the transform is **Hermitian**. More generally, $f$ satisfies the
shifted Hermitian condition $\bar f=\tau_yf$ for a translation $\tau_y$ if and only if $\hat f$ has the
symmetry $\hat f(-\xi)=e^{2\pi iy\cdot\xi}\overline{\hat f(\xi)}$.

**Proof.** Apply the conjugate symmetry identity to $\bar f$: if $f=\bar f$ then
$\hat f(\xi)=\widehat{\bar f}(\xi)=\overline{\hat f(-\xi)}$. Conversely, if $\hat f(-\xi)=\overline{\hat f(\xi)}$
then $\widehat{\bar f}=\hat f$ by the identity, so $\bar f=f$ by the injectivity of the transform. The
translation statement is the same computation with the translation identity
$\widehat{(\tau_{-a}f)}(\xi)=e^{-2\pi ia\cdot\xi}\hat f(\xi)$ of the Fourier article. $\blacksquare$

**Corollary (the parity dictionary for a real function).** Let $f$ be real, and let
$f_{\mathrm e}(x)=\frac12(f(x)+f(-x))$ and $f_{\mathrm o}(x)=\frac12(f(x)-f(-x))$ be its even and odd
parts. Then
$$
\hat f_{\mathrm e}(\xi)=\operatorname{Re}\hat f(\xi),\qquad
\hat f_{\mathrm o}(\xi)=i\operatorname{Im}\hat f(\xi),
$$
so that the even part of a real function has the real part of the spectrum as its transform and the odd part
has $i$ times the imaginary part.

**Proof.** For real $f$, $\hat f(-\xi)=\overline{\hat f(\xi)}$; the even part has transform
$\frac12(\hat f(\xi)+\hat f(-\xi))=\operatorname{Re}\hat f(\xi)$ and the odd part
$\frac12(\hat f(\xi)-\hat f(-\xi))=i\operatorname{Im}\hat f(\xi)$. $\blacksquare$

Thus for a real function the parity of $f$ is read from the reality of $\hat f$ and the sign of the
reflection, and the transform of a real even function is real and even, of a real odd function purely
imaginary and odd. In particular a real even function is determined by the values of its transform on the
positive frequencies alone.

## The Conjugate Fourier Integral

### The Conjugate Function

**Definition.** Let $f$ be a real function in $L^2(\mathbb R)$, extended to the upper half plane by the
Poisson integral. The **conjugate function** (or **harmonic conjugate**) of $f$ is the function
$$
\tilde f(x)=\frac1\pi\,\mathrm{p.v.}\!\int_{\mathbb R}\frac{f(y)}{x-y}\,dy ,
$$
the principal-value integral with the conjugate Poisson kernel; it is the unique real function such that
$f+i\tilde f$ is the boundary value of a function holomorphic in the upper half plane, up to an additive
constant, and it is the value at the boundary of the conjugate Poisson integral
$$
Q_y(x)=\frac1\pi\frac{x}{x^2+y^2},\qquad
\tilde f(x)=\lim_{y\to0}\!\int Q_y(x-t)f(t)\,dt .
$$

**Theorem (the symbol of the conjugate function).** On $L^2(\mathbb R)$ the conjugate function is the
**Hilbert transform** $H$, the bounded operator with the multiplier
$$
\widehat{(Hf)}(\xi)=-i\operatorname{sgn}(\xi)\,\hat f(\xi) ,
$$
and it is skew-adjoint and involutive in the sense $H^2=-\mathrm{id}$; it commutes with the translations and
with the dilations.

**Proof.** The Fourier transform of the principal value of $1/x$ is $-i\pi\operatorname{sgn}(\xi)$ and the
conjugate Poisson kernel multiplies this by $e^{-2\pi y\lvert\xi\rvert}$, so the multiplier at $y=0$ is
$-i\operatorname{sgn}(\xi)$, which is bounded; the skew-adjointness is that of a multiplication by a purely
imaginary odd function, $H^\dagger=-H$, and $H^2$ has multiplier
$(-i\operatorname{sgn})^2=-1$. The commutation with the translations and the dilations is the corresponding
statement for the multiplier, from the convolution and dilation identities of the Fourier article.
$\blacksquare$

The Hilbert transform and its singular-integral theory are *Fourier Analysis on Euclidean Spaces* and
*Real Harmonic Analysis*; the present Article records only its relation to the conjugate symmetry.

### The Analytic Representation

**Definition.** For a real function $f\in L^2(\mathbb R)$ the **analytic representation** (or **Hardy extension**
on the line) is
$$
f_{\mathrm a}=f+iHf .
$$

**Theorem.** The analytic representation has spectrum confined to the positive frequencies,
$$
\widehat{f_{\mathrm a}}(\xi)=\bigl(1+\operatorname{sgn}(\xi)\bigr)\hat f(\xi)
=\begin{cases}2\hat f(\xi),&\xi>0,\\ 0,&\xi<0,\end{cases}
$$
and the real function and its conjugate are recovered from it by $f=\operatorname{Re}f_{\mathrm a}$ and
$Hf=\operatorname{Im}f_{\mathrm a}$; the conjugate symmetry of the spectrum of $f$ is exactly the statement
that the two halves of the spectrum of $f_{\mathrm a}$ are redundant.

**Proof.** The multiplier of $iH$ is $i(-i\operatorname{sgn})=\operatorname{sgn}$, so the multiplier of the
analytic representation is $1+\operatorname{sgn}$, which is $2$ on the positive frequencies and $0$ on the negative
ones; the reconstruction is the definition. $\blacksquare$

This is the analytic form of the conjugate symmetry: a real function is determined by the positive half of its
spectrum, and the conjugate function is the price of discarding the negative half. The systematic use of
this decomposition in the theory of analytic functions is the theory of the Hardy space and the Plemelj
formulae, which belong to the complex analysis of a later Part.

## The Transform as a Star-Isomorphism

### The Two Involutions

**Definition.** On the functions on a group two involutions are in play: the **value-conjugation**
$\bar f(x)=\overline{f(x)}$, and the **convolution involution**
$$
f^{*}(x)=\overline{f(-x)},
$$
which combines the conjugation with the reflection and is the adjoint of convolution; the distinction is the
one recorded in *Hermitian Measures and Complex Measures*, the previous article of this group, between the
value-conjugation $\bar\mu$ and the adjoint involution $\mu^{*}$ of the group measure algebra.

**Theorem (the transform turns the conjugation into the value-conjugation).** In the setting of the convolution
algebra of a group,
$$
\widehat{f^{*}}(\xi)=\overline{\hat f(\xi)},
$$
so that the Fourier transform is a star-isomorphism: it carries the convolution involution $f\mapsto f^{*}$
of the algebra of functions to the pointwise conjugation of the transforms, and the product to the product.
For a finite abelian group the transform is an isomorphism of the group algebra with its star onto the
algebra of functions on the dual group with pointwise product and pointwise conjugation; for
$\mathbb Z$ and $\mathbb R$ it is a star-homomorphism of $\ell^1$ or $L^1$ into the bounded continuous
functions, with dense image, whose extension is the Gelfand transform of the algebra.

**Proof.** $\widehat{f^{*}}(\xi)=\int\overline{f(-x)}e^{-2\pi ix\cdot\xi}dx
=\overline{\int f(-x)e^{2\pi ix\cdot\xi}dx}=\overline{\int f(u)e^{-2\pi iu\cdot\xi}du}=\overline{\hat f(\xi)}$,
which is the statement; the product statement is the convolution theorem of the Fourier article, and the
isomorphism statements are the Fourier inversion and Plancherel theorems. $\blacksquare$

**Corollary (the algebraic reading of the conjugate symmetry).** The value-conjugation identity
$\widehat{\bar f}=\widetilde{\overline{\hat f}}$ and the involution identity
$\widehat{f^{*}}=\overline{\hat f}$ differ by the reflection: $\bar f=f^{*}\circ(\text{reflection})$, and
the transform commutes with the reflection. The conjugate symmetry of the previous sections is therefore the
shadow, at the level of the involution of the algebra, of the elementary identity
$\mathcal F^2=\text{reflection}$.

## Summary

The Fourier transform carries complex conjugation to conjugation followed by reflection,
$\widehat{\bar f}(\xi)=\overline{\hat f(-\xi)}$, so that a function is real exactly when its transform obeys
the conjugate symmetry $\hat f(-\xi)=\overline{\hat f(\xi)}$; for a real function the even part has the real
part of the spectrum as its transform and the odd part $i$ times the imaginary part, and a real even function
has a real even transform. The conjugate function of a real function on the line is the Hilbert transform,
with multiplier $-i\operatorname{sgn}(\xi)$, skew-adjoint and involutive with square $-\mathrm{id}$; the
analytic representation $f+iHf$ has spectrum confined to the positive frequencies, which is the sharpest form of the
redundancy of the conjugate-symmetric spectrum, and its analytic theory is that of the Hardy space and the
Plemelj formulae. On the convolution algebra the Fourier transform is a star-isomorphism carrying the
involution $f^{*}(x)=\overline{f(-x)}$ to the pointwise conjugation of the transforms, so that the conjugate
symmetry of the spectrum and the involution of the algebra are the reflection of order two of the transform
and the inversion theorems read in two ways.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\bar f$, $\bar\mu$ | Value-conjugation $f(x)\mapsto\overline{f(x)}$ and $\mu(A)\mapsto\overline{\mu(A)}$ |
| $\tilde f(x)=f(-x)$ | Reflection, $\mathcal F^2=\text{reflection}$, $\mathcal F^4=1$ |
| $\widehat{\bar f}(\xi)=\overline{\hat f(-\xi)}$ | Conjugate symmetry of the transform |
| $f_{\mathrm e},f_{\mathrm o}$ | Even and odd parts, $\frac12(f(x)\pm f(-x))$ |
| $\tilde f$, $H$ | Conjugate function, Hilbert transform, multiplier $-i\operatorname{sgn}$ |
| $Q_y$ | Conjugate Poisson kernel $\frac1\pi\frac{x}{x^2+y^2}$ |
| $f_{\mathrm a}=f+iHf$ | Analytic representation, spectrum on the positive frequencies |
| $f^{*}(x)=\overline{f(-x)}$ | Convolution involution, $\widehat{f^{*}}=\overline{\hat f}$ |

## Further Reading

- Elias M. Stein and Guido Weiss, *Introduction to Fourier Analysis on Euclidean Spaces* (Princeton
  University Press, 1971), for the transform, the conjugate function and the Hilbert transform.
- Elias M. Stein and Rami Shakarchi, *Fourier Analysis: An Introduction* (Princeton University Press, 2003),
  for the conjugate symmetry, the analytic representation and the Hardy space on the line.
- Frederick W. King, *Hilbert Transforms* (2 vols., Cambridge University Press, 2009), for the conjugate
  function, the conjugate Poisson kernel and the applications.
- Walter Rudin, *Fourier Analysis on Groups* (Interscience, 1962), for the transform as a star-isomorphism
  of the convolution algebra.
- Lynn H. Loomis, *An Introduction to Abstract Harmonic Analysis* (Van Nostrand, 1953; reprinted Dover,
  2011), for the Gelfand transform of the group algebra.
- Christian Berg, Jens Peter Reus Christensen and Paul Ressel, *Harmonic Analysis on Semigroups* (Springer,
  1984), for the interaction of the involution and the transform on semigroups.
