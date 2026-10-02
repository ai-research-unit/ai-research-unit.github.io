
# __The Fourier Operator__

## Introduction

The Fourier transform is not only a formula for a function but an operator, and as an operator it is
unitary. Written
$$
(\mathcal Ff)(\xi)=\int_{\mathbb R^n}f(x)e^{-2\pi ix\cdot\xi}\,dx ,
$$
it extends from the Schwartz class to an isometry of $L^2(\mathbb R^n)$ onto itself, so that it preserves
the inner product and the norm; its inverse is the transform with the conjugate character. The operator
has a second structural feature, its order: applied twice it reflects the argument,
$\mathcal F^2f(x)=f(-x)$, and applied four times it returns $f$, so that $\mathcal F^4=\mathrm{id}$ and its
only possible eigenvalues are the fourth roots of unity. In the Schwartz class that possibility is
realised: the Hermite functions are eigenvectors with eigenvalues $(-i)^k$, and they form an orthonormal
basis of $L^2$ in which $\mathcal F$ is diagonal. This article develops the transform in that
operator-theoretic form: the unitary operator, its order-four structure, the eigenbasis that diagonalises
it, and the unitary equivalence by which it turns differentiation into multiplication and every
translation-invariant operator into a multiplier.

The prerequisites are *Fourier Analysis on Euclidean Spaces* for the transform on $L^1$ and
$\mathcal S(\mathbb R^n)$, the multiplication formula, the inversion theorem, the convolution theorem, the
Plancherel theorem and the Hermite functions, *Measure Theory and Integration* for the $L^2$ space and its
inner product, and *Convolution Operators*, the previous article of this group, for the multiplier
operators. The spectral vocabulary — unitary, self-adjoint, eigenbasis, unitary equivalence, the spectral
theorem — is quoted as it is used from *Banach and Hilbert Spaces*, later in this Part, where it is
developed; the concrete diagonalisation of $\mathcal F$ by the Hermite functions is proved here, and
nothing in the article depends on the general spectral theorem. The adjoint of the Fourier operator is the
subject of *The Adjoint of the Fourier Operator*, in the `* Operator` group of this category, and the
present Article stops at the unitarity from which that adjoint is read. No geometry is invoked; the
transform acts on functions and the operator is studied through the integral and the inner product alone.

## The Transform as an Operator

### Definition on the Schwartz Class

**Definition.** The **Fourier operator** on $\mathbb R^n$ is the map
$$
(\mathcal Ff)(\xi)=\int_{\mathbb R^n}f(x)e^{-2\pi ix\cdot\xi}\,dx ,
$$
under the normalisation of *Fourier Analysis on Euclidean Spaces*; the conjugate transform is
$(\overline{\mathcal F}f)(\xi)=\int f(x)e^{2\pi ix\cdot\xi}dx$, and the inverse transform is
$\check g(x)=\int g(\xi)e^{2\pi ix\cdot\xi}d\xi$.

On the Schwartz class $\mathcal S(\mathbb R^n)$ the transform is a linear homeomorphism onto itself, of
order four; this is the content of the invariance of $\mathcal S$ and of the inversion theorem of the
Fourier article. The two identities this article uses throughout are those of that article as well:
$\mathcal F(\partial_jf)=2\pi i\xi_j\mathcal Ff$ and $\mathcal F(x_jf)=-\frac{1}{2\pi i}\partial_j\mathcal Ff$,
the second from differentiating under the integral.

### Extension to $L^2$ and Unitarity

**Theorem (Plancherel).** The transform extends from $\mathcal S(\mathbb R^n)\cap L^2$ to a unique
bounded linear operator $\mathcal F:L^2(\mathbb R^n)\to L^2(\mathbb R^n)$, which is an isometry:
$$
\lVert\mathcal Ff\rVert_2=\lVert f\rVert_2,\qquad
\langle\mathcal Ff,\mathcal Fg\rangle=\langle f,g\rangle ,
$$
the inner product being $\langle f,g\rangle=\int f\bar g$. It is onto, hence unitary, and its inverse is
the conjugate transform, $\mathcal F^{-1}=\overline{\mathcal F}$.

**Proof.** The isometry on $\mathcal S$ is Plancherel's theorem of *Fourier Analysis on Euclidean
Spaces*; $\mathcal S$ is dense in $L^2$, so the isometry extends uniquely to a bounded isometry of $L^2$,
and the extension is given by the $L^2$ limit of the transforms of an approximating sequence. The inner
product identity is the polarisation of the norm identity over $\mathbb C$ (the article works over
$\mathbb K=\mathbb R$ or $\mathbb C$; over $\mathbb R$ the norm identity is equivalent to the inner product
identity by the polarisation formula). The inverse is the conjugate transform, since the inversion theorem
gives $\check{\hat f}=f$ on $\mathcal S$ and hence, by density and continuity, on $L^2$; surjectivity
follows. $\blacksquare$

