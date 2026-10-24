# __Norm Regularity and Degeneracy in the Biquaternion Algebra__

## Introduction

The biquaternion algebra carries four algebraic norms, the four forms read at two equal arguments. Only one of them is multiplicative, the quaternionic bilinear algebraic norm, and only that one decides invertibility. This article defines it, proves its multiplicative law, and separates the elements of $\mathbb{B}$ into the two cases of its value: the regular case of non-zero norm, whose elements are the units of the algebra and form a group, and the degeneracy case of zero norm, the null cone. This article is the study of this one norm and of its two cases.

**Notation.** An element is $\tilde Q=Q_t e_t+\vec Q$, its natural conjugation is $\tilde Q^{\natural}=Q_t-\vec Q$, and the product of the article is the plain product $\tilde P\tilde Q$ of the algebra, which is associative and has the two-sided unit $e_t$. The norm is $N(\tilde Q)=\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^2$. The product $\tilde P^{\natural}\tilde Q$ has a left unit and no right unit; it is recorded in one remark in §*The Group of Units*, because only the plain product has a group of units.

## The Four Algebraic Norms

The four algebraic norms are the four forms read at two equal arguments:

$$
\langle\tilde Q\rangle=\sum_\mu\varepsilon_\mu Q_\mu^2,\qquad
\langle\tilde Q\rangle_{*}=\sum_\mu|Q_\mu|^2,\qquad
\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^2,\qquad
\langle\tilde Q\rangle_{\natural*}=\sum_\mu\varepsilon_\mu|Q_\mu|^2,
$$

with $\varepsilon_t=1$ and $\varepsilon_x=\varepsilon_y=\varepsilon_z=-1$. They are the general plain bilinear norm, the Hermitian norm, the general quaternionic bilinear norm, and the Krein norm.

Only $\langle\cdot\rangle_{\natural}$ is multiplicative. The general plain bilinear norm is not: $\vec e_x\vec e_y=\vec e_z$ gives $\langle\vec e_x\vec e_y\rangle=-1$ against $\langle\vec e_x\rangle\langle\vec e_y\rangle=1$. It decides no invertibility either: $e_t+\vec e_x$ has $\langle\cdot\rangle=0$ and is a unit, while $e_t+i\vec e_x$ has $\langle\cdot\rangle=2$ and is a zero divisor. The Hermitian norm is definite and real, the Krein norm is indefinite and real; neither is multiplicative. The criterion is carried by $\langle\cdot\rangle_{\natural}$ alone, which is why the rest of the article studies that norm and calls it the reduced norm.

## The Reduced Norm

**Definition.** The **reduced norm**, also the **quaternionic bilinear algebraic norm**, of $\tilde Q=Q_t e_t+\vec Q$ is the complex scalar

$$
N(\tilde Q)=\langle\tilde Q\rangle_{\natural}=\sum_{\mu}Q_{\mu}^{2}=Q_t^{2}+(\vec Q,\vec Q).
$$

**The identity of the norm.** Because $(Q_t-\vec Q)(Q_t+\vec Q)=Q_t^2-\vec Q^2$ and $\vec Q^2=-(\vec Q,\vec Q)$ for a vector part,

$$
\tilde Q\tilde Q^{\natural}=\tilde Q^{\natural}\tilde Q=N(\tilde Q)e_t.
$$

The value is a complex scalar, not a length. Its vanishing set is the null cone in $\mathbb{B}$, not a sphere. The name records the algebra: $\mathbb{B}$ is the complexification of the quaternions, and $N$ is the reduced norm of that algebra.

**Theorem (multiplicativity).** For all $\tilde P,\tilde Q\in\mathbb{B}$,

$$
N(\tilde P\tilde Q)=N(\tilde P)N(\tilde Q).
$$

*Proof.* The natural conjugation is an anti-automorphism, so $(\tilde P\tilde Q)^{\natural}=\tilde Q^{\natural}\tilde P^{\natural}$. Then

