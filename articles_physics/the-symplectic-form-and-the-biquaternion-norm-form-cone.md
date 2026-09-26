# __The Symplectic Form and the Biquaternion Norm-Form Cone__

## Introduction

Hamiltonian mechanics is symplectic geometry. The phase space carries a closed, non-degenerate two-form $\omega$, the Hamiltonian vector field of a function $f$ is defined by $\iota_{X_f}\omega=df$, and the Poisson bracket is $\{f,g\}=\omega(X_f,X_g)$. When the phase space is linear and the form is constant, the same data can be presented as a triple: a positive-definite metric $g$, an antisymmetric form $\omega$, and a complex structure $J$ compatible with both, with $g(Ju,Jv)=g(u,v)$ and $\omega(u,v)=g(Ju,v)$. This is the **Kähler** presentation, and it is the one the biquaternion algebra reproduces.

The biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ carries two canonical quadratic structures: the **Hermitian form** $\tilde Z^\dagger\tilde W$ with its scalar part $\mathrm{Sc}(\tilde Z^\dagger\tilde W)$, and the **holomorphic norm form** $N(\tilde Z)=\tilde Z\bar{\tilde Z}=\sum_\mu Z_\mu^2$. The first is positive definite; the second is a complex bilinear form whose vanishing set is a complex cone — the **norm-form cone**. The thesis of this article is that these two structures are the two faces of one object:

1. The Hermitian pairing, read on the phase-space biquaternion $\tilde Z=\tilde q+i\tilde p$, has a real part that is the Euclidean metric $g$ and an imaginary part that is the symplectic form $\omega$. The algebra's complex structure $i$ is the Kähler $J$.
2. The holomorphic norm form is the symmetric complex bilinear form of the same complex structure; its isotropic cone is the norm-form cone. On the material sector that cone is the light cone, and it is the characteristic cone of the d'Alembertian.
3. On the coadjoint orbit of the companion articles, the symplectic form is the Souriau form and the orbit is a level set of the norm form; the cone is the degenerate orbit at zero level.

The article is classical throughout. The Hermitian pairing is the trace pairing that the companion articles on $\mathbb{M}_+$ write as the Born pairing; here it is read as a phase-space metric and a symplectic form, and no measurement postulate is involved. No commutator appears.

The conventions are those of the read list. The algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$, $e_k^2=-e_0$, $e_je_k=-\delta_{jk}e_0+\varepsilon_{jkl}e_l$; $i$ is central with $i^2=-1$; conjugations are $\bar{\cdot}$ (quaternion), ${}^*$ (complex), and ${}^\dagger=\bar{\cdot}^{\,*}$ (Hermitian); $\mathbb{M}_-$ and $\mathbb{M}_+$ are the anti-Hermitian and Hermitian sectors. The phase-space biquaternion is $\tilde Z=\tilde q+i\tilde p$ with $\tilde q,\tilde p$ pure real quaternions, identified with a point of the six-dimensional real phase space; the norm form is $N(\tilde Q)=\tilde Q\bar{\tilde Q}$. The $ict$ metric is $\eta=\mathrm{diag}(-1,+1,+1,+1)$, and the d'Alembertian of the series is $\Box=\tilde\nabla\bar{\tilde\nabla}=\partial_{ict}^2+\Delta$.

The companion articles are:
- Companion article *Lagrangian and Hamiltonian Mechanics in Biquaternionic Form*, for the phase-space biquaternion and the Poisson bracket.
- Companion article *The Action Principle and the Classical Limit as Stationary Phase in Biquaternionic Form*, for the symplectic potential as the boundary term of the action.
- Companion article *Similitudes Between Biquaternion Rotors and Hamiltonian Flow*, for the coadjoint orbit and the Souriau form.
- Companion article *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*, for the norm form, the four-vector, and the light cone.

## The Standard Symplectic Structure

