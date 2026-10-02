# __Hilbert Spaces__

## Introduction

A Hilbert space is a vector space with an inner product whose induced norm is complete. The inner product is a sesquilinear form with a conjugation built into it, and the present article reads the space through that form: the second slot is conjugate-linear, the form is Hermitian, positive definite, and it induces the norm, so a Hilbert space is a normed space together with a compatible involution on the scalars. The companion article *Banach and Hilbert Spaces* of this category develops the same space in the normed setting and proves the projection theorem, the existence of orthonormal bases and the classification of the separable case; the present article is the involution-first reading on which the rest of the group builds.

The one structure that the form adds to the vector-space data is the **conjugation**: an antilinear isometric involution $J$ with $\langle Jx,Jy\rangle=\langle y,x\rangle$, which exists on every Hilbert space, is the componentwise conjugation in the sequence and function models, and is the algebraic shadow of the sesquilinearity. Conjugations classify the real forms of a complex Hilbert space, and they make the adjoint of an operator expressible through the real structure. This article fixes the form, the completeness, the orthonormal bases, the projection theorem, the conjugation and the self-duality, and points to the operator theory that these produce.

Throughout, $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$, $H$ is a Hilbert space over $\mathbb{K}$ with inner product $\langle\cdot,\cdot\rangle$ **linear in the first argument and conjugate-linear in the second**, and $\|x\|=\sqrt{\langle x,x\rangle}$ is the induced norm. A **conjugation** on $H$ is an antilinear map $J$ with $J^2=I$ and $\langle Jx,Jy\rangle=\langle y,x\rangle$. The dual is $H^*$, the bounded operators are $B(H)$, and the adjoint is $T^*$.

## The Inner Product and the Norm

**Definition.** An **inner product** on a $\mathbb{K}$-vector space $H$ is a pairing $\langle\cdot,\cdot\rangle:H\times H\to\mathbb{K}$ that is linear in the first argument, conjugate-linear in the second, Hermitian in the sense $\langle x,y\rangle=\overline{\langle y,x\rangle}$, and positive definite, $\langle x,x\rangle>0$ for $x\neq0$. An **inner product space** is a pair $(H,\langle\cdot,\cdot\rangle)$, and its induced norm is $\|x\|=\sqrt{\langle x,x\rangle}$.

**Theorem (Cauchy–Schwarz and the norm axioms).** For all $x,y\in H$,

$$
|\langle x,y\rangle|\le\|x\|\,\|y\| ,
$$

with equality exactly when $x,y$ are linearly dependent, and $\|\cdot\|$ is a norm: the triangle inequality is

$$
\|x+y\|\le\|x\|+\|y\| .
$$

*Proof.* If $y\neq0$, write $x=\alpha y+z$ with $\alpha=\langle x,y\rangle/\|y\|^2$ so that $\langle z,y\rangle=0$; then $\|x\|^2=|\alpha|^2\|y\|^2+\|z\|^2\ge|\langle x,y\rangle|^2/\|y\|^2$, which is the inequality, and equality forces $z=0$. The triangle inequality follows from expanding $\|x+y\|^2$ and applying Cauchy–Schwarz. The form is recovered from the norm by the polarisation identity $\langle x,y\rangle=\frac14\sum_{k=0}^3i^k\|x+i^ky\|^2$ over $\mathbb{C}$.

**Proposition (the form as the involution on the scalars).** The sesquilinearity is exactly the statement that the map $x\mapsto\langle x,\cdot\rangle$ is linear while $y\mapsto\langle\cdot,y\rangle$ is conjugate-linear, and the Hermitian symmetry is the compatibility of the form with the conjugation of $\mathbb{K}$. So the form may be read as a linear structure in the first argument together with a conjugate-linear structure in the second, and the two are exchanged by the Hermitian symmetry.

*Proof.* The two linearity statements are the definition, and the Hermitian symmetry conjugates the scalars, which is the statement that the two structures are mutual conjugates.

**Theorem (Jordan–von Neumann).** A norm on a $\mathbb{K}$-vector space is induced by an inner product if and only if it satisfies the parallelogram law

$$
\|x+y\|^2+\|x-y\|^2=2\|x\|^2+2\|y\|^2 ,
$$

and the inner product is then unique and given by the polarisation identity.

*Proof.* Expanding the squares shows that an inner-product norm satisfies the law; conversely, defining the form by polarisation, the parallelogram law is precisely what is needed for additivity in each argument, and the remaining axioms follow. The norm of $\ell^p$ for $p\neq2$ and of $C(K)$ for $K$ with more than one point fails the law, so those spaces are not Hilbert spaces for their given norms.

## Completeness and the Projection Theorem

**Definition.** A **Hilbert space** is an inner product space that is complete for the induced norm.

