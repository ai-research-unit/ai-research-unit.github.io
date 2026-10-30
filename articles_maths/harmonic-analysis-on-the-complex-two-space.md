# __Harmonic Analysis on $\mathbb{C}^2$__

## Introduction

The additive group $\mathbb{C}^2$ is, as a real topological group, the group $\mathbb{R}^4$. Its characters, its Haar measure, its Fourier transform and its convolution are therefore the objects of Euclidean harmonic analysis in four real dimensions, and the whole theory of *Fourier Analysis on Euclidean Spaces* applies without change. What the complex structure adds is a second reading: the group $\mathbb{C}^2$ is also a complex vector space, the rotations by $i$ are a distinguished orthogonal transformation $J$, and the holomorphic exponentials form a complex two-parameter family whose integrals are entire functions. The harmonic analysis of $\mathbb{C}^2$ is the Euclidean theory together with the spectral theory of the Laplacian, the Radon transform, and the spherical harmonics of the sphere $S^3$.

This article treats the group structure and the characters, the Fourier transform and its properties, convolution, the Paley–Wiener theorem, the Radon transform, the spherical harmonics of $S^3$, and the Laplacian. The holomorphic analysis is *Analysis on $\mathbb{C}^2$*; the topology of the space and the sphere is *The Topology of $\mathbb{C}^2$* and *The Unit Sphere and the Hopf Fibration*; the differential forms are *Differential Forms and Stokes' Theorem*; the general Euclidean theory is *Fourier Analysis on Euclidean Spaces*.

**The harmonic analysis of $\mathbb{C}^2$ is the harmonic analysis of $\mathbb{R}^4$ with a complex bookkeeping.** The Fourier transform is the four-dimensional transform; the complex structure enters through the identification of the dual with $\mathbb{C}^2$ by the Hermitian pairing, through the holomorphic characters, and through the decomposition of the spherical harmonics under the unitary group. The Laplacian is the Euclidean Laplacian; the functions whose restriction to every complex line is harmonic are exactly the pluriharmonic functions, a proper subclass of the harmonic ones.

## The Additive Group and Its Characters

**The group $\mathbb{C}^2$ is $\mathbb{R}^4$ with the ordinary addition; its Haar measure is Lebesgue measure, and its characters are the exponentials of the real-linear functionals.**

**Proposition (the group).** The additive group $\mathbb{C}^2$ is a locally compact abelian group isomorphic to $\mathbb{R}^4$. The isomorphism is
$$
Q=(Q_{\blacktriangle},Q_{\blacktriangledown})\longmapsto(q_{\blacktriangle},q'_{\blacktriangle},q_{\blacktriangledown},q'_{\blacktriangledown})\in\mathbb{R}^4,
$$
with $Q_{\blacktriangle}=q_{\blacktriangle}+iq'_{\blacktriangle}$ and $Q_{\blacktriangledown}=q_{\blacktriangledown}+iq'_{\blacktriangledown}$, and the Haar measure is Lebesgue measure $dQ=dq_{\blacktriangle}\,dq'_{\blacktriangle}\,dq_{\blacktriangledown}\,dq'_{\blacktriangledown}$.

*Proof.* The map is an isomorphism of topological groups, and Lebesgue measure is translation invariant and unique up to a positive constant, which is fixed by the identification.

**Definition.** A **character** of $\mathbb{C}^2$ is a continuous homomorphism $\chi:\mathbb{C}^2\to S^1$. Every character is of the form
$$
\chi_\xi(Q)=e^{2\pi i\operatorname{Re}\langle Q,\xi\rangle},\qquad \xi\in\mathbb{C}^2,
$$
where $\langle Q,\xi\rangle=Q_{\blacktriangle}\overline{\xi_{\blacktriangle}}+Q_{\blacktriangledown}\overline{\xi_{\blacktriangledown}}$ is the Hermitian form.