$$
(\tilde P\tilde Q)(\tilde P\tilde Q)^{\natural}
=\tilde P\tilde Q\tilde Q^{\natural}\tilde P^{\natural}
=\tilde P\,N(\tilde Q)e_t\,\tilde P^{\natural}
=N(\tilde Q)\tilde P\tilde P^{\natural}
=N(\tilde P)N(\tilde Q)e_t,
$$

and the left side is $N(\tilde P\tilde Q)e_t$ by the identity of the norm.

**Consequence.** The unit set $\{N\neq0\}$ and the null cone $\{N=0\}$ are both stable under the product.

## The Two Cases

The value of the norm separates the algebra into two parts.

| condition on $N(\tilde Q)$ | set | name |
|---|---|---|
| $\neq0$ | $\mathbb{B}^{\times}=\{N\neq0\}$ | the **regular case**: the group of units |
| $=0$ | the **null cone** $\mathcal C=\{N=0\}$ | the **degeneracy case**: the origin together with the zero divisors |

The split is by the value of the norm, not by zero-divisorhood. The origin lies in the null cone, and it is not a zero divisor; every non-zero point of the cone is one. So the regular case is exactly the unit group, and the degeneracy case is the cone, of which the zero-divisor set is the punctured part.

**Remark (the word regular).** In ring theory a regular element is a non-zero-divisor, and the origin qualifies, so the ring-regular elements are $\mathbb{B}^{\times}\cup\{0\}$. The title uses **norm-regular** instead: the regular side is the unit group, and the origin is norm-degenerate. The two readings differ at one point, the apex, and the article follows the norm.

## The Criterion

**Criterion.** For $\tilde Q\neq0$ the following are equivalent:

1. $N(\tilde Q)\neq0$;
2. $\tilde Q$ is a unit of the plain product;
3. $\tilde Q$ is not a zero divisor;
4. the left translation $\tilde X\mapsto\tilde Q\tilde X$ is injective;
5. the right translation $\tilde X\mapsto\tilde X\tilde Q$ is injective.

*Proof.* (1)$\Rightarrow$(2): the inverse is $\tilde Q^{\natural}/N(\tilde Q)$, by the identity of the norm. (2)$\Rightarrow$(3): a unit cannot annihilate a non-zero element. (3)$\Rightarrow$(4): if the left translation is not injective, some $\tilde X\neq0$ has $\tilde Q\tilde X=0$, and $\tilde Q$ is a left zero divisor. (4)$\Rightarrow$(1): if $N(\tilde Q)=0$ then $\tilde Q\tilde Q^{\natural}=0$ with $\tilde Q^{\natural}\neq0$, so the left translation kills $\tilde Q^{\natural}$. The right-hand conditions are treated the same way.

Equivalently, for $\tilde Q\neq0$, the element is a zero divisor exactly when $N(\tilde Q)=0$. The norm therefore decides invertibility in the precise sense that its non-vanishing set is the unit group; and its vanishing set, minus the origin, is the zero-divisor set.

## The Group of Units

**Definition.** The **unit group** of the plain product is

$$
\mathbb{B}^{\times}=\{\tilde Q\in\mathbb{B}:N(\tilde Q)\neq0\}.
$$

By §*The Criterion* it is the complement of the null cone: the algebra minus the origin and the zero divisors.

**Theorem.** $\mathbb{B}^{\times}$ is a group under the plain product.

*Proof.* Closure: $N(\tilde P\tilde Q)=N(\tilde P)N(\tilde Q)\neq0$. Associativity: the plain product is associative. Identity: $e_t$, with $N(e_t)=1$. Inverse: for $\tilde Q\in\mathbb{B}^{\times}$,

$$
\tilde Q^{-1}=\frac{\tilde Q^{\natural}}{N(\tilde Q)},
$$

since $\tilde Q\tilde Q^{\natural}=\tilde Q^{\natural}\tilde Q=N(\tilde Q)e_t$.

