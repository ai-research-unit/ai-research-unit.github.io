# __Biquaternion Analysis on Subspaces__

## Introduction

The article on biquaternion analysis defined limits, continuity, and the differential operators on a four-dimensional real subspace of $\mathbb{B}$. The article on biquaternion integration defined the integral and the Cauchy integral formula on the same general subspace. This article specializes the general theory to the four-dimensional subspaces of the biquaternion algebra.

The six distinguished real subspaces of $\mathbb{B}$ are the eigenspaces of its three commuting involutions. Complex conjugation ${}^{*}$ has the **quaternion subspace** $\mathbb{H}_{\mathbb{B}}$ as its $+1$ eigenspace and the **anti-quaternion subspace** $i\mathbb{H}_{\mathbb{B}}$ as its $-1$ eigenspace; Hermitian conjugation ${}^{\dagger}$ has the **Hermitian subspace** $\mathbb{M}_+$ and the **anti-Hermitian subspace** $\mathbb{M}_-$; quaternion conjugation $\bar{\cdot}$ has the two-dimensional **center** $\mathbb{C}_{\mathbb{B}}$ and the six-dimensional **vector subspace** $\mathrm{Vect}(\mathbb{B})$. Four of the six are four-dimensional — $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_-$ and $\mathbb{M}_+$ — and it is those four that carry the theory developed here. The center and the vector subspace are not domains of it: the abstract operators are defined on four-dimensional subspaces, and $\mathbb{C}_{\mathbb{B}}$ and $\mathrm{Vect}(\mathbb{B})$ are of the wrong dimension.

The specialization is not merely a matter of notation. The four subspaces have distinct **reality structures** for their complex coefficients, and this distinction propagates into the differential operators. The same abstract operator $\tilde{\nabla} = \sum_\mu e_\mu \partial/\partial Q_\mu$, when written in terms of the specific real parameters of each subspace, gives four different first-order operators. In particular, the same abstract d'Alembertian $\Box = \sum_\mu \partial^2/\partial Q_\mu^2$ takes four different specific forms, one for each subspace.

The treatment is purely mathematical. The independent variables are four real parameters, and they are independent of any physical interpretation. The complex structure of the coefficients and the non-commutative structure of the quaternion units are the only algebraic ingredients.

Every claim is either proved or stated as a definition. Where a computation is long, all steps are shown.

## The Abstract Operators and Their Specializations

The general theory of the analysis article defines the gradient on any four-dimensional real subspace $V \subset \mathbb{B}$ by

$$
\tilde{\nabla} = \sum_{\mu=0}^{3} e_\mu \frac{\partial}{\partial Q_\mu},
$$

where $Q_0, Q_1, Q_2, Q_3$ are the complex coefficients of a general element $\tilde{Q} \in V$ in the standard basis $\{e_0, e_1, e_2, e_3\}$ of $\mathbb{B}$. This is the **Cauchy–Riemann operator** of the theory (classically the Dirac operator); only its coordinate expression in the four real parameter systems changes below.

The **reality properties** of $Q_\mu$ depend on the subspace:

- On $\mathbb{H}_{\mathbb{B}}$: all $Q_\mu$ are real.
- On $i\mathbb{H}_{\mathbb{B}}$: all $Q_\mu$ are purely imaginary.
- On $\mathbb{M}_-$: $Q_0$ is purely imaginary, $Q_1, Q_2, Q_3$ are real.
- On $\mathbb{M}_+$: $Q_0$ is real, $Q_1, Q_2, Q_3$ are purely imaginary.

When $Q_\mu$ is real, $\partial/\partial Q_\mu$ is the ordinary real partial derivative with respect to that coefficient. When $Q_\mu$ is purely imaginary, $Q_\mu = i q'_\mu$ with $q'_\mu \in \mathbb{R}$, and