*Proof.* A character of $\mathbb{R}^4$ is $x\mapsto e^{2\pi i x\cdot u}$ for a unique $u\in\mathbb{R}^4$; under the identification, $x\cdot u=\operatorname{Re}\langle Q,\xi\rangle$ for a unique $\xi\in\mathbb{C}^2$, because the map $\xi\mapsto\operatorname{Re}\langle\cdot,\xi\rangle$ is an isomorphism of real vector spaces.

**Proposition (the dual group).** The map $\xi\mapsto\chi_\xi$ is an isomorphism of topological groups from $\mathbb{C}^2$ onto the dual group $\widehat{\mathbb{C}^2}$, and the pairing
$$
\mathbb{C}^2\times\mathbb{C}^2\longrightarrow S^1,\qquad (Q,\xi)\longmapsto e^{2\pi i\operatorname{Re}\langle Q,\xi\rangle},
$$
is a Pontryagin duality pairing.

*Proof.* The characters form a group under pointwise multiplication, and $\chi_\xi\chi_\eta=\chi_{\xi+\eta}$; the map is continuous, bijective and open by the identification with $\mathbb{R}^4$.

**Remark (the two pairings).** The Hermitian pairing $\langle Q,\xi\rangle$ is complex-linear in $Q$ and conjugate-linear in $\xi$; the **bilinear pairing** $Q\cdot\xi=Q_{\blacktriangle}\xi_{\blacktriangle}+Q_{\blacktriangledown}\xi_{\blacktriangledown}$ is complex-linear in both. **The characters are the exponentials of the real part of either pairing**, and the two readings differ by the complex structure: $\operatorname{Re}\langle Q,\xi\rangle=\operatorname{Re}(Q\cdot\bar\xi)$. The holomorphic exponentials of the next sections use the bilinear pairing and are not unitary.

## The Fourier Transform

**The Fourier transform on $\mathbb{C}^2$ is the Fourier transform on $\mathbb{R}^4$ written in complex coordinates; it is an isometry of $L^2$, it exchanges differentiation with multiplication, and it inverts by the same transform with the opposite sign.**

**Definition.** For $f\in L^1(\mathbb{C}^2)$, the **Fourier transform** is
$$
\widehat f(\xi)=\int_{\mathbb{C}^2}f(Q)\,e^{-2\pi i\operatorname{Re}\langle Q,\xi\rangle}\,dQ,\qquad \xi\in\mathbb{C}^2.
$$

**Theorem (inversion and Plancherel).** The Fourier transform extends to a unitary operator
$$
\widehat{\phantom{f}}:L^2(\mathbb{C}^2)\longrightarrow L^2(\mathbb{C}^2)
$$
with inverse
$$
f(Q)=\int_{\mathbb{C}^2}\widehat f(\xi)\,e^{2\pi i\operatorname{Re}\langle Q,\xi\rangle}\,d\xi
$$
for $f$ in the Schwartz class, and
$$
\lVert\widehat f\rVert_2=\lVert f\rVert_2.
$$

*Proof.* These are the inversion theorem and the Plancherel theorem for $\mathbb{R}^4$, transported by the identification of the previous section; they are proved in *Fourier Analysis on Euclidean Spaces*.

**Proposition (the basic properties).** For $f,g\in L^2(\mathbb{C}^2)$ and $Q_0\in\mathbb{C}^2$,
$$
\widehat{f(\cdot-Q_0)}(\xi)=e^{-2\pi i\operatorname{Re}\langle Q_0,\xi\rangle}\widehat f(\xi),\qquad
\widehat{e^{2\pi i\operatorname{Re}\langle Q,Q_0\rangle}f}(\xi)=\widehat f(\xi-Q_0),
$$
$$
\widehat{f(\lambda Q)}(\xi)=\lambda^{-4}\widehat f(\xi/\lambda)\quad(\lambda>0),\qquad
\widehat{\overline{f}}(\xi)=\overline{\widehat f(-\xi)}.
$$
For a Schwartz function $f$ and a multi-index $\alpha$,
$$
\widehat{\partial^\alpha f}(\xi)=(2\pi i)^{\lvert\alpha\rvert}\xi^\alpha\widehat f(\xi),\qquad
\widehat{Q^\alpha f}(\xi)=\left(\frac{i}{2\pi}\right)^{\lvert\alpha\rvert}\partial^\alpha\widehat f(\xi),
$$
where $\partial^\alpha$ is the real partial derivative and $\xi^\alpha$ the corresponding monomial in the real coordinates.