**Proposition (closed subspaces).** A subspace $M\subseteq H$ is a Hilbert space under the restricted inner product exactly when it is closed; the completion of an incomplete inner product space is a Hilbert space containing it as a dense subspace, and every closed subspace of a Hilbert space is complemented by its orthogonal complement $M^{\perp}=\{y:\langle y,m\rangle=0\ \text{for all } m\in M\}$.

*Proof.* A complete subspace of a metric space is closed, and a closed subspace of a complete space is complete; the completion is the standard metric completion of the normed space, on which the polarized form extends by continuity.

**Theorem (projection).** Let $C\subseteq H$ be a nonempty closed convex set. For every $x\in H$ there is a unique $p\in C$ with $\|x-p\|=d(x,C)$, and if $C=M$ is a closed subspace then $x-p\perp M$ and

$$
H=M\oplus M^{\perp},\qquad x=p+q,\quad p\in M,\ q\in M^{\perp}.
$$

*Proof.* A minimising sequence is Cauchy by the parallelogram law applied to $x-c_m$ and $x-c_n$, so completeness gives a limit that is a nearest point, and uniqueness is again the parallelogram law; for a subspace, minimising $t\mapsto\|x-p-tm\|^2$ gives $\operatorname{Re}\langle x-p,m\rangle=0$ and, over $\mathbb{C}$, also $\langle x-p,im\rangle=0$, so $x-p\perp M$.

**Corollary.** The orthogonal projection $P_M$ onto a closed subspace $M$ is the linear map $x\mapsto p$ of the theorem; it is idempotent and self-adjoint, $P_M^2=P_M=P_M^*$, it is a contraction, and $I-P_M=P_{M^{\perp}}$. Conversely every self-adjoint idempotent of $B(H)$ is the orthogonal projection onto its range.

*Proof.* Linearity follows from the characterisation of $p$ as the unique element of $M$ with $x-p\perp M$; the self-adjointness is $\langle p_M(x),y\rangle=\langle x,p_M(y)\rangle$ by the orthogonality of the three pieces, and the converse is the projection theorem applied to the range.

## Orthonormal Bases and the Conjugation

**Definition.** A set $\{e_\alpha\}$ is **orthonormal** if $\langle e_\alpha,e_\beta\rangle=\delta_{\alpha\beta}$, and an **orthonormal basis** if it is maximal, equivalently if no nonzero vector is orthogonal to all of it. Each vector has the expansion $x=\sum_\alpha\langle x,e_\alpha\rangle e_\alpha$ against a basis, with $\|x\|^2=\sum_\alpha|\langle x,e_\alpha\rangle|^2$ (Parseval), and every Hilbert space has an orthonormal basis, countable exactly when the space is separable.

*Proof.* This is the Bessel–Parseval theory of *Banach and Hilbert Spaces*, where the existence by Zorn's lemma and the classification by the cardinality of a basis are proved.

**Definition.** A **conjugation** on $H$ is an antilinear map $J:H\to H$ with

$$
J^2=I,\qquad \langle Jx,Jy\rangle=\langle y,x\rangle ,
$$

equivalently an antiunitary involution. A vector is **real** for $J$ if $Jx=x$; the **real form** is the real Hilbert space $H_J=\{x:Jx=x\}$ with the real part of the form.

**Proposition (existence and the models).** Every Hilbert space carries a conjugation: choose an orthonormal basis $\{e_\alpha\}$ and set $J(\sum_\alpha c_\alpha e_\alpha)=\sum_\alpha\bar c_\alpha e_\alpha$. On $\ell^2$ the standard conjugation is the componentwise conjugation, and on $L^2(X,\mu)$ it is $f\mapsto\bar f$; the real form of the second is the space of real-valued square-integrable functions.

*Proof.* The map defined by conjugating the coordinates is antilinear, its square is the identity, and it reverses the form because it conjugates each coefficient; the models are the special cases of the coordinate formula in the standard bases.

**Proposition (conjugations and the real forms).** The conjugations of $H$ are in bijection with the real Hilbert subspaces $H_J$ whose complex span is $H$; two conjugations differ by a unitary of $H$, and the group of unitaries acts transitively on them. A conjugation is an isometry of $H$, so it is continuous, and its fixed space $H_J$ is closed and totally real, $H_J\cap iH_J=0$ over $\mathbb{C}$.

*Proof.* The fixed space of an antiunitary involution is a real closed subspace spanning $H$ over $\mathbb{C}$, and conversely a real form determines the conjugation by $J(x+iy)=x-iy$ on the complex span; for two conjugations the composite is a unitary, giving the transitivity; the closedness is the continuity of an isometry and the total reality is $J(ix)=-iJ(x)$.

## Self-Duality and the Riesz Map

**Theorem (Riesz representation).** For every bounded linear functional $\varphi\in H^*$ there is a unique $y\in H$ with

$$
\varphi(x)=\langle x,y\rangle\quad(x\in H),\qquad \|\varphi\|=\|y\| .
$$

The map $\Phi:H\to H^*$, $\Phi(y)=\langle\cdot,y\rangle$, is a conjugate-linear isometric bijection, and $H$ is reflexive.