**Remark (the inverse is the conjugate over the norm).** In the plain product the two-sided inverse is $\tilde Q^{\natural}/N(\tilde Q)$. In the product $\tilde P^{\natural}\tilde Q$ the one-sided solution is $\tilde Q/N(\tilde Q)$. The criterion $N\neq0$ is the same; the inverse is not. The unit group is a plain-product object.

**Theorem (the partition).** The algebra is the disjoint union

$$
\mathbb{B}=\mathbb{B}^{\times}\uplus\{0\}\uplus\mathcal Z,
$$

of the units, the origin, and the zero divisors. Equivalently,

$$
\mathbb{B}=\mathbb{B}^{\times}\uplus\mathcal C,
$$

with $\mathcal C=\{N=0\}$ the null cone, which contains the origin and the zero divisors.

*Proof.* The two sets $\{N\neq0\}$ and $\{N=0\}$ are complementary, and the cone splits into the origin and its punctured part, which is the zero-divisor set by §*The Zero Divisors*.

**Corollary (topology).** $\mathbb{B}^{\times}$ is open and dense in $\mathbb{B}$; $\mathcal C$ is closed, has empty interior, and is of real codimension $2$; and

$$
\partial\mathbb{B}^{\times}=\mathcal C.
$$

The origin is the only point of the cone that is not a zero divisor.

*Proof.* The cone is the zero set of a polynomial, hence closed, and it is a proper algebraic subset, hence of empty interior; its complement is open and dense. The boundary of the group is the intersection of the closures of the group and of its complement, that is the cone.

**Remark (the $\natural$-bilinear product).** For the product $\tilde P^{\natural}\tilde Q$ the element $e_t$ is a left unit and there is no right unit, so no element has a two-sided inverse and there is no group of units. The two one-sided equations with $e_t$ have the common unique solution $\tilde Q/N(\tilde Q)$ exactly when $N(\tilde Q)\neq0$. The criterion is unchanged; what is lost is the group, and with it the two-sided inverse $\tilde Q^{\natural}/N(\tilde Q)$. That is why this article uses the plain product.

## The Zero Divisors

**Definition.** Let $\cdot$ be a product on $\mathbb{B}$. A non-zero $\tilde Q$ is a **left zero divisor** of $\cdot$ if $\tilde Q\cdot\tilde X=0$ for some $\tilde X\neq0$, a **right zero divisor** if $\tilde X\cdot\tilde Q=0$ for some $\tilde X\neq0$, and a **zero divisor** if it is one or the other. The element $0$ is not a zero divisor of any product.

Throughout this section the product is the plain product $\tilde Q_1\tilde Q_2$ of the algebra, which is associative and has the two-sided unit $e_t$; it is the product in which the zero-divisor set is visible as a stratification.

**Theorem (the criterion).** A non-zero $\tilde Q$ is a zero divisor of the plain product exactly when $N(\tilde Q)=0$.

*Proof.* If $N(\tilde Q)=0$ and $\tilde Q\neq0$, then $\tilde Q\tilde Q^{\natural}=N(\tilde Q)e_t=0$ with $\tilde Q^{\natural}\neq0$, so $\tilde Q$ is a left zero divisor. Conversely, if $\tilde Q\tilde X=0$ with $\tilde X\neq0$ and $N(\tilde Q)\neq0$, then $\tilde Q$ is a unit of the plain product, of inverse $\tilde Q^{\natural}/N(\tilde Q)$, and $\tilde X=\tilde Q^{-1}\tilde Q\tilde X=0$, a contradiction.

**Remark (one set for the four products).** The same set is selected by the $\natural$-bilinear product: there the relevant square is $\tilde Q^{\natural}\tilde Q=N(\tilde Q)e_t$, so a vanishing norm gives $\tilde Q^{\natural}\tilde Q=0$. The four general products have four different zero-divisor equations and, in this algebra, one and the same zero-divisor set.

**Definition (the two strata).** The **pure stratum** and the **non-pure stratum** of the null cone are