*Proof.* Each identity is a change of variables, an integration by parts, or a differentiation under the integral sign; the constants come from the $2\pi$ normalization.

**Remark (the complex notation).** In the complex coordinates $Q_{\blacktriangle}=q_{\blacktriangle}+iq'_{\blacktriangle}$, $Q_{\blacktriangledown}=q_{\blacktriangledown}+iq'_{\blacktriangledown}$ and $\xi_{\blacktriangle}=u_{\blacktriangle}+iv_{\blacktriangle}$, $\xi_{\blacktriangledown}=u_{\blacktriangledown}+iv_{\blacktriangledown}$, the pairing is
$$
\operatorname{Re}\langle Q,\xi\rangle=q_{\blacktriangle}u_{\blacktriangle}+q'_{\blacktriangle}v_{\blacktriangle}+q_{\blacktriangledown}u_{\blacktriangledown}+q'_{\blacktriangledown}v_{\blacktriangledown},
$$
so the transform is the four-dimensional transform in the variables $(q_{\blacktriangle},q'_{\blacktriangle},q_{\blacktriangledown},q'_{\blacktriangledown})$ and $(u_{\blacktriangle},v_{\blacktriangle},u_{\blacktriangledown},v_{\blacktriangledown})$. **The complex structure does not change the transform; it changes the interpretation of the frequencies.** A frequency $\xi$ parametrizes the real-linear functional $Q\mapsto\operatorname{Re}\langle Q,\xi\rangle$; the holomorphic transform of the next section uses the complex-linear pairing $Q\cdot\xi$ instead.

## Convolution

**Convolution on $\mathbb{C}^2$ is convolution on $\mathbb{R}^4$; it is commutative and associative, it turns the Fourier transform into a pointwise product, and $L^1$ is a Banach algebra under it.**

**Definition.** For $f,g\in L^1(\mathbb{C}^2)$,
$$
(f*g)(Q)=\int_{\mathbb{C}^2}f(Q-Q_1)g(Q_1)\,dQ_1.
$$

**Theorem (Young and the group algebra).** Convolution is commutative and associative, and
$$
\lVert f*g\rVert_1\le\lVert f\rVert_1\lVert g\rVert_1,\qquad
\lVert f*g\rVert_p\le\lVert f\rVert_1\lVert g\rVert_p\quad(1\le p\le\infty).
$$
For $f,g\in L^1$, the transform of the convolution is
$$
\widehat{f*g}=\widehat f\,\widehat g.
$$

*Proof.* The inequalities are Young's inequality for $\mathbb{R}^4$; the product formula is Fubini's theorem and the character property $\chi_\xi(Q-Q_1)=\chi_\xi(Q)\chi_\xi(-Q_1)$.

**Theorem (approximate identities).** Let $\varphi\in L^1$ with $\int\varphi=1$ and set $\varphi_\epsilon(Q)=\epsilon^{-4}\varphi(Q/\epsilon)$. Then for $f\in L^p$, $1\le p<\infty$,
$$
f*\varphi_\epsilon\longrightarrow f\quad\text{in }L^p,
$$
and for $f$ continuous and bounded the convergence is uniform on compact sets.