*Proof.* If $\varphi\neq0$ its kernel is a closed hyperplane, whose orthogonal complement is spanned by a unit vector $e$; then $y=\overline{\varphi(e)}e$ represents $\varphi$ and the norm identity follows from Cauchy–Schwarz with equality. Uniqueness is the nondegeneracy of the form, conjugate-linearity is the sesquilinearity, and reflexivity is the surjectivity of the map $H\to H^{**}$ obtained by iterating $\Phi$.

**Proposition (the form and the dual form).** The Riesz map $\Phi$ carries the inner product of $H$ to the dual pairing, so the form on $H^*$ defined by $\langle\Phi x,\Phi y\rangle=\overline{\langle x,y\rangle}$ makes $H^*$ a Hilbert space isometric to $H$ through a conjugate-linear map; in this sense a Hilbert space is its own dual, with the identification conjugate-linear rather than linear.

*Proof.* Insert the definition of $\Phi$ and use the Hermitian symmetry; the induced norm on $H^*$ is the operator norm by the Riesz theorem, so the identification is isometric.

**Example (finite dimension).** For $H=\mathbb{K}^n$ with the standard form the Riesz map is $y\mapsto\langle\cdot,y\rangle$, the conjugation is the componentwise conjugation, and the projection theorem is the orthogonal decomposition of linear algebra. For the real Hilbert space $\mathbb{R}^n$ the conjugation is the identity and the form is symmetric.

**Example (the Dirichlet space and the Sobolev spaces).** The Sobolev space $H^1_0(\Omega)$ with $\langle u,v\rangle=\int\nabla u\cdot\nabla\bar v$ is a Hilbert space whose conjugation is complex conjugation of functions; it is the form domain of the Dirichlet form of *Dirichlet Forms and the Hermitian Dirichlet Principle*, and it shows that a Hilbert space is often specified by its form rather than by its coordinates.

## Summary

A Hilbert space is an inner product space complete for the induced norm; the inner product is linear in the first argument and conjugate-linear in the second, the Hermitian symmetry is its compatibility with the conjugation of the scalars, and the Cauchy–Schwarz inequality and the parallelogram law govern it, the latter characterising the inner-product norms by the Jordan–von Neumann theorem. Every closed convex set has a unique nearest point, and for a closed subspace this gives the orthogonal decomposition $H=M\oplus M^{\perp}$ and the orthogonal projection $P_M$, idempotent and self-adjoint. Orthonormal bases exist, they give the expansion $x=\sum\langle x,e_\alpha\rangle e_\alpha$ and Parseval's identity, and the space is separable exactly when it has a countable basis. The sesquilinearity is carried by a **conjugation** $J$, antilinear and antiunitary with $J^2=I$, which exists on every Hilbert space, is componentwise conjugation in the standard models, and whose fixed space is a real form; the conjugations are permuted transitively by the unitaries. The Riesz representation theorem identifies $H^*$ with $H$ conjugate-linearly and isometrically, so a Hilbert space is reflexive and is its own dual, and the operator theory that this structure supports is *Bounded Operators on a Hilbert Space* and *Self-Adjoint Operators and the Spectral Theorem*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $H$, $\langle\cdot,\cdot\rangle$ | Hilbert space and inner product, linear in the first argument |
| $\|x\|^2=\langle x,x\rangle$ | the induced norm |
| $M^{\perp}$ | orthogonal complement, $H=M\oplus M^{\perp}$ for closed $M$ |
| $P_M$ | orthogonal projection, $P_M^2=P_M=P_M^*$ |
| $\{e_\alpha\}$, $\delta_{\alpha\beta}$ | orthonormal set and the Kronecker delta |
| $J$, $J^2=I$ | conjugation, antiunitary involution |
| $H_J=\{x:Jx=x\}$ | real form of the conjugation |
| $\Phi(y)=\langle\cdot,y\rangle$ | Riesz map, conjugate-linear isometry $H\to H^*$ |
| $H^*\cong H$ | self-duality, conjugate-linear |

## Further Reading

- Paul R. Halmos, *Introduction to Hilbert Space* (Chelsea, 2nd ed. 1957), for the geometry of the inner product, orthonormal bases and the projection theorem.
- Frigyes Riesz and Béla Sz.-Nagy, *Functional Analysis* (Dover, 1990), for the form, the projection theorem and the Riesz representation theorem.
- John B. Conway, *A Course in Functional Analysis* (Springer, 2nd ed. 1990), for the completeness, the orthonormal bases and the duality of Hilbert space.
- Erwin Kreyszig, *Introductory Functional Analysis with Applications* (Wiley, 1978), for the elementary theory and the standard examples.
- Israel M. Gelfand and Naum Ya. Vilenkin, *Generalized Functions*, vol. 4 (Academic Press, 1964), for the real forms and the conjugations of a Hilbert space.