$$
\mathcal C_{\mathrm p}=\{N=0,\ Q_t=0,\ \tilde Q\neq0\},\qquad
\mathcal C_{\mathrm{np}}=\{N=0,\ Q_t\neq0\}.
$$

**Observation.** On $\mathcal C$, $Q_t^2+\vec Q^2=0$, so

$$
Q_t=0\iff\vec Q^2=0\iff\tilde Q^2=0.
$$

The pure stratum is therefore the set of non-zero elements with vanishing square; on the non-pure stratum, where $Q_t\neq0$, the square is instead $\tilde Q^2=2Q_t\tilde Q$. No object outside the norm enters the characterisation.

**Theorem (the pure stratum).** Every element of $\mathcal C_{\mathrm p}$ is a nilpotent of index two: $\tilde Q=\vec Q$ and $\tilde Q^2=-\vec Q^2e_t=0$. The stratum is a complex cone of complex dimension $2$ and real dimension $4$ in the three vector coefficients, cut out by the single quadratic equation

$$
Q_x^2+Q_y^2+Q_z^2=0.
$$

*Proof.* On $\mathcal C_{\mathrm p}$ the scalar part vanishes and $Q_t^2+\vec Q^2=0$ gives $\vec Q^2=0$, so $\tilde Q=\vec Q$ and $\tilde Q^2=-\vec Q^2e_t=0$. The equation is one complex equation in the three complex vector coefficients, homogeneous of degree two, with gradient $2(Q_x,Q_y,Q_z)$ non-vanishing off the origin; its real dimension is $2\cdot3-2=4$ and its complex dimension is $3-1=2$.

**Real-coordinate form.** Write $\vec Q=\vec\rho+i\vec\rho'$ with $\vec\rho,\vec\rho'\in\mathbb{R}^3$. Then

$$
\vec Q^2=(|\vec\rho'|^2-|\vec\rho|^2)e_t-2i(\vec\rho\cdot\vec\rho')e_t,
$$

so the pure stratum is the set of bivectors with

$$
\vec\rho\cdot\vec\rho'=0,\qquad |\vec\rho|=|\vec\rho'|.
$$

Equivalently it is the set of elements $r(\vec u+i\vec u_\perp)$ with $r>0$, $\vec u$ a real unit vector and $\vec u_\perp$ a real unit vector perpendicular to $\vec u$: one radius, one direction and one perpendicular direction, that is $1+2+1=4$ real dimensions.

**Theorem (the non-pure stratum).** Every element of $\mathcal C_{\mathrm{np}}$ satisfies $\tilde Q^2=2Q_t\tilde Q$, and is therefore a non-zero complex multiple of a non-trivial idempotent:

$$
\tilde Q=2Q_t\tilde\Pi,\qquad \tilde\Pi=\frac{\tilde Q}{2Q_t},\qquad \tilde\Pi^2=\tilde\Pi.
$$

The stratum is open in $\mathcal C$, of real dimension $6$, and its complement in $\mathcal C$ is the pure stratum.

*Proof.* $\tilde Q^2=(Q_t^2-\vec Q^2)e_t+2Q_t\vec Q$; on $\mathcal C$ we have $\vec Q^2=-Q_t^2$, so $\tilde Q^2=2Q_t^2e_t+2Q_t\vec Q=2Q_t\tilde Q$. Dividing by $2Q_t\neq0$ gives $\tilde\Pi^2=\tilde\Pi$, and $\tilde\Pi\neq0,e_t$ because $\tilde Q\neq0$ and $\tilde Q$ is not a scalar multiple of $e_t$. The stratum is the complement in $\mathcal C$ of the closed subset $\{Q_t=0\}$, hence open in $\mathcal C$, and it has the dimension of $\mathcal C$.

**Peirce factorisation.** Let $\tilde\Pi=\tilde Q/(2Q_t)$ be the idempotent of a non-pure zero divisor. The mixed Peirce corners contain elements

$$
u\in\tilde\Pi\mathbb{B}(e_t-\tilde\Pi),\qquad w\in(e_t-\tilde\Pi)\mathbb{B}\tilde\Pi,
$$