$$
\frac{\partial}{\partial Q_\mu} = \frac{\partial}{\partial (i q'_\mu)} = -i \frac{\partial}{\partial q'_\mu}.
$$

So the **same abstract gradient** has four different expressions in terms of the specific real parameters of the four subspaces. The same is true of every operator built from the gradient, including the d'Alembertian and the square of the gradient.

### The Abstract Second-Order Operators

Before specializing to the four subspaces, it is useful to establish the abstract second-order operators and the identities that relate them. The two natural second-order objects are:

**The d'Alembertian.** The **d'Alembertian** is the composition of the gradient with its quaternion conjugate:

$$
\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \bar{\tilde{\nabla}}\tilde{\nabla} = \sum_{\mu=0}^{3} \frac{\partial^2}{\partial Q_\mu^2}\, e_0.
$$

This is a **scalar operator** (times $e_0$). It is the natural second-order operator in the biquaternion framework: it appears in the wave equation, in the factorization of the Cauchy–Riemann operator, and in the Cauchy integral formula. In each of the four subspaces, the specific form of $\Box$ is a sum of second derivatives in the specific real parameters, with signs determined by the reality properties of the corresponding coefficients.

**The square of the gradient.** The **square of the gradient** is

$$
\tilde{\nabla}^2 = \tilde{\nabla}\tilde{\nabla} = \left(\frac{\partial^2}{\partial Q_0^2} - \Delta_Q\right) e_0 + 2\sum_{k=1}^{3} e_k \frac{\partial^2}{\partial Q_0 \partial Q_k},
$$

where $\Delta_Q = \partial^2/\partial Q_1^2 + \partial^2/\partial Q_2^2 + \partial^2/\partial Q_3^2$. This is a **biquaternion-valued operator**, with a scalar part and a vector part. It is not equal to $\Box$; its scalar part is $\partial^2/\partial Q_0^2 - \Delta_Q$, whereas $\Box$ has scalar part $\partial^2/\partial Q_0^2 + \Delta_Q$.

**The identity relating the two.** The two operators are related by

$$
\boxed{\;\tilde{\nabla}^2 = 2\,\frac{\partial}{\partial Q_0}\,\tilde{\nabla} - \Box.\;}
$$

The conjugate square satisfies the analogous identity

$$
\bar{\tilde{\nabla}}^2 = 2\,\frac{\partial}{\partial Q_0}\,\bar{\tilde{\nabla}} - \Box.
$$

The two squares are related to each other and to $\Box$ by

$$
\tilde{\nabla}^2 + \bar{\tilde{\nabla}}^2 = 2\left(\frac{\partial^2}{\partial Q_0^2} - \Delta_Q\right) e_0, \qquad \tilde{\nabla}^2 - \bar{\tilde{\nabla}}^2 = 4\sum_{k=1}^{3} e_k \frac{\partial^2}{\partial Q_0 \partial Q_k}.
$$

**Verification.** We compute directly:

$$
2\,\frac{\partial}{\partial Q_0}\,\tilde{\nabla} - \Box = 2\,\frac{\partial}{\partial Q_0}\left(e_0 \frac{\partial}{\partial Q_0} + \sum_k e_k \frac{\partial}{\partial Q_k}\right) - \left(\frac{\partial^2}{\partial Q_0^2} + \Delta_Q\right) e_0
$$

$$
= 2\,\frac{\partial^2}{\partial Q_0^2}\, e_0 + 2\sum_k e_k \frac{\partial^2}{\partial Q_0 \partial Q_k} - \frac{\partial^2}{\partial Q_0^2}\, e_0 - \Delta_Q\, e_0
$$

$$
= \left(\frac{\partial^2}{\partial Q_0^2} - \Delta_Q\right) e_0 + 2\sum_k e_k \frac{\partial^2}{\partial Q_0 \partial Q_k} = \tilde{\nabla}^2.
$$

So the identity holds. The other identities follow by conjugation and by combining.

**The status of the two operators.** The d'Alembertian $\Box$ is the natural second-order operator: it is symmetric under the exchange of $\tilde{\nabla}$ and $\bar{\tilde{\nabla}}$, it is scalar-valued, and it is the operator that appears in the standard second-order equations. The square of the gradient $\tilde{\nabla}^2$ arises when the gradient is applied twice without conjugation. It is a valid second-order operator, but it does not play the same central role. The identity above expresses it in terms of $\Box$ and the first derivative in the first coordinate, which is the natural way to write it.

## The Quaternion Subspace

### Definition

The **quaternion subspace** $\mathbb{H}_{\mathbb{B}}$ is the fixed-point set of complex conjugation:

$$
\mathbb{H}_{\mathbb{B}} = \{\tilde{Q} \in \mathbb{B} : \tilde{Q}^* = \tilde{Q}\}.
$$

Explicitly, a biquaternion is in $\mathbb{H}_{\mathbb{B}}$ if and only if it has the form

$$
\tilde{Q} = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3, \qquad q_0, q_1, q_2, q_3 \in \mathbb{R}.
$$

All four coefficients are real. The subset $\mathbb{H}_{\mathbb{B}}$ is a real vector space of dimension 4, and it is a subalgebra of $\mathbb{B}$ isomorphic to the quaternion algebra $\mathbb{H}$.

### Properties

**Real vector space.** $\mathbb{H}_{\mathbb{B}}$ is a real vector space of dimension 4. A basis is $\{e_0, e_1, e_2, e_3\}$.

**Subalgebra.** $\mathbb{H}_{\mathbb{B}}$ is closed under biquaternion multiplication.

**Division algebra.** $\mathbb{H}_{\mathbb{B}}$ is a division algebra. The norm form restricts to a positive-definite quadratic form:

$$
N(\tilde{Q}) = \tilde{Q} \bar{\tilde{Q}} = q_0^2 + q_1^2 + q_2^2 + q_3^2.
$$

This vanishes if and only if all $q_\mu = 0$. So every nonzero element of $\mathbb{H}_{\mathbb{B}}$ is invertible, and $\mathbb{H}_{\mathbb{B}}$ contains no zero divisors.

**Coordinates.** The complex coefficients of $\tilde{Q}$ take the form $Q_\mu = q_\mu$, all real. The four real parameters $q_0, q_1, q_2, q_3$ are the **coordinates** of $\tilde{Q}$ in $\mathbb{H}_{\mathbb{B}}$.

### Functions on the Quaternion Subspace

A **biquaternion-valued function on the quaternion subspace** is a map

$$
\tilde{F} : \mathbb{H}_{\mathbb{B}} \to \mathbb{B}, \qquad \tilde{Q} \mapsto \tilde{F}(\tilde{Q}).
$$

In the specific coordinates,

$$
\tilde{F}(\tilde{Q}) = F_0(q_0, q_1, q_2, q_3) e_0 + F_1(q_0, q_1, q_2, q_3) e_1 + F_2(q_0, q_1, q_2, q_3) e_2 + F_3(q_0, q_1, q_2, q_3) e_3.
$$

### The Specific Differential Operators on $\mathbb{H}_{\mathbb{B}}$

All four complex coefficients of $\tilde{Q} \in \mathbb{H}_{\mathbb{B}}$ are real, so all partial derivatives are ordinary real partial derivatives:

$$
\frac{\partial}{\partial Q_0} = \frac{\partial}{\partial q_0}, \qquad \frac{\partial}{\partial Q_k} = \frac{\partial}{\partial q_k}.
$$

**The gradient.** The specific biquaternionic gradient on $\mathbb{H}_{\mathbb{B}}$ is

$$
\tilde{\nabla} = e_0 \frac{\partial}{\partial q_0} + e_1 \frac{\partial}{\partial q_1} + e_2 \frac{\partial}{\partial q_2} + e_3 \frac{\partial}{\partial q_3} = \sum_{\mu=0}^{3} e_\mu \frac{\partial}{\partial q_\mu}.
$$

It acts on $\tilde{F}$ by the rule

$$
\tilde{\nabla}\tilde{F} = \left(\frac{\partial F_0}{\partial q_0} - \mathrm{div}_{\mathbb{H}}\,\mathbf{F}\right) + \left(\frac{\partial \mathbf{F}}{\partial q_0} + \mathrm{grad}_{\mathbb{H}}\,F_0 + \mathrm{rot}_{\mathbb{H}}\,\mathbf{F}\right),
$$

where

$$
\mathrm{div}_{\mathbb{H}}\,\mathbf{F} = \sum_{k=1}^{3} \frac{\partial F_k}{\partial q_k}, \quad \mathrm{grad}_{\mathbb{H}}\,F_0 = \sum_{k=1}^{3} \left(\frac{\partial F_0}{\partial q_k}\right) e_k, \quad \mathrm{rot}_{\mathbb{H}}\,\mathbf{F} = \sum_{j,k,l=1}^{3} \epsilon_{jkl} \left(\frac{\partial F_k}{\partial q_j}\right) e_l.
$$

**The quaternion conjugate of the gradient.** The quaternion conjugate is

$$
\bar{\tilde{\nabla}} = e_0 \frac{\partial}{\partial q_0} - e_1 \frac{\partial}{\partial q_1} - e_2 \frac{\partial}{\partial q_2} - e_3 \frac{\partial}{\partial q_3}.
$$

**The d'Alembertian.** The **specific d'Alembertian on $\mathbb{H}_{\mathbb{B}}$** is

$$
\Box_{\mathbb{H}} = \tilde{\nabla}\bar{\tilde{\nabla}} = \bar{\tilde{\nabla}}\tilde{\nabla} = \left(\frac{\partial^2}{\partial q_0^2} + \frac{\partial^2}{\partial q_1^2} + \frac{\partial^2}{\partial q_2^2} + \frac{\partial^2}{\partial q_3^2}\right) e_0.
$$

This is the **four-dimensional Euclidean Laplacian** in the real coordinates $(q_0, q_1, q_2, q_3)$. All four directions contribute with the **same sign**, and the signature of the quadratic form is $(4, 0)$.

**The square of the gradient.** The **square of the gradient on $\mathbb{H}_{\mathbb{B}}$** is

$$
\tilde{\nabla}^2 = \left(\frac{\partial^2}{\partial q_0^2} - \Delta_{\mathbb{H}}\right) + 2\sum_{k=1}^{3} e_k \frac{\partial^2}{\partial q_0 \partial q_k},
$$

where $\Delta_{\mathbb{H}} = \partial^2/\partial q_1^2 + \partial^2/\partial q_2^2 + \partial^2/\partial q_3^2$. Using the identity established above, it can also be written as

$$
\tilde{\nabla}^2 = 2\,\frac{\partial}{\partial q_0}\,\tilde{\nabla} - \Box_{\mathbb{H}}.
$$

The scalar part is $\partial_{q_0}^2 - \Delta_{\mathbb{H}}$; the vector part is $2\sum_k e_k \partial_{q_0}\partial_{q_k}$.

**The convective derivative.** For a biquaternion $\tilde{U} = \sum_\mu u_\mu e_\mu$ with $u_\mu \in \mathbb{R}$, the convective derivative is

$$
\tilde{D} = \bar{\tilde{U}} \tilde{\nabla} = \left(u_0 \frac{\partial}{\partial q_0} + \sum_{k=1}^{3} u_k \frac{\partial}{\partial q_k}\right) + \sum_{k=1}^{3} e_k \left(u_0 \frac{\partial}{\partial q_k} - u_k \frac{\partial}{\partial q_0}\right) - \sum_{j,k,l=1}^{3} \epsilon_{jkl} \, u_j \frac{\partial}{\partial q_k} e_l.
$$

The last term is **operator-valued**: the derivatives $\partial_{q_k}$ act on a function to the right, and the constant vector $\mathbf{u} = (u_1, u_2, u_3)$ supplies the coefficients. This term is *not* the same as the curl $\mathrm{rot}_{\mathbb{H}}\,\mathbf{F}$ of a biquaternion-valued function $\mathbf{F}$ defined above: $\mathrm{rot}_{\mathbb{H}}\,\mathbf{F}$ acts on the coefficient functions $F_k$ of $\mathbf{F}$, whereas the term here uses the constants $u_j$ and leaves the derivatives to act on a function that has not yet been specified.

### Integration on $\mathbb{H}_{\mathbb{B}}$

The integral of $\tilde{F}$ over a domain $\Omega \subset \mathbb{H}_{\mathbb{B}}$ is defined component-wise in the real parameters $(q_0, q_1, q_2, q_3)$:

$$
\int_\Omega \tilde{F} \, dV = \sum_{\mu=0}^{3} \left(\int_\Omega F_\mu \, dV\right) e_\mu.
$$

The divergence theorem, Green's formulas, and the Cauchy integral formula all hold. The **Cauchy kernel** — a constant multiple of the fundamental solution of the first-order gradient operator $\tilde{\nabla}$ — is

$$
\tilde{G}(\tilde{Q}) = \frac{\bar{\tilde{Q}}}{\|\tilde{Q}\|_E^4} = \frac{q_0 e_0 - \sum_k q_k e_k}{\left(\sum_\mu q_\mu^2\right)^2}.
$$

Here $\tilde{G}$ is the fundamental solution of the **first-order** operator $\tilde{\nabla}$: in the sense of distributions, $\tilde{\nabla}\tilde{G}$ is a multiple of the delta distribution at the origin. It is *not* the fundamental solution of the second-order d'Alembertian $\Box_{\mathbb{H}}$; on $\mathbb{H}_{\mathbb{B}} \cong \mathbb{R}^4$, the fundamental solution of the Euclidean Laplacian scales as $\|\tilde{Q}\|_E^{-2}$. Since $\mathbb{H}_{\mathbb{B}}$ contains no zero divisors, the analysis is clean everywhere on $\mathbb{H}_{\mathbb{B}}$ except at the origin $\tilde{Q} = 0$, which is the singularity of the kernel.

## The Anti-Quaternion Subspace

### Definition

The **anti-quaternion subspace** $i\mathbb{H}_{\mathbb{B}}$ is the anti-fixed-point set of complex conjugation:

$$
i\mathbb{H}_{\mathbb{B}} = \{\tilde{Q} \in \mathbb{B} : \tilde{Q}^{*} = -\tilde{Q}\} = i\,\mathbb{H}_{\mathbb{B}}.
$$

Explicitly, a biquaternion is in $i\mathbb{H}_{\mathbb{B}}$ if and only if it has the form

$$
\tilde{Q} = i q'_0\, e_0 + i q'_1\, e_1 + i q'_2\, e_2 + i q'_3\, e_3, \qquad q'_0, q'_1, q'_2, q'_3 \in \mathbb{R}.
$$

All four coefficients are purely imaginary. The subset $i\mathbb{H}_{\mathbb{B}}$ is a real vector space of dimension 4 with basis $\{i e_0, i e_1, i e_2, i e_3\}$, and it is the set of products $i\tilde{P}$ with $\tilde{P} \in \mathbb{H}_{\mathbb{B}}$.

### Properties

**Real vector space.** $i\mathbb{H}_{\mathbb{B}}$ is a real vector space of dimension 4. A basis is $\{i e_0, i e_1, i e_2, i e_3\}$.

**Module, not subalgebra.** $i\mathbb{H}_{\mathbb{B}}$ is not closed under biquaternion multiplication: $(i e_\mu)(i e_\nu) = -e_\mu e_\nu$ lies in $\mathbb{H}_{\mathbb{B}}$, not in $i\mathbb{H}_{\mathbb{B}}$, whenever the product is nonzero. It is a two-sided module over the quaternion subspace: for real quaternions $\tilde{P}, \tilde{Q}$ one has $(i\tilde{P})\tilde{Q} = i(\tilde{P}\tilde{Q})$ and $\tilde{Q}(i\tilde{P}) = i(\tilde{Q}\tilde{P})$, both in $i\mathbb{H}_{\mathbb{B}}$.

**Quadratic form.** The norm form restricts to a **negative-definite** quadratic form:

$$
N(\tilde{Q}) = \tilde{Q} \bar{\tilde{Q}} = -(q'_0)^2 - (q'_1)^2 - (q'_2)^2 - (q'_3)^2.
$$

This vanishes if and only if all $q'_\mu = 0$. The signature is $(0, 4)$: all four directions contribute with the same sign, negative. It is the mirror image of the Euclidean form on $\mathbb{H}_{\mathbb{B}}$, in the same sense in which the form on $\mathbb{M}_+$ mirrors the form on $\mathbb{M}_-$.

**No zero divisors.** Since $N(\tilde{Q})$ never vanishes on a nonzero element, $i\mathbb{H}_{\mathbb{B}}$ contains no zero divisors. Like $\mathbb{H}_{\mathbb{B}}$, and unlike the two indefinite subspaces $\mathbb{M}_-$ and $\mathbb{M}_+$, it carries no cone of singular elements.

**Coordinates.** The complex coefficients of $\tilde{Q}$ take the form $Q_\mu = iq'_\mu$, all purely imaginary. The four real parameters $q'_0, q'_1, q'_2, q'_3$ are the **coordinates** of $\tilde{Q}$ in $i\mathbb{H}_{\mathbb{B}}$.

**The central rotation.** Multiplication by the central scalar $i$ is a bijection of the subspace onto the quaternion subspace: $\tilde{P} \mapsto i\tilde{P}$ maps $\mathbb{H}_{\mathbb{B}}$ onto $i\mathbb{H}_{\mathbb{B}}$, with inverse $\tilde{Q} \mapsto -i\tilde{Q}$. Because $i$ commutes with every element of $\mathbb{B}$, this bijection carries each operator built from the quaternion units into the corresponding operator; the only structure it changes is the sign of the norm form, $N(i\tilde{P}) = -N(\tilde{P})$. The analysis on $i\mathbb{H}_{\mathbb{B}}$ is therefore the analysis on $\mathbb{H}_{\mathbb{B}}$ seen through the central rotation, with $\Box$ replaced by $-\Box$, and the explicit forms below record this. The same remark applies with the same force to the pair $\mathbb{M}_-$ and $\mathbb{M}_+$, which is exchanged by the same central rotation.

### Functions on the Anti-Quaternion Subspace

A **biquaternion-valued function on the anti-quaternion subspace** is a map

$$
\tilde{F} : i\mathbb{H}_{\mathbb{B}} \to \mathbb{B}, \qquad \tilde{Q} \mapsto \tilde{F}(\tilde{Q}).
$$

In the specific coordinates,

$$
\tilde{F}(\tilde{Q}) = F_0(q'_0, q'_1, q'_2, q'_3) e_0 + F_1(q'_0, q'_1, q'_2, q'_3) e_1 + F_2(q'_0, q'_1, q'_2, q'_3) e_2 + F_3(q'_0, q'_1, q'_2, q'_3) e_3.
$$

### The Specific Differential Operators on $i\mathbb{H}_{\mathbb{B}}$

All four complex coefficients of $\tilde{Q} \in i\mathbb{H}_{\mathbb{B}}$ are purely imaginary, so every partial derivative carries the factor $-i$:

$$
\frac{\partial}{\partial Q_\mu} = \frac{\partial}{\partial (i q'_\mu)} = -i \frac{\partial}{\partial q'_\mu}, \qquad \mu = 0, 1, 2, 3.
$$

**The gradient.** The specific biquaternionic gradient on $i\mathbb{H}_{\mathbb{B}}$ is

$$
\tilde{\nabla} = -i\, e_0 \frac{\partial}{\partial q'_0} - i\, e_1 \frac{\partial}{\partial q'_1} - i\, e_2 \frac{\partial}{\partial q'_2} - i\, e_3 \frac{\partial}{\partial q'_3} = -i \sum_{\mu=0}^{3} e_\mu \frac{\partial}{\partial q'_\mu}.
$$

All four components carry the same factor $-i$. The operator is $-i$ times the gradient on $\mathbb{H}_{\mathbb{B}}$, written in the coordinates $q'_\mu$.

**The quaternion conjugate of the gradient.** The quaternion conjugate is

$$
\bar{\tilde{\nabla}} = -i\, e_0 \frac{\partial}{\partial q'_0} + i\, e_1 \frac{\partial}{\partial q'_1} + i\, e_2 \frac{\partial}{\partial q'_2} + i\, e_3 \frac{\partial}{\partial q'_3}.
$$

**The d'Alembertian.** The **specific d'Alembertian on $i\mathbb{H}_{\mathbb{B}}$** is

$$
\Box_{i\mathbb{H}} = \tilde{\nabla}\bar{\tilde{\nabla}} = \bar{\tilde{\nabla}}\tilde{\nabla} = -\left(\frac{\partial^2}{\partial {q'_0}^2} + \frac{\partial^2}{\partial {q'_1}^2} + \frac{\partial^2}{\partial {q'_2}^2} + \frac{\partial^2}{\partial {q'_3}^2}\right) e_0.
$$

This is the **negative four-dimensional Euclidean Laplacian** in the coordinates $(q'_0, q'_1, q'_2, q'_3)$. All four directions contribute with the same sign, and the signature is $(0, 4)$ — the mirror image of the signature $(4, 0)$ on $\mathbb{H}_{\mathbb{B}}$, to which it is related by $\Box_{i\mathbb{H}} = -\,\Box_{\mathbb{H}}$ under the central rotation.

**The square of the gradient.** The **square of the gradient on $i\mathbb{H}_{\mathbb{B}}$** is

$$
\tilde{\nabla}^2 = -\left(\frac{\partial^2}{\partial {q'_0}^2} - \Delta_{i\mathbb{H}}\right) - 2\sum_{k=1}^{3} e_k \frac{\partial^2}{\partial q'_0 \partial q'_k},
$$

where $\Delta_{i\mathbb{H}} = \partial^2/\partial {q'_1}^2 + \partial^2/\partial {q'_2}^2 + \partial^2/\partial {q'_3}^2$. Using the identity established above, it can also be written as

$$
\tilde{\nabla}^2 = -2i\,\frac{\partial}{\partial q'_0}\,\tilde{\nabla} - \Box_{i\mathbb{H}}.
$$

The scalar part is $-\partial_{q'_0}^2 + \Delta_{i\mathbb{H}}$; the vector part is $-2\sum_k e_k \partial_{q'_0}\partial_{q'_k}$.

**The convective derivative.** For a biquaternion $\tilde{U} = \sum_\mu u_\mu e_\mu$ with $u_\mu \in \mathbb{R}$, the convective derivative is

$$
\tilde{D} = \bar{\tilde{U}} \tilde{\nabla} = -i\, \bar{\tilde{U}} \left(\sum_{\mu=0}^{3} e_\mu \frac{\partial}{\partial q'_\mu}\right),
$$

that is, the same differential operator as on $\mathbb{H}_{\mathbb{B}}$, with the same coefficients, multiplied by $-i$.

### Integration on $i\mathbb{H}_{\mathbb{B}}$

The integral of $\tilde{F}$ over a domain $\Omega \subset i\mathbb{H}_{\mathbb{B}}$ is defined component-wise in the real parameters $(q'_0, q'_1, q'_2, q'_3)$:

$$
\int_\Omega \tilde{F} \, dV = \sum_{\mu=0}^{3} \left(\int_\Omega F_\mu \, dV\right) e_\mu.
$$

The **Cauchy kernel** — a constant multiple of the fundamental solution of the first-order gradient operator $\tilde{\nabla}$ — is

$$
\tilde{G}(\tilde{Q}) = \frac{\bar{\tilde{Q}}}{\|\tilde{Q}\|_E^4} = \frac{i q'_0 e_0 - i\sum_k q'_k e_k}{\left(\sum_\mu {q'_\mu}^2\right)^2}.
$$

It is the fundamental solution of the **first-order** operator $\tilde{\nabla}$, not of the second-order d'Alembertian. Since $i\mathbb{H}_{\mathbb{B}}$ has no zero divisors, the kernel is defined everywhere except at the origin $\tilde{Q} = 0$, exactly as on $\mathbb{H}_{\mathbb{B}}$; it is $i$ times the Euclidean kernel evaluated at the same coordinates.

## The Anti-Hermitian Subspace

### Definition

The **anti-Hermitian subspace** $\mathbb{M}_-$ is the fixed-point set of anti-Hermitian conjugation:

$$
\mathbb{M}_- = \{\tilde{Q} \in \mathbb{B} : \tilde{Q}^\flat = \tilde{Q}\},
$$

where $\tilde{Q}^\flat = -\bar{\tilde{Q}}^*$. Explicitly, a biquaternion is in $\mathbb{M}_-$ if and only if it has the form

$$
\tilde{Q} = i q'_0\, e_0 + q_1\, e_1 + q_2\, e_2 + q_3\, e_3, \qquad q'_0, q_1, q_2, q_3 \in \mathbb{R}.
$$

The scalar part is purely imaginary, and the vector part is real. The subset $\mathbb{M}_-$ is a real vector space of dimension 4.

### Properties

**Real vector space.** $\mathbb{M}_-$ is a real vector space of dimension 4. A basis is $\{i e_0, e_1, e_2, e_3\}$.

**Not a subalgebra.** $\mathbb{M}_-$ is not closed under biquaternion multiplication. For example, $(i e_0) \circ (i e_0) = -e_0$, which is not in $\mathbb{M}_-$.

**Quadratic form.** The biquaternion norm form restricts to a real quadratic form on $\mathbb{M}_-$:

$$
N(\tilde{Q}) = \tilde{Q} \bar{\tilde{Q}} = -(q'_0)^2 + q_1^2 + q_2^2 + q_3^2.
$$

This quadratic form has signature $(3, 1)$: three positive directions (the coefficients $q_1, q_2, q_3$) and one negative direction (the coefficient $q'_0$). It vanishes on a three-dimensional cone, the set of zero divisors in $\mathbb{M}_-$.

**Coordinates.** The complex coefficients of $\tilde{Q}$ take the form

$$
Q_0 = i q'_0, \qquad Q_1 = q_1, \qquad Q_2 = q_2, \qquad Q_3 = q_3.
$$

The first coefficient is **purely imaginary**, and the three remaining coefficients are **real**. The four real parameters $q'_0, q_1, q_2, q_3$ are the **coordinates** of $\tilde{Q}$ in $\mathbb{M}_-$.

### Functions on the Anti-Hermitian Subspace

A **biquaternion-valued function on the anti-Hermitian subspace** is a map

$$
\tilde{F} : \mathbb{M}_- \to \mathbb{B}, \qquad \tilde{Q} \mapsto \tilde{F}(\tilde{Q}).
$$

In the specific coordinates,

$$
\tilde{F}(\tilde{Q}) = F_0(q'_0, q_1, q_2, q_3) e_0 + F_1(q'_0, q_1, q_2, q_3) e_1 + F_2(q'_0, q_1, q_2, q_3) e_2 + F_3(q'_0, q_1, q_2, q_3) e_3.
$$

### The Specific Differential Operators on $\mathbb{M}_-$

On $\mathbb{M}_-$, the first complex coefficient is imaginary, and the three remaining coefficients are real. The partial derivatives are therefore

$$
\frac{\partial}{\partial Q_0} = \frac{\partial}{\partial (i q'_0)} = -i \frac{\partial}{\partial q'_0}, \qquad \frac{\partial}{\partial Q_k} = \frac{\partial}{\partial q_k}.
$$

The $-i$ factor is on the coefficient $Q_0$ because it is imaginary.

**The gradient.** The specific biquaternionic gradient on $\mathbb{M}_-$ is

$$
\tilde{\nabla} = -i\, e_0 \frac{\partial}{\partial q'_0} + e_1 \frac{\partial}{\partial q_1} + e_2 \frac{\partial}{\partial q_2} + e_3 \frac{\partial}{\partial q_3}.
$$

The first component of the gradient is purely imaginary (coefficient $-i$), and the three remaining components are real.

**The quaternion conjugate of the gradient.** The quaternion conjugate is

$$
\bar{\tilde{\nabla}} = -i\, e_0 \frac{\partial}{\partial q'_0} - e_1 \frac{\partial}{\partial q_1} - e_2 \frac{\partial}{\partial q_2} - e_3 \frac{\partial}{\partial q_3}.
$$

**The d'Alembertian.** The **specific d'Alembertian on $\mathbb{M}_-$** is

$$
\Box_{\mathbb{M}_-} = \tilde{\nabla}\bar{\tilde{\nabla}} = \bar{\tilde{\nabla}}\tilde{\nabla} = \left(-\frac{\partial^2}{\partial {q'_0}^2} + \frac{\partial^2}{\partial q_1^2} + \frac{\partial^2}{\partial q_2^2} + \frac{\partial^2}{\partial q_3^2}\right) e_0.
$$

This is a **second-order differential operator with signature** $(3, 1)$: three of the coordinates contribute with positive sign and the coordinate $q'_0$ contributes with negative sign. It is the **mirror** of the operator on $\mathbb{M}_+$.

**The square of the gradient.** The **square of the gradient on $\mathbb{M}_-$** is

$$
\tilde{\nabla}^2 = -\left(\frac{\partial^2}{\partial {q'_0}^2} + \Delta_{\mathbb{M}_-}\right) - 2i\sum_{k=1}^{3} e_k \frac{\partial^2}{\partial q'_0 \partial q_k},
$$

where $\Delta_{\mathbb{M}_-} = \partial^2/\partial q_1^2 + \partial^2/\partial q_2^2 + \partial^2/\partial q_3^2$. Using the identity established above, it can also be written as

$$
\tilde{\nabla}^2 = -2i\,\frac{\partial}{\partial q'_0}\,\tilde{\nabla} - \Box_{\mathbb{M}_-}.
$$

The scalar part is $-\partial_{q'_0}^2 - \Delta_{\mathbb{M}_-}$; the vector part is $-2i\sum_k e_k \partial_{q'_0}\partial_{q_k}$.

**The convective derivative.** For a biquaternion $\tilde{U} = \sum_\mu u_\mu e_\mu$ with $u_\mu \in \mathbb{R}$, the convective derivative is

$$
\tilde{D} = \bar{\tilde{U}} \tilde{\nabla} = \left(-i u_0 \frac{\partial}{\partial q'_0} + \sum_{k=1}^{3} u_k \frac{\partial}{\partial q_k}\right) + \sum_{k=1}^{3} e_k \left(u_0 \frac{\partial}{\partial q_k} + i u_k \frac{\partial}{\partial q'_0}\right) - \sum_{j,k,l=1}^{3} \epsilon_{jkl} \, u_j \frac{\partial}{\partial q_k} e_l.
$$

The last term is operator-valued, with the same meaning as on $\mathbb{H}_{\mathbb{B}}$: the derivatives $\partial_{q_k}$ act on a function to the right, and the constants $u_j$ provide the coefficients.

### Integration on $\mathbb{M}_-$

The integral of $\tilde{F}$ over a domain $\Omega \subset \mathbb{M}_-$ is defined component-wise in the real parameters $(q'_0, q_1, q_2, q_3)$:

$$
\int_\Omega \tilde{F} \, dV = \sum_{\mu=0}^{3} \left(\int_\Omega F_\mu \, dV\right) e_\mu.
$$

The Cauchy kernel — a constant multiple of the fundamental solution of the first-order gradient operator on $\mathbb{M}_-$ — is

$$
\tilde{G}(\tilde{Q}) = \frac{\bar{\tilde{Q}}}{\|\tilde{Q}\|_E^4} = \frac{i q'_0 e_0 - \sum_k q_k e_k}{\left((q'_0)^2 + \sum_k q_k^2\right)^2}.
$$

As on $\mathbb{H}_{\mathbb{B}}$, this is the fundamental solution of $\tilde{\nabla}$, not of the second-order d'Alembertian.

### The Role of the Zero Divisor Cone

On $\mathbb{M}_-$, the zero divisors form a three-dimensional cone $\mathcal{C}$ defined by

$$
(q'_0)^2 = q_1^2 + q_2^2 + q_3^2
$$

in the coordinates $(q'_0, q_1, q_2, q_3)$ of $\mathbb{M}_-$. On the complement of the cone, the analysis is clean. On the cone itself, the function $\tilde{G}$ is undefined at the apex; on the rest of the cone, $\tilde{G}$ remains finite but takes zero-divisor values, since the element $\tilde{Q}$ is itself a zero divisor and the algebra structure degenerates there. The kernel does not blow up away from the apex; what fails on the cone (away from the origin) is the invertibility of $\tilde{Q}$.

## The Hermitian Subspace

### Definition

The **Hermitian subspace** $\mathbb{M}_+$ is the fixed-point set of Hermitian conjugation:

$$
\mathbb{M}_+ = \{\tilde{Q} \in \mathbb{B} : \tilde{Q}^\dagger = \tilde{Q}\}.
$$

Explicitly, a biquaternion is in $\mathbb{M}_+$ if and only if it has the form

$$
\tilde{Q} = q_0\, e_0 + i q'_1\, e_1 + i q'_2\, e_2 + i q'_3\, e_3, \qquad q_0, q'_1, q'_2, q'_3 \in \mathbb{R}.
$$

The scalar part is real, and the vector part is purely imaginary. The subset $\mathbb{M}_+$ is a real vector space of dimension 4.

### Properties

**Real vector space.** $\mathbb{M}_+$ is a real vector space of dimension 4. A basis is $\{e_0, i e_1, i e_2, i e_3\}$.

**Not a subalgebra.** $\mathbb{M}_+$ is not closed under biquaternion multiplication. For example, $(i e_1) \circ (i e_2) = -e_3$, which is not in $\mathbb{M}_+$.

**Quadratic form.** The biquaternion norm form restricts to a real quadratic form on $\mathbb{M}_+$:

$$
N(\tilde{Q}) = \tilde{Q} \bar{\tilde{Q}} = q_0^2 - (q'_1)^2 - (q'_2)^2 - (q'_3)^2.
$$

This quadratic form has signature $(1, 3)$: one positive direction (the coefficient $q_0$) and three negative directions (the coefficients $q'_1, q'_2, q'_3$). It is the **mirror image** of the form on $\mathbb{M}_-$: the roles of the first and the remaining coefficients are interchanged. It vanishes on a three-dimensional cone, the set of zero divisors in $\mathbb{M}_+$.

**Coordinates.** The complex coefficients of $\tilde{Q}$ take the form

$$
Q_0 = q_0, \qquad Q_1 = i q'_1, \qquad Q_2 = i q'_2, \qquad Q_3 = i q'_3.
$$

The first coefficient is **real**, and the three remaining coefficients are **purely imaginary**. The four real parameters $q_0, q'_1, q'_2, q'_3$ are the **coordinates** of $\tilde{Q}$ in $\mathbb{M}_+$.

### Functions on the Hermitian Subspace

A **biquaternion-valued function on the Hermitian subspace** is a map

$$
\tilde{F} : \mathbb{M}_+ \to \mathbb{B}, \qquad \tilde{Q} \mapsto \tilde{F}(\tilde{Q}).
$$

In the specific coordinates,

$$
\tilde{F}(\tilde{Q}) = F_0(q_0, q'_1, q'_2, q'_3) e_0 + F_1(q_0, q'_1, q'_2, q'_3) e_1 + F_2(q_0, q'_1, q'_2, q'_3) e_2 + F_3(q_0, q'_1, q'_2, q'_3) e_3.
$$

### The Specific Differential Operators on $\mathbb{M}_+$

On $\mathbb{M}_+$, the first complex coefficient is real, and the three remaining coefficients are imaginary. The partial derivatives are therefore

$$
\frac{\partial}{\partial Q_0} = \frac{\partial}{\partial q_0}, \qquad \frac{\partial}{\partial Q_k} = \frac{\partial}{\partial (i q'_k)} = -i \frac{\partial}{\partial q'_k}.
$$

The $-i$ factor is now on the three remaining coordinates, mirroring the situation on $\mathbb{M}_-$.

**The gradient.** The specific biquaternionic gradient on $\mathbb{M}_+$ is

$$
\tilde{\nabla} = e_0 \frac{\partial}{\partial q_0} - i\, e_1 \frac{\partial}{\partial q'_1} - i\, e_2 \frac{\partial}{\partial q'_2} - i\, e_3 \frac{\partial}{\partial q'_3}.
$$

The first component is real (coefficient $+1$), and the three remaining components are purely imaginary (coefficient $-i$).

**The quaternion conjugate of the gradient.** The quaternion conjugate is

$$
\bar{\tilde{\nabla}} = e_0 \frac{\partial}{\partial q_0} + i\, e_1 \frac{\partial}{\partial q'_1} + i\, e_2 \frac{\partial}{\partial q'_2} + i\, e_3 \frac{\partial}{\partial q'_3}.
$$

**The d'Alembertian.** The **specific d'Alembertian on $\mathbb{M}_+$** is

$$
\Box_{\mathbb{M}_+} = \tilde{\nabla}\bar{\tilde{\nabla}} = \bar{\tilde{\nabla}}\tilde{\nabla} = \left(\frac{\partial^2}{\partial q_0^2} - \frac{\partial^2}{\partial {q'_1}^2} - \frac{\partial^2}{\partial {q'_2}^2} - \frac{\partial^2}{\partial {q'_3}^2}\right) e_0.
$$

This is a **second-order differential operator with signature** $(1, 3)$: the coordinate $q_0$ contributes with positive sign and the three coordinates $q'_1, q'_2, q'_3$ contribute with negative sign. It is the mirror image of the operator on $\mathbb{M}_-$.

**The square of the gradient.** The **square of the gradient on $\mathbb{M}_+$** is

$$
\tilde{\nabla}^2 = \left(\frac{\partial^2}{\partial q_0^2} + \Delta_{\mathbb{M}_+}\right) - 2i\sum_{k=1}^{3} e_k \frac{\partial^2}{\partial q_0 \partial q'_k},
$$

where $\Delta_{\mathbb{M}_+} = \partial^2/\partial {q'_1}^2 + \partial^2/\partial {q'_2}^2 + \partial^2/\partial {q'_3}^2$. Using the identity established above, it can also be written as

$$
\tilde{\nabla}^2 = 2\,\frac{\partial}{\partial q_0}\,\tilde{\nabla} - \Box_{\mathbb{M}_+}.
$$

The scalar part is $\partial_{q_0}^2 + \Delta_{\mathbb{M}_+}$; the vector part is $-2i\sum_k e_k \partial_{q_0}\partial_{q'_k}$.

**The convective derivative.** For a biquaternion $\tilde{U} = \sum_\mu u_\mu e_\mu$ with $u_\mu \in \mathbb{R}$, the convective derivative is

$$
\tilde{D} = \bar{\tilde{U}} \tilde{\nabla} = \left(u_0 \frac{\partial}{\partial q_0} - i \sum_{k=1}^{3} u_k \frac{\partial}{\partial q'_k}\right) + \sum_{k=1}^{3} e_k \left(-i u_0 \frac{\partial}{\partial q'_k} - u_k \frac{\partial}{\partial q_0}\right) + i \sum_{j,k,l=1}^{3} \epsilon_{jkl} \, u_j \frac{\partial}{\partial q'_k} e_l.
$$

The last term is operator-valued. Note the appearance of the factor $i$ and the derivative $\partial_{q'_k}$, reflecting the imaginary character of the spatial coordinates on $\mathbb{M}_+$. In particular, this term is not the negative of the corresponding term on $\mathbb{M}_-$, but differs by the factor $i$ and by which coordinates appear.

### Integration on $\mathbb{M}_+$

The integral of $\tilde{F}$ over a domain $\Omega \subset \mathbb{M}_+$ is defined component-wise in the real parameters $(q_0, q'_1, q'_2, q'_3)$:

$$
\int_\Omega \tilde{F} \, dV = \sum_{\mu=0}^{3} \left(\int_\Omega F_\mu \, dV\right) e_\mu.
$$

The Cauchy kernel — a constant multiple of the fundamental solution of the first-order gradient operator on $\mathbb{M}_+$ — is

$$
\tilde{G}(\tilde{Q}) = \frac{\bar{\tilde{Q}}}{\|\tilde{Q}\|_E^4} = \frac{q_0 e_0 - i\sum_k q'_k e_k}{\left(q_0^2 + \sum_k {q'_k}^2\right)^2}.
$$

As on $\mathbb{H}_{\mathbb{B}}$ and $\mathbb{M}_-$, this is the fundamental solution of $\tilde{\nabla}$, not of the second-order d'Alembertian.

### The Role of the Zero Divisor Cone

On $\mathbb{M}_+$, the zero divisors form a three-dimensional cone defined by

$$
q_0^2 = (q'_1)^2 + (q'_2)^2 + (q'_3)^2
$$

in the coordinates $(q_0, q'_1, q'_2, q'_3)$ of $\mathbb{M}_+$. The cone is the mirror image of the cone on $\mathbb{M}_-$: the first and the remaining coordinates are interchanged. As on $\mathbb{M}_-$, the Cauchy kernel is undefined at the apex and takes zero-divisor values on the rest of the cone, where the algebra structure degenerates because $\tilde{Q}$ has no inverse.

## Comparison of the Four Subspaces

The four subspaces are all real vector spaces of dimension 4. Their algebraic properties differ, and the **specific forms** of the differential operators differ in a characteristic way.

| Property | $\mathbb{H}_{\mathbb{B}}$ | $i\mathbb{H}_{\mathbb{B}}$ | $\mathbb{M}_-$ | $\mathbb{M}_+$ |
|---|---|---|---|---|
| Definition | Fixed-point set of $^*$ | Anti-fixed-point set of $^*$ | Fixed-point set of $\flat$ | Fixed-point set of $\dagger$ |
| Basis | $\{e_0, e_1, e_2, e_3\}$ | $\{i e_0, i e_1, i e_2, i e_3\}$ | $\{i e_0, e_1, e_2, e_3\}$ | $\{e_0, i e_1, i e_2, i e_3\}$ |
| Coordinates | $q_0, q_k$ | $q'_0, q'_k$ | $q'_0, q_k$ | $q_0, q'_k$ |
| $Q_0$ | $q_0$ (real) | $i q'_0$ (imaginary) | $i q'_0$ (imaginary) | $q_0$ (real) |
| $Q_k$ | $q_k$ (real) | $i q'_k$ (imaginary) | $q_k$ (real) | $i q'_k$ (imaginary) |
| Norm form | $q_0^2 + q_1^2 + q_2^2 + q_3^2$ | $-\sum_\mu {q'_\mu}^2$ | $-(q'_0)^2 + \sum_k q_k^2$ | $q_0^2 - \sum_k {q'_k}^2$ |
| Signature | $(4, 0)$ | $(0, 4)$ | $(3, 1)$ | $(1, 3)$ |
| Zero divisors | None | None | Cone: $(q'_0)^2 = \sum_k q_k^2$ | Cone: $q_0^2 = \sum_k {q'_k}^2$ |
| Subalgebra | Yes | No (a module over $\mathbb{H}_{\mathbb{B}}$) | No | No |
| Pair with | $i\mathbb{H}_{\mathbb{B}}$ | $\mathbb{H}_{\mathbb{B}}$ | $\mathbb{M}_+$ | $\mathbb{M}_-$ |

The key structural facts:

**The same abstract operator, four specific forms.** The abstract gradient $\tilde{\nabla} = \sum_\mu e_\mu \partial/\partial Q_\mu$ has one form in each subspace. On $\mathbb{H}_{\mathbb{B}}$, all coefficients are real; on $i\mathbb{H}_{\mathbb{B}}$, all four are $-i$; on $\mathbb{M}_-$, the first coefficient is $-i$; on $\mathbb{M}_+$, the three remaining coefficients are $-i$.

**The same abstract d'Alembertian, four signatures.** The abstract d'Alembertian $\Box = \sum_\mu \partial^2/\partial Q_\mu^2$ takes the following specific forms:

- **Signature $(4,0)$** on $\mathbb{H}_{\mathbb{B}}$ — the four-dimensional Euclidean Laplacian.
- **Signature $(0,4)$** on $i\mathbb{H}_{\mathbb{B}}$ — the negative of the Euclidean Laplacian.
- **Signature $(3,1)$** on $\mathbb{M}_-$ — the second-order operator with the first coordinate contributing with negative sign.
- **Signature $(1,3)$** on $\mathbb{M}_+$ — the second-order operator with the three remaining coordinates contributing with negative sign.

**Two mirror pairs, each exchanged by $i$.** The four subspaces fall into two pairs related by multiplication by the central scalar $i$: $\mathbb{H}_{\mathbb{B}}$ with $i\mathbb{H}_{\mathbb{B}}$, and $\mathbb{M}_-$ with $\mathbb{M}_+$. In each pair the exchange reverses the norm form, and with it the sign of $\Box$ and the signature: $(4,0)$ is mirrored by $(0,4)$, and $(3,1)$ by $(1,3)$.

**The zero divisor cone.** The cone on each indefinite subspace is precisely the zero divisor cone of the algebra restricted to that subspace. The two definite subspaces, $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$, have no such cone.

## Relation Between the Four Subspaces

The four subspaces are related by the conjugations of the biquaternion algebra and by multiplication by $i$.

**Quaternion conjugation.** The quaternion conjugation $\bar{\cdot}$ preserves each of the four subspaces:

$$
\bar{\mathbb{H}}_{\mathbb{B}} = \mathbb{H}_{\mathbb{B}}, \qquad \bar{i\mathbb{H}}_{\mathbb{B}} = i\mathbb{H}_{\mathbb{B}}, \qquad \bar{\mathbb{M}}_- = \mathbb{M}_-, \qquad \bar{\mathbb{M}}_+ = \mathbb{M}_+.
$$

The reason is that quaternion conjugation negates the vector part of a biquaternion, and on each of these subspaces the reality structure of the vector part is preserved under negation: the vector part of an element of $\mathbb{H}_{\mathbb{B}}$ is real and its negative is real; the vector part of an element of $i\mathbb{H}_{\mathbb{B}}$ is imaginary and its negative is imaginary; the vector part of an element of $\mathbb{M}_-$ is real and its negative is real; the vector part of an element of $\mathbb{M}_+$ is imaginary and its negative is imaginary.

**Complex conjugation.** The complex conjugation $^*$ also preserves each of the four subspaces:

$$
\mathbb{H}_{\mathbb{B}}^* = \mathbb{H}_{\mathbb{B}}, \qquad (i\mathbb{H}_{\mathbb{B}})^* = i\mathbb{H}_{\mathbb{B}}, \qquad \mathbb{M}_-^* = \mathbb{M}_-, \qquad \mathbb{M}_+^* = \mathbb{M}_+.
$$

Indeed, on $\mathbb{H}_{\mathbb{B}}$ the coefficients are real, so $^*$ is the identity. On $i\mathbb{H}_{\mathbb{B}}$ every coefficient is purely imaginary, so $^*$ negates the element, $^* = -\mathrm{id}$, and carries the subspace onto itself. On $\mathbb{M}_-$, the scalar coefficient $iq'_0$ is conjugated to $-iq'_0$ (still imaginary) and the vector coefficients $q_k$ are real (unchanged). On $\mathbb{M}_+$, the scalar coefficient $q_0$ is real (unchanged) and the vector coefficients $iq'_k$ are conjugated to $-iq'_k$ (still imaginary).

**Hermitian conjugation.** The Hermitian conjugation $\dagger$ preserves each of the four subspaces as a set, but acts differently on each: it is the identity on $\mathbb{M}_+$, negation on $\mathbb{M}_-$, quaternion conjugation on $\mathbb{H}_{\mathbb{B}}$, and the negative of quaternion conjugation on $i\mathbb{H}_{\mathbb{B}}$:

$$
\tilde{Q}^\dagger = \tilde{Q} \;\; \text{for } \tilde{Q} \in \mathbb{M}_+, \qquad \tilde{Q}^\dagger = -\tilde{Q} \;\; \text{for } \tilde{Q} \in \mathbb{M}_-, \qquad \tilde{Q}^\dagger = \bar{\tilde{Q}} \;\; \text{for } \tilde{Q} \in \mathbb{H}_{\mathbb{B}}, \qquad \tilde{Q}^\dagger = -\bar{\tilde{Q}} \;\; \text{for } \tilde{Q} \in i\mathbb{H}_{\mathbb{B}}.
$$

These identities are the defining properties of $\mathbb{M}_\pm$ and a direct computation on $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$.

**Multiplication by $i$.** Multiplication by the scalar imaginary $i$ exchanges the members of each mirror pair:

$$
i \mathbb{M}_- = \mathbb{M}_+, \qquad i \mathbb{M}_+ = \mathbb{M}_-, \qquad i(i\mathbb{H}_{\mathbb{B}}) = \mathbb{H}_{\mathbb{B}}, \qquad i \mathbb{H}_{\mathbb{B}} = i\mathbb{H}_{\mathbb{B}}.
$$

Indeed, for $\tilde{Q} = iq'_0 e_0 + \sum_k q_k e_k \in \mathbb{M}_-$, we have $i\tilde{Q} = -q'_0 e_0 + i\sum_k q_k e_k$, which has real scalar part $-q'_0$ and imaginary vector part $i\sum_k q_k e_k$ — hence lies in $\mathbb{M}_+$. The reverse map is analogous. For $\tilde{P} = \sum_\mu q'_\mu e_\mu \in \mathbb{H}_{\mathbb{B}}$ one has $i\tilde{P} = \sum_\mu q'_\mu (ie_\mu) \in i\mathbb{H}_{\mathbb{B}}$, with the same real coordinates $q'_\mu$, and $i(i\tilde{P}) = -\tilde{P} \in \mathbb{H}_{\mathbb{B}}$; the two subspaces are exchanged in the same way. In both pairs the exchange reverses the norm form, $N(i\tilde{Q}) = -N(\tilde{Q})$.

**Intersections.** The pairwise intersections are:

$$
\mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_- = \mathrm{span}_\mathbb{R}\{e_1, e_2, e_3\}, \qquad \mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_+ = \mathbb{R} e_0, \qquad \mathbb{M}_- \cap \mathbb{M}_+ = \{0\},
$$

$$
\mathbb{H}_{\mathbb{B}} \cap i\mathbb{H}_{\mathbb{B}} = \{0\}, \qquad i\mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_- = \mathbb{R}(ie_0), \qquad i\mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_+ = \mathrm{span}_\mathbb{R}\{ie_1, ie_2, ie_3\}.
$$

**Proof of the first intersection.** An element of $\mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_-$ has coefficients $Q_0, Q_1, Q_2, Q_3$ that are simultaneously real (from $\mathbb{H}_{\mathbb{B}}$) and satisfy $Q_0$ imaginary, $Q_1, Q_2, Q_3$ real (from $\mathbb{M}_-$). For $Q_0$ to be both real and imaginary, $Q_0 = 0$. The coefficients $Q_1, Q_2, Q_3$ are real, which is consistent with both conditions. So the intersection is the real span of $e_1, e_2, e_3$, a three-dimensional subspace.

**Proof of the second intersection.** An element of $\mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_+$ has coefficients that are simultaneously real (from $\mathbb{H}_{\mathbb{B}}$) and satisfy $Q_0$ real, $Q_1, Q_2, Q_3$ imaginary (from $\mathbb{M}_+$). For each of the three coefficients $Q_1, Q_2, Q_3$ to be both real and imaginary, $Q_1 = Q_2 = Q_3 = 0$. The coefficient $Q_0$ is real, consistent with both. So the intersection is the real span of $e_0$, a one-dimensional subspace.

**Proof of the third intersection.** An element of $\mathbb{M}_- \cap \mathbb{M}_+$ is both anti-Hermitian and Hermitian, hence satisfies $\tilde{Q} = -\tilde{Q}$, so $\tilde{Q} = 0$. The intersection is trivial.

**Proof of the remaining intersections.** An element of $\mathbb{H}_{\mathbb{B}} \cap i\mathbb{H}_{\mathbb{B}}$ has all coefficients simultaneously real and purely imaginary, hence zero. An element of $i\mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_-$ has $Q_0$ purely imaginary in both readings, so $Q_0$ survives, while each $Q_k$ is required to be both purely imaginary (from $i\mathbb{H}_{\mathbb{B}}$) and real (from $\mathbb{M}_-$), so $Q_1 = Q_2 = Q_3 = 0$; the intersection is $\mathbb{R}(ie_0)$. An element of $i\mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_+$ has $Q_0$ required to be both purely imaginary and real, so $Q_0 = 0$, while $Q_1, Q_2, Q_3$ are purely imaginary in both readings; the intersection is $\mathrm{span}_\mathbb{R}\{ie_1, ie_2, ie_3\}$.

**Decompositions.** The three decompositions of $\mathbb{B}$ are:

$$
\mathbb{B} = \mathbb{H}_{\mathbb{B}} \oplus i\mathbb{H}_{\mathbb{B}}, \qquad \mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-, \qquad \mathbb{B} = \mathbb{C}_{\mathbb{B}} \oplus \mathrm{Vect}(\mathbb{B}).
$$

The first is the quaternion decomposition — the $\pm 1$ eigenspaces of complex conjugation $^*$; the second is the Hermitian decomposition — the $\pm 1$ eigenspaces of Hermitian conjugation $\dagger$; the third is the center–vector decomposition — the $\pm 1$ eigenspaces of quaternion conjugation $\bar{\cdot}$, whose summands are two- and six-dimensional. The first two are direct sums of two four-dimensional real subspaces, and it is they that supply the domains of the analysis above; the third has no four-dimensional summand and lies outside it.

The pairwise sums of subspaces from different decompositions are not the whole algebra: for instance, $\mathbb{H}_{\mathbb{B}} + \mathbb{M}_- = \mathrm{span}_\mathbb{R}\{e_0, ie_0, e_1, e_2, e_3\}$, which is a five-dimensional subspace of $\mathbb{B}$, and $\mathbb{H}_{\mathbb{B}} + \mathbb{M}_+ = \mathrm{span}_\mathbb{R}\{e_0, e_1, e_2, e_3, ie_1, ie_2, ie_3\}$, which is a seven-dimensional subspace. Only within each decomposition does the direct sum recover the full algebra.

**Compatibility of the analysis.** The differential and integral operators on the four subspaces are the same abstract operators, with the same formulas. The difference is only in the specific expression of the partial derivatives in the coordinates of each subspace. A function defined on a domain that intersects two or more subspaces can be analyzed on each subspace separately, and the results agree on the intersections.

## Summary of the Operators

The following table summarizes the specific differential operators on the four subspaces.

**First-order operators.**

| Operator | $\mathbb{H}_{\mathbb{B}}$ | $i\mathbb{H}_{\mathbb{B}}$ | $\mathbb{M}_-$ | $\mathbb{M}_+$ |
|---|---|---|---|---|
| $\tilde{\nabla}$ | $\sum_\mu e_\mu \partial_{q_\mu}$ | $-i\sum_\mu e_\mu \partial_{q'_\mu}$ | $-i e_0 \partial_{q'_0} + \sum_k e_k \partial_{q_k}$ | $e_0 \partial_{q_0} - i \sum_k e_k \partial_{q'_k}$ |
| $\bar{\tilde{\nabla}}$ | $e_0 \partial_{q_0} - \sum_k e_k \partial_{q_k}$ | $-i e_0 \partial_{q'_0} + i \sum_k e_k \partial_{q'_k}$ | $-i e_0 \partial_{q'_0} - \sum_k e_k \partial_{q_k}$ | $e_0 \partial_{q_0} + i \sum_k e_k \partial_{q'_k}$ |
| $\tilde{D} = \bar{\tilde{U}}\tilde{\nabla}$ | (specific form above) | $-i$ times the $\mathbb{H}_{\mathbb{B}}$ form | (specific form above) | (specific form above) |

**Second-order operators.** The d'Alembertian is the natural second-order operator; the square of the gradient is related to it by the identity $\tilde{\nabla}^2 = 2\partial_{Q_0}\tilde{\nabla} - \Box$.

| Operator | $\mathbb{H}_{\mathbb{B}}$ | $i\mathbb{H}_{\mathbb{B}}$ | $\mathbb{M}_-$ | $\mathbb{M}_+$ |
|---|---|---|---|---|
| $\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \bar{\tilde{\nabla}}\tilde{\nabla}$ | $\partial_{q_0}^2 + \Delta_{\mathbb{H}}$ | $-\partial_{q'_0}^2 - \Delta_{i\mathbb{H}}$ | $-\partial_{q'_0}^2 + \Delta_{\mathbb{M}_-}$ | $\partial_{q_0}^2 - \Delta_{\mathbb{M}_+}$ |
| Signature of $\Box$ | $(4, 0)$ | $(0, 4)$ | $(3, 1)$ | $(1, 3)$ |
| $\tilde{\nabla}^2$ (direct) | $(\partial_{q_0}^2 - \Delta_{\mathbb{H}}) + 2\sum_k e_k \partial_{q_0}\partial_{q_k}$ | $-(\partial_{q'_0}^2 - \Delta_{i\mathbb{H}}) - 2\sum_k e_k \partial_{q'_0}\partial_{q'_k}$ | $-(\partial_{q'_0}^2 + \Delta_{\mathbb{M}_-}) - 2i\sum_k e_k \partial_{q'_0}\partial_{q_k}$ | $(\partial_{q_0}^2 + \Delta_{\mathbb{M}_+}) - 2i\sum_k e_k \partial_{q_0}\partial_{q'_k}$ |
| $\tilde{\nabla}^2$ (via $\Box$) | $2\partial_{q_0}\tilde{\nabla} - \Box_{\mathbb{H}}$ | $-2i\partial_{q'_0}\tilde{\nabla} - \Box_{i\mathbb{H}}$ | $-2i\partial_{q'_0}\tilde{\nabla} - \Box_{\mathbb{M}_-}$ | $2\partial_{q_0}\tilde{\nabla} - \Box_{\mathbb{M}_+}$ |

**Cauchy kernel.** The kernel $\tilde{G}(\tilde{Q}) = \bar{\tilde{Q}}/\|\tilde{Q}\|_E^4$ is a constant multiple of the fundamental solution of the first-order operator $\tilde{\nabla}$ (the Cauchy kernel for the Cauchy integral formula), not of the second-order d'Alembertian. With this convention, the explicit forms on the four subspaces are:

| Subspace | $\tilde{G}(\tilde{Q})$ |
|---|---|
| $\mathbb{H}_{\mathbb{B}}$ | $\dfrac{q_0 e_0 - \sum_k q_k e_k}{\left(\sum_\mu q_\mu^2\right)^2}$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $\dfrac{i q'_0 e_0 - i\sum_k q'_k e_k}{\left(\sum_\mu {q'_\mu}^2\right)^2}$ |
| $\mathbb{M}_-$ | $\dfrac{i q'_0 e_0 - \sum_k q_k e_k}{\left((q'_0)^2 + \sum_k q_k^2\right)^2}$ |
| $\mathbb{M}_+$ | $\dfrac{q_0 e_0 - i\sum_k q'_k e_k}{\left(q_0^2 + \sum_k {q'_k}^2\right)^2}$ |

The Cauchy kernel has the same abstract form on all four subspaces; its expression in the specific coordinates differs only through the specific form of $\bar{\tilde{Q}}$ and $\|\tilde{Q}\|_E$.

## Open Questions

The following questions are not answered in this article and are left for later work:

1. **The relation between the analyses on the two members of each mirror pair.** The subspaces $\mathbb{M}_-$ and $\mathbb{M}_+$ are exchanged by multiplication by $i$, which also exchanges their specific d'Alembertians, and the same is true of $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$. Is the analysis on the second member of each pair fully determined by the analysis on the first and the exchange map, or does it differ in an essential way? The formulas above suggest that the exchange is exact; a proof would remove the pairs from the list of independent cases.

2. **The analysis on the complex and vector subspaces.** The complex subspace $\mathbb{C}_{\mathbb{B}}$ is two-dimensional and carries the ordinary complex analysis. How does the biquaternion analysis on the four-dimensional subspaces restrict to $\mathbb{C}_{\mathbb{B}}$? The vector subspace $\mathrm{Vect}(\mathbb{B})$ is six-dimensional, and raises the complementary question: whether any part of the theory survives on a subspace that is not four-dimensional.

3. **The analysis on the full algebra.** Can the analysis be extended from the four-dimensional subspaces to the full eight-dimensional algebra $\mathbb{B}$? If so, what replaces the four-dimensional operators, and what is the meaning of the partial derivatives with respect to genuinely complex coefficients?

4. **The role of the zero divisor cones.** On $\mathbb{M}_-$ and $\mathbb{M}_+$, the zero divisors form three-dimensional cones. What is the structure of functions that are defined on the cones, or that have singularities on the cones?

5. **The integral formulas on the four subspaces.** The Cauchy integral formulas on $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_-$, and $\mathbb{M}_+$ have the same abstract form. Do they differ in the specific coordinates in a way that reflects the difference in the signature of the d'Alembertian?

6. **The interaction between the subspaces.** If a function is defined on two of the subspaces, how do the analyses on the two subspaces interact?

7. **The square of the gradient.** The square $\tilde{\nabla}^2$ appears when the gradient is applied twice without conjugation. The identity $\tilde{\nabla}^2 = 2\partial_{Q_0}\tilde{\nabla} - \Box$ expresses it in terms of $\Box$ and the first derivative. What is the natural setting in which the square $\tilde{\nabla}^2$ (as opposed to $\Box$) is the operator that appears?

## Summary

The four-dimensional subspaces of the biquaternion algebra are the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$, the anti-Hermitian subspace $\mathbb{M}_-$, and the Hermitian subspace $\mathbb{M}_+$. They are the four-dimensional members of the algebra's six distinguished real subspaces; the remaining two, the two-dimensional center $\mathbb{C}_{\mathbb{B}}$ and the six-dimensional vector subspace $\mathrm{Vect}(\mathbb{B})$, are of the wrong dimension and lie outside the four-dimensional theory.

The quaternion subspace $\mathbb{H}_{\mathbb{B}}$ is the fixed-point set of complex conjugation. It is a subalgebra of $\mathbb{B}$ isomorphic to the quaternion algebra $\mathbb{H}$, with a positive-definite norm form and no zero divisors. Its specific d'Alembertian is the four-dimensional Euclidean Laplacian in the real coordinates $(q_0, q_1, q_2, q_3)$, with signature $(4, 0)$.

The anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$ is the anti-fixed-point set of complex conjugation. Its coordinates are $(q'_0, q'_1, q'_2, q'_3)$, all imaginary. Its norm form is negative definite, of signature $(0, 4)$, and it contains no zero divisors. Its specific d'Alembertian is the negative Euclidean Laplacian, $-\partial_{q'_0}^2 - \Delta_{i\mathbb{H}}$. It is a module over $\mathbb{H}_{\mathbb{B}}$ but not a subalgebra, and it is the image of $\mathbb{H}_{\mathbb{B}}$ under the central rotation $\tilde{P} \mapsto i\tilde{P}$. It is the mirror of the quaternion subspace.

The anti-Hermitian subspace $\mathbb{M}_-$ is the fixed-point set of anti-Hermitian conjugation. Its coordinates are $(q'_0, q_1, q_2, q_3)$, with the first coefficient imaginary. Its specific d'Alembertian is $-\partial_{q'_0}^2 + \Delta_{\mathbb{M}_-}$, with signature $(3, 1)$. Its zero divisors form the cone $(q'_0)^2 = q_1^2 + q_2^2 + q_3^2$.

The Hermitian subspace $\mathbb{M}_+$ is the fixed-point set of Hermitian conjugation. Its coordinates are $(q_0, q'_1, q'_2, q'_3)$, with the three remaining coefficients imaginary. Its specific d'Alembertian is $\partial_{q_0}^2 - \Delta_{\mathbb{M}_+}$, with signature $(1, 3)$. Its zero divisors form the mirror cone $q_0^2 = {q'_1}^2 + {q'_2}^2 + {q'_3}^2$.

The four subspaces share the same **abstract** differential and integral operators — the gradient $\tilde{\nabla}$, its quaternion conjugate $\bar{\tilde{\nabla}}$, the d'Alembertian $\Box$, the square of the gradient $\tilde{\nabla}^2$, the convective derivative $\tilde{D}$, and the Cauchy kernel $\tilde{G}$ — but the **specific expressions** of these operators in the coordinates of each subspace differ in a characteristic way. The abstract d'Alembertian $\Box = \sum_\mu \partial^2/\partial Q_\mu^2$ becomes the Euclidean Laplacian on $\mathbb{H}_{\mathbb{B}}$, its negative on $i\mathbb{H}_{\mathbb{B}}$, the operator with signature $(3,1)$ on $\mathbb{M}_-$, and the mirror operator with signature $(1,3)$ on $\mathbb{M}_+$. The square of the gradient is related to the d'Alembertian by the identity $\tilde{\nabla}^2 = 2\partial_{Q_0}\tilde{\nabla} - \Box$, which holds in the abstract algebra and in each subspace.

The four subspaces are related by the conjugations of the biquaternion algebra and by multiplication by $i$. Quaternion conjugation and complex conjugation each preserve all four subspaces. Multiplication by $i$ exchanges the members of the two mirror pairs — $\mathbb{H}_{\mathbb{B}}$ with $i\mathbb{H}_{\mathbb{B}}$, and $\mathbb{M}_-$ with $\mathbb{M}_+$ — and reverses the norm form in each, so that the signatures $(4,0)$ and $(3,1)$ go over into $(0,4)$ and $(1,3)$. Each pair spans the algebra, $\mathbb{B} = \mathbb{H}_{\mathbb{B}} \oplus i\mathbb{H}_{\mathbb{B}}$ and $\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-$; the third decomposition of the algebra, $\mathbb{B} = \mathbb{C}_{\mathbb{B}} \oplus \mathrm{Vect}(\mathbb{B})$, pairs the center with the vector subspace and has no four-dimensional summand.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra |
| $\mathbb{H}_{\mathbb{B}}$ | Quaternion subspace: coordinates $(q_0, q_1, q_2, q_3)$ all real |
| $i\mathbb{H}_{\mathbb{B}}$ | Anti-quaternion subspace: coordinates $(q'_0, q'_1, q'_2, q'_3)$ all imaginary; signature $(0,4)$, no zero divisors; a module over $\mathbb{H}_{\mathbb{B}}$ |
| $\mathbb{C}_{\mathbb{B}}, \mathrm{Vect}(\mathbb{B})$ | Center (real dimension 2) and vector subspace (real dimension 6); not domains of the four-dimensional analysis |
| $\mathbb{M}_-$ | Anti-Hermitian subspace: coordinates $(q'_0, q_1, q_2, q_3)$, first coefficient imaginary |
| $\mathbb{M}_+$ | Hermitian subspace: coordinates $(q_0, q'_1, q'_2, q'_3)$, remaining coefficients imaginary |
| $Q_\mu$ | Complex coefficient in the standard basis |
| $\tilde{\nabla}$ | Biquaternionic gradient (abstract and specific forms) |
| $\bar{\tilde{\nabla}}$ | Quaternion conjugate of the gradient |
| $\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \bar{\tilde{\nabla}}\tilde{\nabla}$ | d'Alembertian (natural second-order operator) |
| $\tilde{\nabla}^2 = 2\partial_{Q_0}\tilde{\nabla} - \Box$ | Square of the gradient |
| $\tilde{D} = \bar{\tilde{U}}\tilde{\nabla}$ | Convective derivative |
| $\tilde{G}(\tilde{Q}) = \bar{\tilde{Q}}/\|\tilde{Q}\|_E^4$ | Cauchy kernel (fundamental solution of $\tilde{\nabla}$) |
| $\Delta_{\mathbb{H}}, \Delta_{i\mathbb{H}}, \Delta_{\mathbb{M}_-}, \Delta_{\mathbb{M}_+}$ | Spatial Laplacians in each subspace |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the original formulation.
- William Kingdon Clifford, "Preliminary Sketch of Biquaternions" (1873), for the first systematic treatment of biquaternions.
- R. Fueter, "Die Funktionentheorie der Differentialgleichungen $\Delta u = 0$ und $\Delta\Delta u = 0$ mit vier reellen Variablen", *Commentarii Mathematici Helvetici* **7** (1934–35) 307–330, for the analysis of quaternion-valued functions of four real variables.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- F. Brackx, R. Delanghe, and F. Sommen, *Clifford Analysis* (Pitman, 1982), for the general Clifford analysis.
- John Ryan, *Clifford Algebras in Analysis and Related Topics* (CRC Press, 1996), for the analytic theory of Clifford algebras.