*Proof.* The proof is the standard approximation argument of *Fourier Analysis on Euclidean Spaces*: the mass of $\varphi_\epsilon$ concentrates at the origin, and the continuity of translations in $L^p$ gives the convergence.

**Remark (the algebra and the transform).** The Fourier transform is an injective homomorphism from the Banach algebra $L^1(\mathbb{C}^2)$ with convolution into the algebra $C_0(\widehat{\mathbb{C}^2})$ with pointwise multiplication; its image is dense in the sup norm but is not closed. **The algebra is not unital**, because a unit would be a function whose transform is identically $1$, and no $L^1$ function has that transform; the approximate identities replace the unit. The same statements hold on $\mathbb{R}^4$, and the complex structure plays no role in this section.

## The Paley–Wiener Theorem

**A function of compact support has a Fourier transform that extends to an entire function of exponential type on the complexified dual, and the type is the radius of the support; the theorem characterizes compact support by the growth of the extension.**

**Theorem (Paley–Wiener for $\mathbb{R}^4$).** Let $R>0$. A function $f\in L^2(\mathbb{R}^4)$ is supported in the closed ball of radius $R$ if and only if its Fourier transform extends to an entire function $F$ on $\mathbb{C}^4$ such that for every $\eta\in\mathbb{R}^4$,
$$
\int_{\mathbb{R}^4}\lvert F(\xi+i\eta)\rvert^2\,d\xi\le C\,e^{4\pi R\lVert\eta\rVert}
$$
for a constant $C$, and
$$
\lvert F(\zeta)\rvert\le C'\,e^{2\pi R\lVert\operatorname{Im}\zeta\rVert}.
$$
The extension is the Fourier–Laplace transform
$$
F(\zeta)=\int_{\mathbb{R}^4}f(x)\,e^{-2\pi i x\cdot\zeta}\,dx.
$$

*Proof.* This is the Paley–Wiener theorem of *Fourier Analysis on Euclidean Spaces*, in the $L^2$ form; the direct part is the analytic continuation of the integral, and the converse is the theorem of Paley and Wiener.

**Theorem (the holomorphic reading on $\mathbb{C}^2$).** Let $f\in L^2(\mathbb{C}^2)$ be supported in the ball $\lVert Q\rVert\le R$. Then the **holomorphic Fourier transform**
$$
\mathcal{F}f(\xi)=\int_{\mathbb{C}^2}f(Q)\,e^{-2\pi i\,Q\cdot\xi}\,dQ,\qquad Q\cdot\xi=Q_{\blacktriangle}\xi_{\blacktriangle}+Q_{\blacktriangledown}\xi_{\blacktriangledown},
$$
is an entire function of $\xi\in\mathbb{C}^2$ of exponential type $R$:
$$
\lvert\mathcal{F}f(\xi)\rvert\le C\,e^{2\pi R\lVert\xi\rVert}.
$$
Conversely, an entire function of exponential type $R$ that satisfies the $L^2$ growth condition of the Paley–Wiener theorem is the holomorphic Fourier transform of a function supported in the ball of radius $R$.

*Proof.* The integral is entire because $f$ is compactly supported and the exponential is entire in $\xi$; the bound is the estimate $\lvert e^{-2\pi i Q\cdot\xi}\rvert\le e^{2\pi R\lVert\xi\rVert}$ on the support. The converse is the Paley–Wiener theorem applied to the real-linear functionals $Q\mapsto\operatorname{Re}(Q\cdot\xi)$, which form a real four-dimensional space of frequencies; the exponential type in the complex norm is the radius of the support.

**Remark (the two transforms).** The transform $\mathcal{F}$ is **not** the restriction of the group Fourier transform $\widehat{\phantom{f}}$ to real $\xi$: the exponential $e^{-2\pi iQ\cdot\xi}$ has modulus $e^{2\pi\operatorname{Im}(Q\cdot\xi)}$, which is not $1$, so it is a holomorphic exponential on the complex group and not a unitary character of the real group. **The group transform is unitary and lives on $\mathbb{R}^4$; the holomorphic transform is entire and lives on $\mathbb{C}^2$**, and the Paley–Wiener theorem is the bridge between the support of $f$ and the growth of the entire function. The holomorphic transform is the one used in several complex variables, where the support condition is replaced by the condition that $f$ be compactly supported in the domain.