The word **unitary** for $\mathcal F$ is used in the sense of *Banach and Hilbert Spaces*, later in this
Part: a bounded operator with $\mathcal F^\dagger\mathcal F=\mathcal F\mathcal F^\dagger=\mathrm{id}$. The
dagger is the adjoint, in the sense of *Conventions in Mathematics*; the star, by contrast, names the
involution of the elements, $\bar f$. The unitarity of $\mathcal F$ is the statement that
$\overline{\mathcal F}=\mathcal F^{-1}$.

## The Order-Four Structure

### The Square of the Transform Is Parity

**Definition.** The **parity operator** $P$ is the reflection $(Pf)(x)=f(-x)$. It is unitary and
self-adjoint, and $P^2=\mathrm{id}$; hence $P$ has the two eigenvalues $+1$ and $-1$, with the even
functions as the $+1$ eigenspace and the odd functions as the $-1$ eigenspace.

**Theorem.** On $L^2(\mathbb R^n)$ one has $\mathcal F^2=P$ and consequently
$\mathcal F^4=\mathrm{id}$, $\mathcal F^{-1}=\mathcal F^3$, and $\mathcal F^3=\mathcal FP=P\mathcal F$.

**Proof.** On $\mathcal S$, inserting the definition and exchanging the order of integration, which the
rapid decrease justifies,
$$
\mathcal F^2f(x)=\int \mathcal Ff(\xi)e^{-2\pi ix\cdot\xi}\,d\xi
=\iint f(y)e^{-2\pi iy\cdot\xi}e^{-2\pi ix\cdot\xi}\,dy\,d\xi
=\int f(y)\Bigl(\int e^{-2\pi i(x+y)\cdot\xi}d\xi\Bigr)dy ,
$$
and the inner integral is the delta distribution at $x+y$, so it selects $y=-x$ and $\mathcal F^2f=f(-x)$.
Both sides extend to $L^2$ by continuity and density. Then $\mathcal F^4=(\mathcal F^2)^2=P^2=\mathrm{id}$,
and $\mathcal F^{-1}=\mathcal F^3$ follows by multiplying by $\mathcal F$; the last identity is
$\mathcal F\mathcal F^2=\mathcal F^2\mathcal F$, that is, parity commutes with $\mathcal F$, which holds
because $\mathcal F^2$ is a function of $\mathcal F$. $\blacksquare$

**Corollary (the eigenvalues).** A unitary operator satisfying $\mathcal F^4=\mathrm{id}$ has spectrum
contained in the fourth roots of unity $\{1,i,-1,-i\}$. In finite dimension it would be diagonalisable
with these eigenvalues; on the infinite-dimensional $L^2$ the same eigenvalues occur, but the operator has
no eigenvectors in $L^2$ beyond the eigenbasis below, and no other spectral values.

**Proof.** If $\mathcal F^4=\mathrm{id}$ and $\lambda$ is an eigenvalue, then $\lambda^4=1$. The spectrum
statement is the spectral mapping theorem for the polynomial $z^4-1$, applied in *Banach and Hilbert
Spaces*, later in this Part. $\blacksquare$

## The Hermite Eigenbasis

### The Hermite Functions

**Definition.** On $\mathbb R$ the **Hermite functions** are obtained from the Gaussian by the operators of
multiplication by $x$ and of differentiation,
$$
h_k(x)=\frac{(-1)^k}{(2^kk!\sqrt\pi)^{1/2}}e^{\pi x^2}\frac{d^k}{dx^k}\bigl(e^{-2\pi x^2}\bigr),
\qquad k=0,1,2,\dots,
$$
and on $\mathbb R^n$ the product functions $h_\alpha(x)=h_{\alpha_1}(x_1)\cdots h_{\alpha_n}(x_n)$, for
multi-indices $\alpha$, are the Hermite functions of several variables. They lie in the Schwartz class and
form an orthonormal basis of $L^2(\mathbb R^n)$.

**Proof.** The orthonormality and completeness are those of the Hermite basis of *Fourier Analysis on
Euclidean Spaces*; the normalising constant is chosen so that $\lVert h_k\rVert_2=1$, and the products are
orthonormal in $L^2(\mathbb R^n)$ by Fubini. $\blacksquare$

### The Eigenvalues

**Theorem.** The Fourier operator is diagonal in the Hermite basis:
$$
\mathcal Fh_\alpha=(-i)^{\lvert\alpha\rvert}h_\alpha ,
\qquad\text{so}\qquad
\mathcal F=\sum_\alpha(-i)^{\lvert\alpha\rvert}\langle\cdot,h_\alpha\rangle h_\alpha .
$$