A **symplectic vector space** is a real vector space $V$ with a bilinear form $\omega$ that is antisymmetric, $\omega(u,v)=-\omega(v,u)$, and non-degenerate, $\omega(u,v)=0$ for all $v$ implies $u=0$. In canonical coordinates $(\mathbf q,\mathbf p)$ on $V=\mathbb{R}^{2n}$ the standard form is

$$
\omega=\sum_{k=1}^{n}dq_k\wedge dp_k ,
$$

so that $\omega(u,v)=\sum_k(q_k^u p_k^v-p_k^u q_k^v)$ on component vectors. The **Hamiltonian vector field** of a function $f$ is defined by

$$
\iota_{X_f}\,\omega=df,\qquad\text{that is}\qquad X_f=\sum_k\left(\frac{\partial f}{\partial p_k}\frac{\partial}{\partial q_k}-\frac{\partial f}{\partial q_k}\frac{\partial}{\partial p_k}\right),
$$

and the **Poisson bracket** is

$$
\{f,g\}=\omega(X_f,X_g)=\sum_k\left(\frac{\partial f}{\partial q_k}\frac{\partial g}{\partial p_k}-\frac{\partial f}{\partial p_k}\frac{\partial g}{\partial q_k}\right).
$$

The form $\omega$ is closed ($d\omega=0$, trivially for a constant form), and **Darboux's theorem** states that any symplectic form can be brought to the constant form above by a change of coordinates, so there are no local invariants beyond the dimension.

A **Kähler structure** on $(V,\omega)$ is a pair $(g,J)$ with $g$ a positive-definite symmetric bilinear form and $J$ a complex structure, $J^2=-\mathrm{id}$, such that

$$
g(Ju,Jv)=g(u,v),\qquad \omega(u,v)=g(Ju,v).
$$

In that case $\omega(Ju,Jv)=\omega(u,v)$, and $(g,\omega,J)$ is called a compatible triple. The standard example on $\mathbb{R}^{2n}$ is the Euclidean metric $g(u,v)=\sum_k(q_k^uq_k^v+p_k^up_k^v)$ with the block matrix $J$ sending $q_k\mapsto p_k$, $p_k\mapsto -q_k$. The biquaternion algebra realizes exactly this triple with $J$ equal to its own complex structure $i$.

## The Hermitian Pairing of the Phase-Space Biquaternion

### The Identity

Let $\tilde q,\tilde p$ be pure real quaternions and form

$$
\tilde Z=\tilde q+i\tilde p\in\mathbb{B}.
$$

The Hermitian conjugate of $\tilde Z$ is

$$
\tilde Z^\dagger=-\tilde q+i\tilde p ,
$$

since $\tilde q^\dagger=-\tilde q$ and $(i\tilde p)^\dagger=i\tilde p$ for pure real $\tilde q,\tilde p$. For a second phase-space biquaternion $\tilde W=\tilde r+i\tilde s$, a direct computation of the scalar part gives the central identity of the article,

$$
\boxed{\;\mathrm{Sc}\!\left(\tilde Z^\dagger\tilde W\right)
=\bigl(\mathbf q\cdot\mathbf r+\mathbf p\cdot\mathbf s\bigr)
+i\bigl(\mathbf q\cdot\mathbf s-\mathbf p\cdot\mathbf r\bigr).\;}
$$

The real part is the Euclidean pairing of the two phase-space points, and the imaginary part is an antisymmetric pairing. Both statements follow from $\mathrm{Sc}(\tilde a\tilde b)=-\mathbf a\cdot\mathbf b$ for pure real quaternions, applied term by term.

### The Metric and the Symplectic Form

Define the two real bilinear forms

$$
g(\tilde Z,\tilde W)=\mathrm{Re}\,\mathrm{Sc}\!\left(\tilde Z^\dagger\tilde W\right)=\mathbf q\cdot\mathbf r+\mathbf p\cdot\mathbf s,
$$

$$
\omega(\tilde Z,\tilde W)=\mathrm{Im}\,\mathrm{Sc}\!\left(\tilde Z^\dagger\tilde W\right)=\mathbf q\cdot\mathbf s-\mathbf p\cdot\mathbf r .
$$