normalised so that $uw=\tilde\Pi$, and both are square-zero: $u^2=w^2=0$. Hence every non-pure zero divisor is a scalar multiple of a product of two nilpotents,

$$
\tilde Q=2Q_t\,uw,\qquad u^2=w^2=0.
$$

The idempotents, their classification and their Peirce systems are *Ideals and Peirce Decompositions of the Biquaternion Algebra*; the factorisation is recorded here because it places the non-pure zero divisors in the same Peirce framework as the pure ones.

**Theorem (the zero-divisor set).** The set

$$
\mathcal Z=\{\tilde Q\neq0:N(\tilde Q)=0\}=\mathcal C\setminus\{0\}
$$

is a complex cone of complex dimension $3$ and real dimension $6$ in $\mathbb{B}\cong\mathbb{C}^4$. It is the complement of the units in the complement of the origin,

$$
\mathcal Z=\mathbb{B}\setminus\bigl(\{0\}\cup\mathbb{B}^{\times}\bigr),
$$

and it is stable under multiplication by non-zero complex scalars.

*Proof.* $N=0$ is one complex equation in the four complex coefficients, homogeneous of degree two, with non-vanishing gradient off the origin. The real dimension is $2\cdot4-2=6$ and the complex dimension is $4-1=3$; removing the origin changes neither.

**Correspondence (the remarkable subspaces).** By the signatures tabulated in §*The Norm on the Remarkable Subspaces*, the norm is definite on the centre, the quaternion subspace and the anti-quaternion subspace, so none of the three contains a zero divisor; the zero-divisor set in the vector subspace is the pure stratum; and the Hermitian and anti-Hermitian subspaces each carry a null cone. A generic zero divisor has all four coefficients non-zero and lies in none of them.

**Remark (the spectral reading).** Inside $\mathcal C$ the pure stratum is cut out by $\vec Q^2=0$, which is the quadratic equation that also marks the spectral-degenerate elements. The strata here are defined by $Q_t$ alone; the comparison of the two cones belongs to *Spectral Regularity and Degeneracy in the Biquaternion Algebra*.

### The Spinor Factorisation of a Null Element

The scalar-part split has a matrix reading that isolates it. Under the isomorphism $\mathsf M_2:\mathbb{B}\to M_2(\mathbb{C})$ the reduced norm is the determinant and the trace is twice the scalar part (*Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*):

$$
\det\mathsf M_2(\tilde Q)=N(\tilde Q),\qquad \operatorname{tr}\mathsf M_2(\tilde Q)=2Q_t.
$$

On the cone the determinant vanishes, so a non-zero $\mathsf M_2(\tilde Q)$ has rank one and is an outer product,

$$
\mathsf M_2(\tilde Q)=u\,v^{\mathsf T},\qquad u=\begin{pmatrix}u_1\\u_2\end{pmatrix}\in\mathbb{C}^2,\quad v^{\mathsf T}=(v_1\ v_2),
$$

and the pair is determined only up to $(u,v)\mapsto(\lambda u,\lambda^{-1}v)$. The column is the spinor factor and the row the cospinor factor; only the matrix identity is used below.

**Theorem (the scalar part is the contraction).** For a non-zero null $\tilde Q$ with $\mathsf M_2(\tilde Q)=uv^{\mathsf T}$,

$$
Q_t=\tfrac12\,v^{\mathsf T}u.
$$

*Proof.* $\operatorname{tr}(uv^{\mathsf T})=v^{\mathsf T}u$, while $\operatorname{tr}\mathsf M_2(\tilde Q)=2Q_t$.

**Corollary (the two strata).** For a non-zero null element,

$$
Q_t=0\iff v^{\mathsf T}u=0,
\qquad
Q_t\neq0\iff v^{\mathsf T}u\neq0.
$$

The pure stratum is therefore the set of null elements whose two rank-one factors are orthogonal for the bilinear pairing, and the non-pure stratum is its complement.