**Proof.** On $\mathbb R$ the two identities $\mathcal F(\partial_xf)=2\pi i\xi\mathcal Ff$ and
$\mathcal F(xf)=-\frac1{2\pi i}\partial_x\mathcal Ff$ show that $\mathcal F$ commutes with the creation and
annihilation operators $x\pm\frac1{2\pi}\frac{d}{dx}$ which raise and lower $k$, hence that $\mathcal F$
carries $h_k$ to a multiple of $h_k$; the eigenvalue is then fixed on $h_0$ by the Gaussian computation
$\mathcal F(e^{-\pi x^2})=e^{-\pi x^2}$ of the Fourier article, giving eigenvalue $1$ for $k=0$, and the
commutation with the raising operator multiplies the eigenvalue by $-i$ at each step, giving
$\mathcal Fh_k=(-i)^kh_k$. In $n$ variables the eigenvalue of $h_\alpha$ is the product of the one-variable
eigenvalues along the coordinates, $(-i)^{\lvert\alpha\rvert}$. $\blacksquare$

**Corollary (the four eigenspaces).** The eigenvalues $1,i,-1,-i$ correspond to the values
$\lvert\alpha\rvert\equiv0,1,2,3\pmod 4$, so $L^2(\mathbb R^n)$ is the orthogonal direct sum of four
closed subspaces on which $\mathcal F$ acts as the scalars $1,i,-1,-i$; each is infinite-dimensional for
$n\geq1$. This is the diagonalisation of a unitary operator of order four, and the spectral theorem for a
unitary operator is the general statement behind it.

## The Fourier Operator as a Unitary Equivalence

### Differentiation Becomes Multiplication

**Theorem.** With $D_j=\frac1{2\pi i}\partial_j$ acting on the Schwartz class, one has
$$
\mathcal FD_j\mathcal F^{-1}=M_{x_j},\qquad \mathcal FM_{x_j}\mathcal F^{-1}=-D_j ,
$$
where $M_{x_j}$ is multiplication by the coordinate $x_j$; equivalently $\mathcal F$ is a unitary
equivalence carrying the differentiation $\frac1{2\pi i}\partial_j$ into multiplication by the coordinate.

**Proof.** The first identity is the rearrangement of $\mathcal F(\partial_jf)=2\pi i\xi_j\mathcal Ff$, the
second of $\mathcal F(x_jf)=-\frac1{2\pi i}\partial_j\mathcal Ff$; both are the differentiation identities
of *Fourier Analysis on Euclidean Spaces*. On $\mathcal S$ they are identities of operators, and they
extend to the closures. $\blacksquare$

The theorem is the reason the transform solves constant-coefficient equations: a polynomial in the
derivatives becomes multiplication by the same polynomial in the coordinates, so a differential equation
becomes an algebraic one.

### Translation and Convolution Become Multiplication

**Theorem.** For the translation $\tau_y$ and the character $e_y(\xi)=e^{-2\pi iy\cdot\xi}$ one has
$$
\mathcal F\tau_y\mathcal F^{-1}=M_{e_y} ,
$$
and for $k\in L^1(\mathbb R^n)$, with $T_k$ the convolution operator of the previous article,
$$
\mathcal FT_k\mathcal F^{-1}=M_{\hat k},\qquad \mathcal F^{-1}T_m\mathcal F=M_m
$$
for the multiplier operator $T_m$.

**Proof.** $\mathcal F(\tau_yf)=\widehat{f(\cdot-y)}=e_y\mathcal Ff$ is the translation identity of the
Fourier article and gives the first formula; the convolution theorem $\widehat{k*f}=\hat k\hat f$ gives
$T_k=\mathcal F^{-1}M_{\hat k}\mathcal F$, and the multiplier operator is defined by
$T_m=\mathcal F^{-1}M_m\mathcal F$. $\blacksquare$

**Corollary.** Conjugation by $\mathcal F$ is a unitary isomorphism of the algebra of translation-invariant
bounded operators onto the algebra of multiplication operators $M_m$ with $m\in L^\infty$; it carries
composition to pointwise multiplication, adjunction to complex conjugation of the symbol, and compactness
to the vanishing of the symbol. This is the operator form of the Fourier multiplier correspondence of
*Convolution Operators*.

## The Discrete and Finite Models

### The Finite Abelian Group