The form $g$ is symmetric and positive definite: $g(\tilde Z,\tilde Z)=|\mathbf q|^2+|\mathbf p|^2$, the Euclidean norm of the phase-space point, vanishing only at the origin. The form $\omega$ is antisymmetric, because exchanging $\tilde Z$ and $\tilde W$ exchanges $\mathbf q\cdot\mathbf s$ with $\mathbf r\cdot\mathbf p=\mathbf p\cdot\mathbf r$ and reverses the sign; and it is non-degenerate, since $\omega(\tilde Z,\tilde W)=0$ for all $\tilde W$ forces $\mathbf q=\mathbf p=0$. As a two-form in coordinates,

$$
\omega=\sum_{k=1}^{3}dq_k\wedge dp_k ,
$$

which is the standard symplectic form. The identity above is therefore the statement that **the symplectic form is the imaginary part of the Hermitian scalar pairing, and the Euclidean metric is its real part.**

### The Complex Structure

The algebra's scalar imaginary $i$ acts on $\tilde Z$ by

$$
i\tilde Z=-\tilde p+i\tilde q ,
$$

exchanging the configuration and the momentum (with a sign). Using the two forms, one checks

$$
g(i\tilde Z,\tilde W)=\omega(\tilde Z,\tilde W),\qquad
g(i\tilde Z,i\tilde W)=g(\tilde Z,\tilde W),\qquad
\omega(i\tilde Z,i\tilde W)=\omega(\tilde Z,\tilde W).
$$

The first is the compatibility relation $\omega(\tilde Z,\tilde W)=g(J\tilde Z,\tilde W)$ with $J=i$; the second says that $i$ is an isometry of $g$; the third follows from the other two. Hence