**Corollary (nilpotency).** For $\mathsf M_2(\tilde Q)=uv^{\mathsf T}$,

$$
\mathsf M_2(\tilde Q)^2=u\,(v^{\mathsf T}u)\,v^{\mathsf T}=(v^{\mathsf T}u)\,\mathsf M_2(\tilde Q),
$$

so $\mathsf M_2(\tilde Q)^2=0$ exactly when $v^{\mathsf T}u=0$, that is exactly when $Q_t=0$. This is the identity $\tilde Q^2=2Q_t\tilde Q$ in matrix form: the square is a multiple of the element, and the multiplier is the contraction of the two factors. On the non-pure stratum the multiplier is non-zero, and $\tilde Q/(2Q_t)=\tilde\Pi$ is the idempotent of the Peirce factorisation above.

## The Annihilators

**Definition.** The **left** and the **right annihilator** of $\tilde Q$ in the plain product are

$$
A(\tilde Q)=\{\tilde X:\tilde Q\tilde X=0\},\qquad
B(\tilde Q)=\{\tilde X:\tilde X\tilde Q=0\}.
$$

They are the kernels of the left and the right translation, and hence complex subspaces of $\mathbb{B}$.

**Theorem (the trichotomy).** The two cases of the norm are read as three dimensions, the same on both sides:

$$
\tilde Q=0:\ \dim A=\dim B=4;\qquad
N\neq0:\ \dim A=\dim B=0;\qquad
\tilde Q\neq0,\ N=0:\ \dim A=\dim B=2.
$$

*Proof.* At the origin both translations are the zero map. If $N\neq0$ then $\tilde Q$ is a unit, so both translations are bijections and both annihilators vanish. If $N=0$ and $\tilde Q\neq0$, the image of the left translation is the left ideal $\tilde Q\mathbb{B}$; it is non-zero, since it contains $\tilde Q$, and proper, since $e_t$ is not in it: $\tilde Q\tilde X=e_t$ has no solution by §*The Criterion*. The left ideals of $\mathbb{B}$ are $0$, the minimal left ideals, and $\mathbb{B}$, and a minimal left ideal is a complex plane (*Ideals and Peirce Decompositions of the Biquaternion Algebra*, §*The Decomposition into Minimal Left and Right Ideals*); so the image has complex dimension $2$ and the kernel has dimension $4-2=2$. The right side is the same.

**Proposition (two planes, not one).** On the punctured null cone the two annihilators are distinct complex planes whose intersection is the line $\mathbb{C}\tilde Q^{\natural}$.

*Proof.* Both contain $\tilde Q^{\natural}$, since $\tilde Q\tilde Q^{\natural}=\tilde Q^{\natural}\tilde Q=0$. Both have dimension $2$, so their intersection contains that line and has dimension $1$ or $2$; it is not $2$, because the two planes differ. For $\tilde Q=e_t+i\vec e_x$ the element $\tilde X=(e_t-i\vec e_x)\vec e_y/2$ satisfies $\tilde Q\tilde X=0$ but $\tilde X\tilde Q=\vec e_y-i\vec e_z\neq0$, so $\tilde X\in A(\tilde Q)\setminus B(\tilde Q)$.

**Correspondence.** The annihilator is the criterion made quantitative: it vanishes in the regular case, it is a complex plane on the punctured cone, and it is all of $\mathbb{B}$ at the origin. The two cases are the dimensions $0$ on one side and $2$, $4$ on the other.

**Remark (the $\natural$-bilinear product).** In the product $\tilde P^{\natural}\tilde Q$ the two annihilators coincide, because $(\tilde Q^{\natural}\tilde X)^{\natural}=\tilde X^{\natural}\tilde Q$ and the conjugation is injective. The coincidence is special to that product; in the plain product the two sides are genuinely two.

## The Norm on the Remarkable Subspaces

The restriction of the norm to a remarkable subspace has a realified signature, and the complex equation $N=0$ decides whether the subspace carries non-zero elements of norm zero. The values are computed in *Remarkable Subspaces under the General Quaternionic Algebra*.