## The Radon Transform

**The Radon transform integrates a function over the affine hyperplanes of $\mathbb{R}^4$; the Fourier slice theorem expresses its one-dimensional Fourier transform as the Fourier transform of $f$ along the normal, and it inverts by integrating over the sphere of normals.**

**Definition.** For $\omega\in S^3\subset\mathbb{R}^4$ and $t\in\mathbb{R}$, let
$$
Rf(\omega,t)=\int_{\{x\in\mathbb{R}^4:x\cdot\omega=t\}}f(x)\,d\sigma(x),
$$
where $d\sigma$ is the Lebesgue measure on the hyperplane. The function $Rf$ is defined on $S^3\times\mathbb{R}$.

**Theorem (the Fourier slice theorem).** For $f\in L^1(\mathbb{R}^4)$,
$$
\int_{\mathbb{R}}Rf(\omega,t)\,e^{-2\pi i\lambda t}\,dt=\widehat f(\lambda\omega),\qquad \omega\in S^3,\ \lambda\in\mathbb{R}.
$$

*Proof.* Write the left-hand side as an integral over $\mathbb{R}^4$ with the delta function of $x\cdot\omega-t$, or apply Fubini to the decomposition of $\mathbb{R}^4$ into the hyperplanes orthogonal to $\omega$; the one-dimensional integral of the character over the hyperplane gives the four-dimensional character at $\lambda\omega$.

**Theorem (inversion).** For suitable $f$,
$$
f(x)=\int_{S^3}\int_{\mathbb{R}}\widehat f(\lambda\omega)\,e^{2\pi i\lambda\,x\cdot\omega}\,\lvert\lambda\rvert^{3}\,d\lambda\,d\omega,
$$
and, equivalently, $f$ is recovered from $Rf$ by differentiating $Rf$ three times in $t$ and integrating over $S^3$.

*Proof.* The Fourier inversion formula in polar coordinates $\xi=\lambda\omega$ gives the first display, with $d\xi=\lvert\lambda\rvert^{3}d\lambda\,d\omega$; the Fourier slice theorem replaces $\widehat f(\lambda\omega)$ by the one-dimensional transform of $Rf$, and the differentiation in $t$ produces the factor $\lambda^3$.

**Remark (the complex lines).** The Radon transform of $\mathbb{C}^2$ has a second version: integration over the **complex lines**. An affine complex line is $\{Q_0+\lambda Q_1:\lambda\in\mathbb{C}\}$ for $Q_0,Q_1\in\mathbb{C}^2$ with $Q_1\neq0$, and the space of such lines is $\mathbb{CP}^2$ minus the point $[0:0:1]$, a complex surface: the line is $\alpha Q_{\blacktriangle}+\beta Q_{\blacktriangledown}=\gamma$ with $(\alpha,\beta)\neq(0,0)$, and the triple $[\alpha:\beta:\gamma]$ is its class. **The complex-line transform is the analytical counterpart of the real hyperplane transform**, and its inversion uses a Cauchy–Fantappiè kernel rather than a power of the Laplacian; it is the transform behind the Bochner–Martinelli formula of *The $\bar\partial$-Problem and the Bochner–Martinelli Integral on $\mathbb{C}^2$*.

## Spherical Harmonics

**The spherical harmonics of $S^3$ are the restrictions of the harmonic homogeneous polynomials; they diagonalise the Laplacian of the sphere, and the space of degree $k$ has dimension $(k+1)^2$.**