$$
\boxed{\;\text{the algebra's complex structure } i \text{ is the Kähler } J\;}
$$

and $(g,\omega,i)$ is a compatible Kähler triple on the real phase-space module. The complex structure that the algebra carries intrinsically is the same object that the standard theory introduces by hand on $\mathbb{R}^{2n}$.

## The Symplectic Potential and the Biquaternion Two-Form

### The Potential

The **symplectic potential** is the one-form whose exterior derivative is $\omega$. From the identity above, the natural biquaternion expression is the imaginary part of $\mathrm{Sc}(\tilde Z^\dagger d\tilde Z)$:

$$
\mathrm{Sc}\!\left(\tilde Z^\dagger d\tilde Z\right)
=\tfrac{1}{2}\,d\,g(\tilde Z,\tilde Z)+i\left(\mathbf q\cdot d\mathbf p-\mathbf p\cdot d\mathbf q\right).
$$

Taking the imaginary part and defining

$$
\theta=\tfrac{1}{2}\,\mathrm{Im}\,\mathrm{Sc}\!\left(\tilde Z^\dagger d\tilde Z\right)
=\tfrac{1}{2}\left(\mathbf q\cdot d\mathbf p-\mathbf p\cdot d\mathbf q\right),
$$

one finds

$$
d\theta=\tfrac{1}{2}\left(d\mathbf q\wedge d\mathbf p-d\mathbf p\wedge d\mathbf q\right)
=d\mathbf q\wedge d\mathbf p=\omega .
$$

The boundary term of the action of the preceding article, $\theta_{\mathrm{bdry}}=\mathrm{Sc}(\bar{\tilde p}\,d\tilde q)=\mathbf p\cdot d\mathbf q$, is the canonical potential in the same sense but with the opposite sign: $d\theta_{\mathrm{bdry}}=d\mathbf p\wedge d\mathbf q=-\omega$, so it is $-\theta_{\mathrm{bdry}}$, not $\theta_{\mathrm{bdry}}$, that is a potential for the same $\omega$ as $\theta$. Comparing the two potentials for $\omega$,

$$
\theta-\left(-\theta_{\mathrm{bdry}}\right)
=\tfrac{1}{2}\left(\mathbf q\cdot d\mathbf p-\mathbf p\cdot d\mathbf q\right)+\mathbf p\cdot d\mathbf q
=\tfrac{1}{2}\,d(\mathbf q\cdot\mathbf p),
$$

so they differ by the exact form $\tfrac12 d(\mathbf q\cdot\mathbf p)$, and the symplectic form is unchanged. This is the biquaternion form of the standard freedom in the symplectic potential, together with the standard sign that relates $p\,dq$ to $dq\wedge dp$; the sign is fixed once and for all here, so that the $\omega$ used below is the one whose brackets are the canonical ones of the preceding articles.

### The Two-Form Identity

The symplectic form can also be written as the scalar part of a biquaternion two-form. Computing

$$
\mathrm{Sc}\!\left(d\tilde Z\wedge d\tilde Z^\dagger\right),
\qquad d\tilde Z=\sum_k(dq_k+i\,dp_k)\,e_k,\qquad
d\tilde Z^\dagger=-\sum_k(dq_k-i\,dp_k)\,e_k ,
$$

and using the antisymmetry of the wedge together with the anticommutativity of the quaternion units, the only terms that survive are the scalar ones, and they give

$$
\boxed{\;\mathrm{Sc}\!\left(d\tilde Z\wedge d\tilde Z^\dagger\right)=-2i\,\omega\;}
\qquad\text{equivalently}\qquad
\omega=\frac{i}{2}\,\mathrm{Sc}\!\left(d\tilde Z\wedge d\tilde Z^\dagger\right).
$$

The computation is one line in the one-degree-of-freedom case, where $\tilde Z=(q+ip)e_1$ and

$$
d\tilde Z\wedge d\tilde Z^\dagger
=(dq+i\,dp)\wedge(-dq+i\,dp)\,e_1^2
=\bigl(2i\,dq\wedge dp\bigr)(-e_0)
=-2i\,dq\wedge dp\,e_0 ,
$$

and the general case follows from the same cancellation of the non-scalar terms. A companion identity is worth recording: the wedge of $\,d\tilde Z$ with itself vanishes,

$$
d\tilde Z\wedge d\tilde Z=0 ,
$$

because the quaternion units anticommute while the wedge is antisymmetric, so the terms with distinct indices cancel pairwise and the terms with equal indices vanish. The one-form $d\tilde Z$ is **isotropic** for the wedge product; it is the biquaternion form of the statement that a complex coordinate differential is closed under the wedge.

### The Poisson Bracket from the Pairing

The same Hermitian pairing that gives $g$ and $\omega$ gives the Poisson bracket directly. For a real function $f(\tilde q,\tilde p)$ define the **phase-space biquaternion gradient**

$$
\nabla f=\sum_{\mu=0}^{3}e_\mu\left(\frac{\partial f}{\partial q_\mu}+i\frac{\partial f}{\partial p_\mu}\right).
$$

Then

$$
\mathrm{Sc}\!\left((\nabla f)^\dagger\,\nabla g\right)
=\sum_\mu\left(\frac{\partial f}{\partial q_\mu}\frac{\partial g}{\partial q_\mu}
+\frac{\partial f}{\partial p_\mu}\frac{\partial g}{\partial p_\mu}\right)
+i\sum_\mu\left(\frac{\partial f}{\partial q_\mu}\frac{\partial g}{\partial p_\mu}
-\frac{\partial f}{\partial p_\mu}\frac{\partial g}{\partial q_\mu}\right),
$$

whose imaginary part is the Poisson bracket:

$$
\boxed{\;\{f,g\}=\mathrm{Im}\,\mathrm{Sc}\!\left((\nabla f)^\dagger\,\nabla g\right).\;}
$$

The conjugate here must be the **Hermitian** one, $(\nabla f)^\dagger=\overline{(\nabla f)}^*$, and not the quaternion conjugate alone: the gradient is a complex biquaternion, and conjugating only its quaternion structure would flip the relative sign between the two terms of the real part and symmetrise the imaginary part. With the Hermitian conjugate the real part is the positive-definite metric pairing of the two gradients and the imaginary part is the antisymmetric symplectic pairing. The bracket is thus the imaginary part of the same Hermitian pairing, evaluated on gradients, and the identity displays the Kähler structure in the bracket itself: the metric and the bracket are two projections of one complex pairing. This is verified directly on the canonical functions, where $\nabla q_\mu=e_\mu$ and $\nabla p_\mu=ie_\mu$, giving $\{q_\mu,p_\nu\}=\delta_{\mu\nu}$.

## The Norm Form and Its Cone

### The Holomorphic Form

The Hermitian form of the previous section is one of two canonical quadratic structures. The other is the **norm form**

$$
N(\tilde Z)=\tilde Z\bar{\tilde Z}=\sum_{\mu=0}^{3}Z_\mu^2 ,
$$

where $Z_\mu$ are the $\mathbb{C}$-coefficients in the basis $e_\mu$. For the phase-space biquaternion with pure-vector components this is

$$
N(\tilde Z)=Z_1^2+Z_2^2+Z_3^2 .
$$

Unlike the Hermitian form, $N$ is **holomorphic**: it is a complex bilinear form, $N(\alpha\tilde Z)=\alpha^2N(\tilde Z)$ for complex $\alpha$, and its polarization is the symmetric bilinear form

$$
B(\tilde Z,\tilde W)=\mathrm{Sc}\!\left(\tilde Z\bar{\tilde W}\right)
=\bigl(\mathbf q\cdot\mathbf r-\mathbf p\cdot\mathbf s\bigr)
+i\bigl(\mathbf q\cdot\mathbf s+\mathbf p\cdot\mathbf r\bigr),
$$

which is symmetric, $B(\tilde Z,\tilde W)=B(\tilde W,\tilde Z)$, and complex-valued. The Hermitian pairing and the holomorphic form are the two natural pairings of a complex structure: the first is sesquilinear and positive definite, the second is bilinear and isotropic.

### The Cone

The **norm-form cone** is the zero set

$$
N(\tilde Z)=0 .
$$

For the pure-vector phase-space biquaternion it is the complex cone

$$
Z_1^2+Z_2^2+Z_3^2=0 ,
$$

equivalently, separating real and imaginary parts,

$$
|\mathbf q|^2-|\mathbf p|^2=0,\qquad \mathbf q\cdot\mathbf p=0 .
$$

The cone is the locus where the configuration and momentum magnitudes are equal and the two vectors are orthogonal; it is isotropic for the holomorphic form, $B(\tilde Z,\tilde Z)=N(\tilde Z)=0$. Two remarks are needed. First, the condition equates the magnitudes of $\mathbf q$ and $\mathbf p$, which carry different physical dimensions unless a scale is fixed; the cone is therefore a statement about the complexified phase space after a symplectic normalization, and it is not by itself a physically invariant locus. Second, the cone meets the real phase space $\tilde q,\tilde p$ real only at $\tilde Z=0$: the complex bilinear form is definite there, and its real zero set is a single point. The cone is a genuinely complex object.

The algebra's reason for caring about the cone is that its points are the **zero divisors**: the biquaternions with $N(\tilde Q)=0$ are exactly the elements $\tilde Q\neq0$ for which multiplication by $\tilde Q$ is not invertible, so the norm form's cone is the singular locus of the algebra's product. This is the same cone that the companion articles identify as the boundary of the idempotent (state) manifold in $\mathbb{M}_+$ and as the light cone of the material sector.

### The Material Light Cone

The cone becomes physical when the scalar coordinate is imaginary. For a material-sector four-vector $\tilde X=ict\,e_0+\mathbf x\in\mathbb{M}_-$,

$$
N(\tilde X)=(ict)^2+\mathbf x^2=-c^2t^2+\mathbf x^2 ,
$$

which is the Minkowski interval; its zero set $N(\tilde X)=0$ is the **light cone**. So the light cone is the real slice of the norm-form cone, obtained by taking the scalar coefficient of the phase-space biquaternion to be purely imaginary rather than real. The indefinite signature of the Minkowski form and the definiteness of the Euclidean phase-space form are the same ambiguity of the norm form under a complex rotation of its scalar direction.

The same computation identifies the characteristic cone of the d'Alembertian. For a plane-wave biquaternion $\tilde K=\frac{i\omega}{c}e_0+\mathbf k$, the norm form is

$$
N(\tilde K)=-\frac{\omega^2}{c^2}+\mathbf k^2 ,
$$

and $N(\tilde K)=0$ is the dispersion relation $\omega^2/c^2=\mathbf k^2$ of the wave equation $\Box\tilde\Phi=0$. On a plane wave of frequency $\omega$ and wave vector $\mathbf k$, whose wave biquaternion is $\tilde K=\frac{i\omega}{c}e_0+\mathbf k$, the operator $\Box=\partial_{ict}^2+\Delta$ acts as the eigenvalue

$$
(iK_0)^2+(i\mathbf k)^2
=-\left(K_0^2+\mathbf k^2\right)=-N(\tilde K)=\frac{\omega^2}{c^2}-\mathbf k^2,
\qquad K_0=\frac{i\omega}{c},
$$

so $\Box\tilde\Phi=0$ is exactly $N(\tilde K)=0$; the overall sign of the symbol is immaterial for the kernel, and the **norm-form cone is the characteristic cone of the d'Alembertian.** The cone is thus at once the zero-divisor cone of the algebra, the light cone of the material sector, and the wave cone of the field equation.

## The Coadjoint Orbit and the Norm-Form Level Sets

The norm form's level sets carry the symplectic structure in the case the companion articles develop. Let $\tilde S\in\mathbb{H}_{\mathbb{B}}\cap\mathbb{M}_-$ be a real pure quaternion, identified with a vector $\mathbf S$, and consider the level sets

$$
N(\tilde S)=|\mathbf S|^2=S^2 .
$$

These are the spheres of radius $S$ in the three-dimensional space of pure real quaternions. On a sphere, the **Souriau–Kirillov form** is

$$
\omega_{\mathrm{S}}
=\frac{1}{S}\,\Omega_S,
\qquad
\Omega_S=\frac{1}{2S}\,\varepsilon_{ijk}S_i\,dS_j\wedge dS_k ,
$$

where $\Omega_S$ is the area form of the sphere of radius $S$ (the sum over $i,j,k$ is unrestricted; the explicit $\tfrac12$ is what makes the expression the area form rather than twice it). The division by $S$ is the Souriau normalization: it is fixed by requiring that the inverse form give the bracket $\{S_i,S_j\}=\varepsilon_{ijk}S_k$ of the companion article, and it is checked at once at the north pole, where $\omega_{\mathrm S}=S^{-1}dS_1\wedge dS_2$ and the bracket reads $\{S_1,S_2\}=S_3=S$. The form is non-degenerate on the sphere and closed. The Hamiltonian flow generated by $H=2\mathbf G\cdot\mathbf S$ is the rotor conjugation $\tilde S\mapsto e^{t\tilde G}\tilde S\,e^{-t\tilde G}$, as the companion article *Similitudes Between Biquaternion Rotors and Hamiltonian Flow* establishes, with $\{S_i,S_j\}=\varepsilon_{ijk}S_k$.

The norm form enters in two ways. First, the orbits are the level sets of $N$; the symplectic form is the Souriau form on those level sets, and the norm form's gradient is normal to them. Second, the level $S=0$ is the **degenerate orbit**: the sphere shrinks to a point, the area form collapses, and $N(\tilde S)=0$ is exactly the norm-form cone. The cone is therefore the singular (zero-radius) member of the family of coadjoint orbits on which the symplectic form lives. On the cone the form degenerates, and the algebra's product degenerates with it; away from the cone the orbifold of level sets carries a non-degenerate symplectic form. This is the precise sense in which the symplectic form and the norm-form cone are two aspects of one structure.

## Darboux Coordinates and the Canonical Frame

In the biquaternion phase space the coordinates $\tilde q,\tilde p$ are already Darboux coordinates: the form $\omega=\sum_k dq_k\wedge dp_k$ is constant, and the Poisson brackets are the canonical ones, $\{q_\mu,p_\nu\}=\delta_{\mu\nu}$. A rotor conjugation $\tilde Z\mapsto\tilde R\tilde Z\tilde R^\dagger$ with $N(\tilde R)=e_0$, restricted to the phase space, is a rotation of the phase-space coordinates; it preserves $N$ and $g$ and, when it acts as an algebra automorphism commuting with $i$, it preserves $\omega$ as well. The cubic terms that would obstruct Darboux coordinates in a curved symplectic manifold are absent here because the phase space is linear; the only non-triviality is the noncommutativity of the quaternion product, which affects the interpretation of the coordinates but not the constancy of the form.

A point worth stating precisely: the phase-space biquaternion $\tilde Z=\tilde q+i\tilde p$ is a complexification of the phase-space point, and the symplectic form is the imaginary part of the Hermitian pairing on that complexification. The complexification is not an extra structure added to mechanics; it is the algebra's own complex structure, the same $i$ that appears in the sector decomposition $\mathbb{B}=\mathbb{M}_-\oplus\mathbb{M}_+$ and that exchanges the sectors.

## What Is Structural and What Is Familiar

The material of this article divides as follows.

**Familiar, rewritten.** The symplectic form, its closedness and non-degeneracy, Darboux's theorem, the Hamiltonian vector field, the Poisson bracket, and the Kähler triple $(g,\omega,J)$ are standard symplectic geometry, cited as such. The coadjoint-orbit picture and the Souriau form are standard; the rotor realization is the companion article's subject.

**Structurally the algebra's.**

1. The Hermitian pairing's scalar part splits as $g+i\omega$: the metric and the symplectic form are the real and imaginary parts of one complex pairing. The algebra carries the pairing; the split is forced by the Hermitian conjugation.
2. The algebra's complex structure $i$ is the Kähler $J$; it satisfies $g(i\tilde Z,\tilde W)=\omega(\tilde Z,\tilde W)$ and $g(i\tilde Z,i\tilde W)=g(\tilde Z,\tilde W)$ identically.
3. The symplectic form is the scalar part of a biquaternion two-form: $\omega=\frac{i}{2}\mathrm{Sc}(d\tilde Z\wedge d\tilde Z^\dagger)$, and $d\tilde Z\wedge d\tilde Z=0$.
4. The Poisson bracket is the imaginary part of the same pairing on gradients: $\{f,g\}=\mathrm{Im}\,\mathrm{Sc}((\nabla f)^\dagger\nabla g)$.
5. The norm-form cone is simultaneously the zero-divisor cone of the algebra, the light cone of the material sector, and the characteristic cone of $\Box$; and it is the degenerate member of the family of coadjoint orbits.

## Summary

The symplectic form and the norm-form cone are the two canonical quadratic structures of the biquaternion algebra, and this article relates them.

- For the phase-space biquaternion $\tilde Z=\tilde q+i\tilde p$, the Hermitian scalar pairing satisfies $\mathrm{Sc}(\tilde Z^\dagger\tilde W)=g(\tilde Z,\tilde W)+i\omega(\tilde Z,\tilde W)$, with $g$ the Euclidean metric of phase space and $\omega$ the symplectic form $\omega=\sum_k dq_k\wedge dp_k$.
- The algebra's complex structure $i$ is the Kähler $J$: $g(i\tilde Z,\tilde W)=\omega(\tilde Z,\tilde W)$ and $g(i\tilde Z,i\tilde W)=g(\tilde Z,\tilde W)$.
- The symplectic potential is $\theta=\frac12\mathrm{Im}\,\mathrm{Sc}(\tilde Z^\dagger d\tilde Z)$, with $d\theta=\omega$; equivalently $\omega=\frac{i}{2}\mathrm{Sc}(d\tilde Z\wedge d\tilde Z^\dagger)$, while $d\tilde Z\wedge d\tilde Z=0$.
- The Poisson bracket is the imaginary part of the same pairing: $\{f,g\}=\mathrm{Im}\,\mathrm{Sc}((\nabla f)^\dagger\nabla g)$ with $\nabla f=\sum_\mu e_\mu(\partial_{q_\mu}f+i\partial_{p_\mu}f)$.
- The holomorphic companion of the Hermitian pairing is the norm form $N(\tilde Z)=\sum_\mu Z_\mu^2$, whose zero set is the norm-form cone. On the material sector the cone is the light cone $N(\tilde X)=0$ and the characteristic cone $N(\tilde K)=0$ of the d'Alembertian; in the algebra it is the zero-divisor cone; on the coadjoint orbit it is the degenerate level $S=0$ of a family whose non-degenerate members carry the Souriau form.

The symplectic form is the antisymmetric (imaginary) part of one Hermitian pairing, the metric is its symmetric (real) part, the algebra's complex structure is the compatible $J$, and the norm-form cone is the isotropic cone of the holomorphic form of the same complex structure. Nothing in this article is quantum: the Hermitian pairing is read as a classical phase-space form, and the cone is the classical light and wave cone.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde Z=\tilde q+i\tilde p$ | Phase-space biquaternion |
| $\tilde Z^\dagger=-\tilde q+i\tilde p$ | Hermitian conjugate for pure real $\tilde q,\tilde p$ |
| $\mathrm{Sc}(\tilde Z^\dagger\tilde W)$ | Hermitian scalar pairing |
| $g(\tilde Z,\tilde W)=\mathbf q\cdot\mathbf r+\mathbf p\cdot\mathbf s$ | Euclidean metric of phase space |
| $\omega(\tilde Z,\tilde W)=\mathbf q\cdot\mathbf s-\mathbf p\cdot\mathbf r$ | Symplectic form, $\omega=\sum_k dq_k\wedge dp_k$ |
| $i$ | Central scalar imaginary; the Kähler $J$ |
| $\theta=\frac12\mathrm{Im}\,\mathrm{Sc}(\tilde Z^\dagger d\tilde Z)$ | Symplectic potential, $d\theta=\omega$ |
| $N(\tilde Q)=\tilde Q\bar{\tilde Q}=\sum_\mu Q_\mu^2$ | Norm form (holomorphic) |
| $B(\tilde Z,\tilde W)=\mathrm{Sc}(\tilde Z\bar{\tilde W})$ | Symmetric complex bilinear form of $N$ |
| $N(\tilde X)=0$, $\tilde X=ict\,e_0+\mathbf x$ | Light cone of the material sector |
| $N(\tilde K)=0$, $\tilde K=\frac{i\omega}{c}e_0+\mathbf k$ | Characteristic cone of $\Box$ |
| $N(\tilde S)=S^2$ | Coadjoint-orbit level set; $S=0$ is the cone |
| $\omega_{\mathrm S}=\frac{1}{S}\Omega_S,\ \ \Omega_S=\frac{1}{2S}\varepsilon_{ijk}S_i dS_j\wedge dS_k$ | Souriau–Kirillov form on the orbit (area form divided by $S$) |

## Further Reading

- V. I. Arnold, *Mathematical Methods of Classical Mechanics* (Springer, 1989), for symplectic manifolds, Darboux's theorem, and Hamiltonian vector fields.
- Ralph Abraham and Jerrold E. Marsden, *Foundations of Mechanics* (Benjamin, 1978), for the symplectic and Poisson formulations and the momentum map.
- V. Guillemin and S. Sternberg, *Symplectic Techniques in Physics* (Cambridge, 1984), for the Kostant–Kirillov–Souriau form on coadjoint orbits.
- A. A. Kirillov, *Lectures on the Orbit Method* (American Mathematical Society, 2004), for coadjoint orbits and their symplectic structure.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for complex structures, Kähler forms, and the geometric algebra of Minkowski space.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for zero divisors and the norm form in Clifford algebras.
- W. R. Hamilton, *Lectures on Quaternions* (Hodges and Smith, 1853), for the quaternion product and its conjugate.