| remarkable subspace | realified signature of $N$ | elements of norm zero |
|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$, the centre | $(1,1)$ | $0$ alone |
| $\mathrm{Vect}(\mathbb{B})$, the vector subspace | $(3,3)$ | the isotropic cone of the vector subspace |
| $\mathbb{H}_{\mathbb{B}}$, the quaternion subspace | $(4,0)$ | $0$ alone |
| $i\mathbb{H}_{\mathbb{B}}$, the anti-quaternion subspace | $(0,4)$ | $0$ alone |
| $\mathbb{M}_{+}$, the Hermitian subspace | $(1,3)$ | the isotropic cone of $\mathbb{M}_{+}$, all of it non-pure |
| $\mathbb{M}_{-}$, the anti-Hermitian subspace | $(3,1)$ | the isotropic cone of $\mathbb{M}_{-}$, all of it non-pure |

**Corollary.** Every non-zero element of the centre, the quaternion subspace and the anti-quaternion subspace is a unit. The vector, Hermitian and anti-Hermitian subspaces contain zero divisors, and the origin is the only element of norm zero in those subspaces that is not one.

*Proof.* The signatures give the values, and §*The Criterion* converts the values into the two statements. On the centre the norm is $Q_t^2$, which vanishes only at the origin. On a pure element the norm is $(\vec Q,\vec Q)$ and on a Hermitian element it is $|a_0|^2-|\vec b|^2$, so a zero in $\mathbb{M}_{+}$ or $\mathbb{M}_{-}$ has non-zero scalar part and is non-pure.

**Remark.** The geometry also uses one mixed real subspace, the split form $W=\operatorname{span}_{\mathbb{R}}\{e_t,\vec e_x,i\vec e_y,i\vec e_z\}$ of real dimension four, on which $N|_W=a^2+b^2-c^2-d^2$, of signature $(2,2)$.

## Summary

The biquaternion algebra carries four algebraic norms; only the quaternionic bilinear one, $N(\tilde Q)=\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^2$, is multiplicative, and only it decides invertibility.

The plain product is associative and has the two-sided unit $e_t$. The units are the elements of non-zero norm: they form the group $\mathbb{B}^{\times}$, with inverse $\tilde Q^{\natural}/N(\tilde Q)$, and the algebra is the disjoint union $\mathbb{B}=\mathbb{B}^{\times}\uplus\mathcal C$ of the units and the null cone. The group is open and dense, the cone is closed of real codimension $2$ and is its boundary. The $\natural$-bilinear product, which has a left unit and no right unit, is recorded in one remark: there the one-sided solution is $\tilde Q/N(\tilde Q)$, and the criterion is the same.

The degeneracy case is the null cone, with the origin at its apex and the zero divisors at its punctured points. The zero-divisor set splits into the pure stratum, the nilpotents of index two, of real dimension $4$, and the non-pure stratum, the non-zero complex multiples of idempotents, of real dimension $6$, the split being by the scalar part $Q_t$. In the matrix model a non-zero null element is the rank-one matrix $uv^{\mathsf T}$; its scalar part is the contraction $\tfrac12 v^{\mathsf T}u$, the pure stratum is the locus $v^{\mathsf T}u=0$, and the identity $\tilde Q^2=2Q_t\tilde Q$ is the rank-one identity $\mathsf M_2(\tilde Q)^2=(v^{\mathsf T}u)\mathsf M_2(\tilde Q)$. The cone is not a subspace and is stable under the product. The realified signature of the norm is definite on the centre, the quaternion and the anti-quaternion subspaces, and indefinite on the other three.