**Definition.** A **spherical harmonic of degree $k$** on $S^3\subset\mathbb{R}^4$ is the restriction to $S^3$ of a homogeneous polynomial $P$ of degree $k$ in the four real variables that is harmonic, $\Delta P=0$. The space is denoted $\mathcal{H}_k$.

**Theorem (the dimension and the eigenvalue).** The space $\mathcal{H}_k$ has dimension
$$
\dim\mathcal{H}_k=(k+1)^2,
$$
and each $Y\in\mathcal{H}_k$ is an eigenfunction of the Laplace–Beltrami operator $\Delta_{S^3}$ with eigenvalue
$$
-k(k+2).
$$

*Proof.* The harmonic homogeneous polynomials of degree $k$ in $n$ variables have dimension $\binom{n+k-1}{k}-\binom{n+k-3}{k-2}$; for $n=4$ this is $\binom{k+3}{3}-\binom{k+1}{3}=(k+1)^2$. The eigenvalue is the standard one for the sphere $S^{n-1}$, $-k(k+n-2)$, with $n=4$.

**Theorem (the decomposition).** The spaces $\mathcal{H}_k$ are mutually orthogonal in $L^2(S^3)$ and
$$
L^2(S^3)=\bigoplus_{k=0}^{\infty}\mathcal{H}_k
$$
as an orthogonal direct sum; the sum is dense, and the convergence is in $L^2$.

*Proof.* The restrictions of the homogeneous harmonic polynomials are dense in $L^2(S^3)$ by the Weierstrass approximation theorem and the decomposition of polynomials into harmonic pieces; the orthogonality follows from the divergence theorem applied to $P\Delta Q-Q\Delta P$ on the ball.

**Remark (the Hopf fibration and the unitary action).** The group $\mathrm{U}(2)$ acts on $\mathbb{C}^2$ and on $S^3$, and it commutes with the Laplacian; **the spaces $\mathcal{H}_k$ are invariant under $\mathrm{U}(2)$ and decompose into irreducible unitary representations**. The circle $S^1$ of scalar multiplications acts by the Hopf fibration $S^3\to S^2$, and the weight of this action is the difference of the bihomogeneous degrees of the monomials. The monomials $Q^\alpha\overline{Q}^\beta$ with $\lvert\alpha\rvert+\lvert\beta\rvert=k$ span the polynomials of degree $k$, and the harmonic ones are obtained by subtracting the multiples of $\lVert Q\rVert^2$; the bookkeeping is the one of the Hopf fibration of *The Unit Sphere and the Hopf Fibration*.

**Remark (the addition formula and the Funk–Hecke formula).** For each $k$ there is a reproducing kernel $Z_k(x,y)$ on $S^3\times S^3$, the **zonal spherical harmonic**, which depends only on the inner product $x\cdot y$ and satisfies
$$
\int_{S^3}Z_k(x,y)Y(y)\,d\sigma(y)=Y(x),\qquad Y\in\mathcal{H}_k.
$$
**The Funk–Hecke formula** expresses the integral of $Y$ against a function of $x\cdot y$ as a constant multiple of $Y(x)$; the constants are the eigenvalues of the convolution operators on the sphere and are given by Gegenbauer polynomials. The formula is the spherical analogue of the Fourier convolution theorem.

## The Laplacian

**The Laplacian of $\mathbb{C}^2$ is the Euclidean Laplacian of $\mathbb{R}^4$; it is $4\partial\bar\partial$, its fundamental solution is a constant times $\lVert Q\rVert^{-2}$, and its harmonic functions satisfy the mean value property.**

**Definition.** The **Laplacian** on $\mathbb{C}^2$ is
$$
\Delta=\frac{\partial^2}{\partial q_{\blacktriangle}^2}+\frac{\partial^2}{\partial q'^2_{\blacktriangle}}+\frac{\partial^2}{\partial q_{\blacktriangledown}^2}+\frac{\partial^2}{\partial q'^2_{\blacktriangledown}}
=4\left(\frac{\partial^2}{\partial Q_{\blacktriangle}\partial\overline{Q}_{\blacktriangle}}+\frac{\partial^2}{\partial Q_{\blacktriangledown}\partial\overline{Q}_{\blacktriangledown}}\right).
$$