**Example (the discrete Fourier transform).** Let $G$ be a finite abelian group of order $N$, with the
counting measure normalised to total mass one, and let $\widehat G$ be its character group. The **discrete
Fourier transform** is
$$
(\mathcal Ff)(\chi)=\frac1{\sqrt N}\sum_{g\in G}f(g)\overline{\chi(g)} ,
\qquad f\in\ell^2(G),
$$
and the characters form an orthonormal basis of $\ell^2(G)$, so $\mathcal F$ is a unitary operator. For
$G=\mathbb Z/N\mathbb Z$ it is the matrix with entries $N^{-1/2}\omega^{jk}$, $\omega=e^{-2\pi i/N}$, which
is symmetric, and its square is the reversal of the coordinates, so $\mathcal F^2=P$ and
$\mathcal F^4=\mathrm{id}$ exactly as on $\mathbb R^n$. This is the finite model of the theory: the four
eigenvalues, the order-four structure and the diagonalisation by characters are all visible in an
$N$-dimensional unitary matrix.

The finite abelian group transform and the general character theory are the subject of *Character Theory*
and, in its analytic form, of *Harmonic Analysis on Groups*; the matrix above is recorded here because it
is the exact analogue of the integral operator of the present Article and because its four-eigenvalue
structure is the one the integral transform shares.

### The Group $\mathbb Z$ and the Circle

**Example ($\mathbb Z$ and $\mathbb T$).** On $\ell^2(\mathbb Z)$ the transform to $L^2(\mathbb T)$ is
$(\mathcal Fa)(\theta)=\sum_{n\in\mathbb Z}a_ne^{-2\pi in\theta}$, a unitary isomorphism by Parseval for
Fourier series; its inverse is the coefficient map. The shift of *Convolution Operators* becomes
multiplication by $e^{-2\pi i\theta}$, and a convolution operator becomes multiplication by a function on
the circle. The same dictionary of this article — order four, diagonalisation, equivalence of translation
and multiplication — holds verbatim, with the Hermite basis replaced by the characters.

## Summary

The Fourier operator $\mathcal Ff(\xi)=\int f(x)e^{-2\pi ix\cdot\xi}dx$ extends from the Schwartz class to
a unitary operator of $L^2(\mathbb R^n)$, isometric for the inner product, with inverse the conjugate
transform. It has order four: $\mathcal F^2=P$ is parity and $\mathcal F^4=\mathrm{id}$, so its spectrum
lies in the fourth roots of unity, and it is diagonalised in the Hermite basis by
$\mathcal Fh_\alpha=(-i)^{\lvert\alpha\rvert}h_\alpha$, which splits $L^2$ into four eigenspaces. As a
unitary equivalence it carries differentiation into multiplication by the coordinate and, by the
convolution theorem, carries every translation-invariant operator into its multiplier, so that the
translation-invariance, the multiplier and the four-eigenvalue structure of the transform are three faces
of the same diagonalisation. The finite abelian group $\mathbb Z/N\mathbb Z$ and the pair
$\mathbb Z,\mathbb T$ exhibit the identical structure with characters in place of Hermite functions.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal F$, $\overline{\mathcal F}$ | Fourier operator and its conjugate |
| $\check g$ | Inverse transform, $\check g(x)=\int g(\xi)e^{2\pi ix\cdot\xi}d\xi$ |
| $P$ | Parity, $(Pf)(x)=f(-x)$; $\mathcal F^2=P$ |
| $h_\alpha$ | Hermite functions, orthonormal basis with $\mathcal Fh_\alpha=(-i)^{\lvert\alpha\rvert}h_\alpha$ |
| $D_j$ | $\frac1{2\pi i}\partial_j$; $\mathcal FD_j\mathcal F^{-1}=M_{x_j}$ |
| $M_{x_j}$, $M_m$ | Multiplication operators |
| $\tau_y$, $e_y$ | Translation and character, $\mathcal F\tau_y\mathcal F^{-1}=M_{e_y}$ |
| $T_k$, $T_m$ | Convolution operator and multiplier operator |
| $\omega$ | $e^{-2\pi i/N}$, the primitive $N$-th root of the finite transform |

## Further Reading

- Elias M. Stein and Guido Weiss, *Introduction to Fourier Analysis on Euclidean Spaces* (Princeton
  University Press, 1971), for Plancherel's theorem, the order-four structure and the Hermite functions.
- Gerald B. Folland, *Harmonic Analysis in Phase Space* (Princeton University Press, 1989), for the Fourier
  operator as a metaplectic operator and the Hermite eigenbasis.
- Michael Reed and Barry Simon, *Methods of Modern Mathematical Physics I: Functional Analysis* (Academic
  Press, 1980), for the transform as a unitary operator and the spectral theorem behind its
  diagonalisation.
- Walter Rudin, *Fourier Analysis on Groups* (Interscience, 1962), for the finite and infinite abelian
  transforms and the character theory.
- Elias M. Stein and Rami Shakarchi, *Fourier Analysis: An Introduction* (Princeton University Press,
  2003), for the transform and the eigenfunction structure at the level used here.
- John J. Benedetto and Michael W. Frazier, *Wavelets: Mathematics and Applications* (CRC Press, 1994),
  for the transform as an operator and its unitary discretisations.