The annihilators are the kernels of the two translations. They vanish in the regular case, are distinct complex planes on the punctured cone, meeting in the line $\mathbb{C}\tilde Q^{\natural}$, and are all of $\mathbb{B}$ at the origin.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | the basis, $e_t$ the identity |
| $\tilde Q=Q_t e_t+\vec Q$ | an element and its scalar–vector split |
| $\tilde Q^{\natural}=Q_t-\vec Q$ | the natural conjugation |
| $\tilde P\tilde Q$ | the plain product, associative, with the two-sided unit $e_t$ |
| $N(\tilde Q)=\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^2$ | the reduced norm, the only multiplicative one of the four |
| $\langle\tilde Q\rangle=Q_t^2-Q_x^2-Q_y^2-Q_z^2$ | the general plain bilinear algebraic norm, not multiplicative |
| $\mathbb{B}^{\times}=\{\tilde Q:N(\tilde Q)\neq0\}$ | the unit group, with inverse $\tilde Q^{\natural}/N(\tilde Q)$ |
| $\mathcal C=\{\tilde Q:N=0\}$ | the null cone |
| $\mathcal Z=\mathcal C\setminus\{0\}$ | the zero-divisor set |
| $\mathcal C_{\mathrm p}=\{Q_t=0,\ \tilde Q\neq0\}$ | the pure stratum, the nilpotents of index two |
| $\mathcal C_{\mathrm{np}}=\{Q_t\neq0\}$ | the non-pure stratum, complex multiples of non-trivial idempotents |
| $\mathsf M_2(\tilde Q)=uv^{\mathsf T}$ | the rank-one factorisation of a non-zero null element |
| $A(\tilde Q)=\{\tilde X:\tilde Q\tilde X=0\}$ | the left annihilator |
| $B(\tilde Q)=\{\tilde X:\tilde X\tilde Q=0\}$ | the right annihilator |
| $\tilde P^{\natural}\tilde Q$ | the $\natural$-bilinear product, with a left unit and no right unit |
| $S(\tilde Q)=\tilde Q/N(\tilde Q)$ | the one-sided solution of that product |
| $e_t+\vec e_x$, $e_t+i\vec e_x$ | the witnesses that the plain bilinear norm decides no invertibility |

## Further Reading

- [Spectral Regularity and Degeneracy in the Biquaternion Algebra](spectral-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the second quadratic condition $B^2$, the spectral-degenerate cone and its three regimes.
- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for the norm and the one-sided inverses of a non-associative algebra.
- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, 1968), for a quadratic form defined by a product and its multiplicative law.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), for the complex-valued norm of the biquaternion algebra.
- S. J. Sangwine, T. A. Ell and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* **21** (2011) 607–636, for the norm and its axioms.
- [The Four Forms and the Four Algebraic Norms](the-four-forms-and-the-four-algebraic-norms.html), for the definition of an algebraic norm and the separation of the four.
- [Ideals and Peirce Decompositions of the Biquaternion Algebra](ideals-and-peirce-decompositions-of-the-biquaternion-algebra.html), for the minimal left ideals and the Peirce factorisation of the strata.
- [Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions](introduction-to-the-2x2-matrix-element-representation-of-biquaternions.html), for the isomorphism $\mathsf M_2$, the determinant, the trace and the rank-one elements.
- [The Biquaternion Unit Group as a Topological Group](the-biquaternion-unit-group-as-a-topological-group.html), for the topology of $\mathbb{B}^{\times}$, its maximal compact subgroup and its homotopy.
- [Zero Divisors of the General Quaternionic Algebra](zero-divisors-of-the-general-quaternionic-algebra.html), for the zero-divisor set and its criterion for the general quaternionic product.
- [Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](zero-divisors-in-the-algebraic-structures-over-the-biquaternion-c-space.html), for the comparison of the zero-divisor sets of the twelve products.
- [Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternion-c-space.html), §*The Unit and the Inverse*, for the definitions of the unit and of the one-sided inverse.
- [Remarkable Subspaces under the General Quaternionic Algebra](remarkable-subspaces-under-the-general-quaternionic-algebra.html), for the signatures of the norm on the six subspaces.
- [Annihilators of the General Quaternionic Algebra](annihilators-of-the-general-quaternionic-algebra.html), §*The Dichotomy by the Null Cone*, for the $\natural$-bilinear product, where the two annihilators coincide.