**Proposition (the Fourier multiplier).** For a Schwartz function $f$,
$$
\widehat{\Delta f}(\xi)=-4\pi^2\lVert\xi\rVert^2\widehat f(\xi),
$$
where $\lVert\xi\rVert^2=\lvert\xi_{\blacktriangle}\rvert^2+\lvert\xi_{\blacktriangledown}\rvert^2$. Hence $\Delta$ is self-adjoint on $L^2$ and its spectrum is $(-\infty,0]$.

*Proof.* The Fourier transform of a real second derivative is $(2\pi i)^2$ times the square of the frequency; summing over the four real coordinates gives the display. The symbol is real and nonpositive, so the operator is self-adjoint with the stated spectrum.

**Theorem (the fundamental solution).** The function
$$
E(Q)=\frac{1}{4\pi^2\lVert Q\rVert^2}
$$
satisfies
$$
-\Delta E=\delta_0
$$
in the sense of distributions on $\mathbb{C}^2$.

*Proof.* For $n=4$ the fundamental solution of $-\Delta$ is $\frac{1}{(n-2)\omega_{n-1}}\lVert x\rVert^{2-n}$ with $\omega_3=2\pi^2$; this gives the constant. The distributional computation is the one of *Fourier Analysis on Euclidean Spaces*.

**Theorem (the mean value property).** Let $u$ be harmonic on a domain containing the closed ball $\overline{B}(Q_0,r)$. Then
$$
u(Q_0)=\frac{1}{\omega_3}\int_{S^3}u(Q_0+r\omega)\,d\omega,
$$
and $u$ is $C^\infty$; harmonic functions are real analytic.

*Proof.* The mean value property is the Euclidean one in four dimensions; the regularity follows from the representation $u=u*\varphi_\epsilon$ with a radial approximate identity, or from the fundamental solution.

**Remark (harmonic against pluriharmonic).** Every pluriharmonic function is harmonic, because $\Delta=4(\partial^2/\partial Q_{\blacktriangle}\partial\overline{Q}_{\blacktriangle}+\partial^2/\partial Q_{\blacktriangledown}\partial\overline{Q}_{\blacktriangledown})$ is the trace of the Hermitian matrix of the mixed derivatives; **the converse fails**, and $\lvert Q_{\blacktriangle}\rvert^2-\lvert Q_{\blacktriangledown}\rvert^2$ is harmonic but not pluriharmonic. The two notions are the real and the complex readings of the same operator: harmonic functions are the solutions of $\Delta u=0$, and pluriharmonic functions are the real parts of holomorphic functions. The distinction is developed in *Analysis on $\mathbb{C}^2$*.

**Remark (the Kähler Laplacian).** The Laplacian is the Laplacian associated with the **flat Kähler metric** of $\mathbb{C}^2$: the Kähler form is closed and parallel, and $\Delta$ is $4\partial\bar\partial$ acting on functions. **The harmonic analysis of $\mathbb{C}^2$ is therefore the spectral analysis of the flat Kähler Laplacian**, and the spherical harmonics of $S^3$ are its eigenfunctions on the sphere, with the eigenvalues $-k(k+2)$ of the Laplace–Beltrami operator.

## Summary

The additive group $\mathbb{C}^2$ is $\mathbb{R}^4$; its characters are $\chi_\xi(Q)=e^{2\pi i\operatorname{Re}\langle Q,\xi\rangle}$, its Haar measure is Lebesgue measure, and its Fourier transform is the four-dimensional transform, unitary on $L^2$ and inverting by the opposite character. Convolution is the convolution of $\mathbb{R}^4$; it makes $L^1$ a commutative Banach algebra without unit, and the transform turns it into pointwise multiplication. The Paley–Wiener theorem characterizes compact support by the growth of the Fourier–Laplace extension; in the complex reading, the holomorphic Fourier transform $\mathcal{F}f(\xi)=\int f(Q)e^{-2\pi iQ\cdot\xi}dQ$ is entire of exponential type equal to the radius of the support.

The Radon transform integrates over the affine hyperplanes of $\mathbb{R}^4$; the Fourier slice theorem identifies its one-dimensional transform with the Fourier transform along the normal, and the inversion differentiates three times and integrates over $S^3$. The spherical harmonics of $S^3$ are the restrictions of the harmonic homogeneous polynomials; the space of degree $k$ has dimension $(k+1)^2$ and the eigenvalue $-k(k+2)$, and $L^2(S^3)$ is their orthogonal direct sum. The Laplacian is the Euclidean Laplacian, equal to $4\partial\bar\partial$, with fundamental solution $1/(4\pi^2\lVert Q\rVert^2)$ and with the mean value property; the pluriharmonic functions are the harmonic functions that are real parts of holomorphic functions, and the distinction is the one of *Analysis on $\mathbb{C}^2$*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $Q=(Q_{\blacktriangle},Q_{\blacktriangledown})$, $Q_{\blacktriangle}=q_{\blacktriangle}+iq'_{\blacktriangle}$ | the complex and real coordinates of $\mathbb{C}^2\cong\mathbb{R}^4$ |
| $\chi_\xi(Q)=e^{2\pi i\operatorname{Re}\langle Q,\xi\rangle}$ | the unitary character of frequency $\xi$ |
| $\widehat f(\xi)$ | the Fourier transform on the group |
| $\mathcal{F}f(\xi)$ | the holomorphic Fourier transform, with the bilinear pairing |
| $f*g$ | the convolution |
| $Rf(\omega,t)$ | the Radon transform over the hyperplane $x\cdot\omega=t$ |
| $\mathcal{H}_k$ | the spherical harmonics of degree $k$ on $S^3$ |
| $\Delta_{S^3}$ | the Laplace–Beltrami operator of the sphere |
| $\Delta=4\partial\bar\partial$ | the Euclidean Laplacian of $\mathbb{C}^2$ |
| $E(Q)=1/(4\pi^2\lVert Q\rVert^2)$ | the fundamental solution of $-\Delta$ |

## Further Reading

- [Complex Two-Space](the-complex-two-space.html), for the space, the realification and the Hermitian form.
- [The Realification of $\mathbb{C}^2$](the-realification-of-the-complex-two-space.html), for the identification with $\mathbb{R}^4$ and the complex structure $J$.
- [The Topology of $\mathbb{C}^2$](the-topology-of-the-complex-two-space.html), for the group structure and the sphere $S^3$.
- [The Unit Sphere and the Hopf Fibration](the-unit-sphere-and-the-hopf-fibration.html), for the Hopf fibration and the action of $S^1$ on $S^3$.
- [Analysis on $\mathbb{C}^2$](analysis-on-the-complex-two-space.html), for the harmonic and pluriharmonic functions and the Laplacian.
- [The $\bar\partial$-Problem and the Bochner–Martinelli Integral on $\mathbb{C}^2$](the-dbar-problem-and-the-bochner-martinelli-integral.html), for the complex-line transform and the boundary kernel.
- [Fourier Analysis on Euclidean Spaces](fourier-analysis-on-euclidean-spaces.html), for the Fourier transform, convolution, the Paley–Wiener theorem and the fundamental solution.
- [Differential Forms and Stokes' Theorem](differential-forms-and-stokes-theorem.html), for the calculus of forms and the divergence theorem.
- [Conventions in Mathematics](conventions-in-mathematics.html), for the glyphs and the typographic conventions of the corpus.
