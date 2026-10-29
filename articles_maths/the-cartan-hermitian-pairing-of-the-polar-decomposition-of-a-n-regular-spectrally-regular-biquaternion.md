# __The Cartan Hermitian Pairing of the Polar Decomposition of a N-Regular, Spectrally Regular Biquaternion__

## Introduction

Throughout this article $\tilde Q$ lies in the N-regular, spectrally regular sector $\Sigma_{11}$, so $N\neq0$ and $B^2\neq0$. The sector condition is the domain on which the eigenbasis and the companion constructions are those of the regular case; the wall $B^2=0$ is treated in the companion article of the same title with *Spectrally Degenerate*.

Every element of $\Sigma_{11}$ is the ordered product of a positive real scale, a central phase and two unit factors,

$$
\tilde{Q} = r\,\exp(i\alpha)\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r}
= r\,\exp(i\alpha)\,\exp\Bigl(i\tfrac{\psi}{2}\vec u_{\mathrm b}\Bigr)\,\exp\Bigl(\tfrac{\theta}{2}\vec u_{\mathrm r}\Bigr) .
$$

The four factors are those of *The Polar Decomposition of a N-Regular Biquaternion*, §*The Four Factors*, and their exponential forms those of *Exponential Polar Decomposition of a N-Regular, Spectrally Regular Biquaternion*, §*The Decomposition*: the scale $r>0$, the central phase $\exp(i\alpha)$ with $\alpha\in(-\pi/2,\pi/2]$, the Hermitian positive boost $\tilde U_{\mathrm b}$ of rapidity $\psi\ge0$ and the unit real rotor $\tilde u_{\mathrm r}$ of angle $\theta\in[0,2\pi]$. They are unique, so they can be grouped in pairs in exactly three ways. This article reads the grouping that puts the scale with the boost.

**The Cartan Hermitian pairing** is the grouping that multiplies the scale into the boost and the phase into the rotor:

$$ \tilde{Q} = \tilde Q_H\,\tilde Q_0 , \qquad \tilde Q_H = r\,\tilde U_{\mathrm b} , \qquad \tilde Q_0 = \exp(i\alpha)\,\tilde u_{\mathrm r}. $$

It takes the first and the third factors of the word, the scale and the boost $\tilde U_{\mathrm b}$, into $\tilde Q_H$, and the second and the fourth, the phase and the rotor $\tilde u_{\mathrm r}$, into $\tilde Q_0$. The two factors are therefore of two different kinds: $\tilde Q_H$ is **Hermitian and positive**, $\tilde Q_0$ is **$*$-unitary**. The pairing is the matrix polar decomposition of the biquaternion, read in the algebra, and it is the form of the polar word that the physics articles use for a unit-norm Lorentz rotor. It is called the **Cartan pairing** here because the two exponents of its factors lie in the two summands of the Cartan decomposition of the algebra as a real Lie algebra, one Hermitian and one anti-Hermitian; the Hermitian split of the exponents, and not the mere grouping of the factors, is what the name records.

**The approach.** The article follows the skeleton shared by the three pairing articles: the results imported, the pairing and the two equations that determine its factors, the two factors, existence and domain, the comparison of the three bracketings, and the three conjugations. It then records the two exponents, which are the precise sense in which the pairing is a Hermitian pairing, the Cartan decomposition of the unit group, and the published form. Each result is collected in a table, and each imported proof is cited rather than repeated.

**The result.** For every biquaternion with $\langle\tilde Q\rangle_{\natural}\neq0$ the word $\tilde{Q} = \tilde Q_H\,\tilde Q_0$ is unique with $\tilde Q_H$ Hermitian positive and $\tilde Q_0$ $*$-unitary; the first factor is the Hermitian positive square root $\tilde Q_H = \sqrt{\tilde{Q}\tilde{Q}^{*}}$, the second is $\tilde Q_0 = \tilde Q_H^{-1}\tilde{Q}$, and the two exponents $\ln \tilde Q_H$ and $\ln \tilde Q_0$ lie in the Hermitian subspace $\mathbb{M}_+$ and the anti-Hermitian subspace $\mathbb{M}_-$. The pairing is collected in the table.

| item | the Cartan pairing |
|---|---|
| grouping | the scale with the boost, the phase with the rotor |
| first factor | $\tilde Q_H=r\tilde U_{\mathrm b}=\sqrt{\tilde Q\tilde Q^{*}}$, Hermitian positive |
| second factor | $\tilde Q_0=\exp(i\alpha)\tilde u_{\mathrm r}=\tilde Q_H^{-1}\tilde Q$, $*$-unitary |
| equation | $\tilde Q=\tilde Q_H\tilde Q_0$, with $\tilde Q\tilde Q^{*}=\tilde Q_H^{2}$ |
| exponents | $\ln\tilde Q_H\in\mathbb{M}_+$, $\ln\tilde Q_0\in\mathbb{M}_-$ |
| domain | $\langle\tilde Q\rangle_{\natural}\neq0$, the complement of the null cone |
| classical limit | the matrix polar decomposition |
| position among the three | the only total pairing, and the only pairing whose two factors are of the two involutive kinds |

The other two pairings are partial: *The Hamilton Root Pairing of the Polar Decomposition of a N-Regular, Spectrally Regular Biquaternion* cannot form its single exponential where the vector part is null, and *The Quaternion Pairing of the Polar Decomposition of a N-Regular, Spectrally Regular Biquaternion* cannot construct its modulus where the real quaternion part is singular. The present pairing is **not** partial: it loses nothing, it is available on the whole complement of the null cone, and both of its factors are functions of the element alone. The complement is the maximal domain of the positive definite $*$-unitary form. The extension to the cone, where the $*$-unitary factor becomes a partial isometry and the positive factor a scaled Hermitian idempotent, is *The Polar Decomposition of a N-Degenerate Biquaternion*. The unit-norm case, in which the scale and the phase are trivial, is the Cartan decomposition $\tilde{Q} = \tilde U_{\mathrm b}\tilde u_{\mathrm r}$ of the unit group, and the physical interpretation of the two factors is the Lorentz boost and the spatial rotation.

The article assumes the algebra and the domain of the polar decomposition from the companion article, and takes the four factors as defined there and does not re-derive them. It is not the four-factor decomposition itself, and it is not the operator polar decomposition of *The Polar Decomposition of an Operator of the Form*, a different statement about a Tomita operator on a completion. No physics is invoked; the physical interpretation is recorded where it clarifies the algebra.

## The Results Used

The article takes the following results as established and does not prove them again.

| result | established in | used here for |
|---|---|---|
| the four factors, their ranges and their order | *The Polar Decomposition of a N-Regular Biquaternion*, §*The Four Factors* | the word that is bracketed |
| existence and uniqueness of the word on $\langle\tilde Q\rangle_{\natural}\neq0$ | *Exponential Polar Decomposition of a N-Regular, Spectrally Regular Biquaternion*, §*Existence and Uniqueness* | the factorisation $\tilde Q=\tilde Q_H\tilde Q_0$, its uniqueness and its domain |
| the matrix model and the transport of ${}^{*}$ | *$M_2(\mathbb{C})$ Model : The Product, the Trace and the Determinant* and *$M_2(\mathbb{C})$ Representation : Trace, Determinant and the Biquaternion Norm* | the equation $\tilde Q\tilde Q^{*}=\tilde Q_H^{2}$ |
| the Hermitian and anti-Hermitian split | *Hermitian and Skew-Hermitian Elements*, §*The Two Halves* | the subspaces $\mathbb{M}_\pm$ and the two exponents |
| the $*$-unitary group | *The Unitary Group of the Biquaternion Algebra*, §*The Structure of the $*$-Unitary Group* | $\mathrm{U}(\mathbb{B})\cong\mathrm{U}(2)\cong\mathrm{U}(1)\cdot\mathrm{Sp}(1)$ |
| the positive cone and the positive square root | *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint*, §*The Polar Decomposition* | $\tilde Q_H=\sqrt{\tilde Q\tilde Q^{*}}$ and its positivity |
| the Cartan decomposition | *The Cartan Involution and the Cartan Decomposition*, §*The Cartan Decomposition* | the split of the exponents into $\mathbb{M}_+\oplus\mathbb{M}_-$ |

The central computation of the article is the product $\tilde Q\tilde Q^{*}=\tilde Q_H^{2}$ and the recovery $\tilde Q_0=\tilde Q_H^{-1}\tilde Q$; the theorem is the matrix polar decomposition read through these results, and §*The Matrix Proof* reduces it to the matrix theorem.

## The Pairing

### The Definition

The **Cartan pairing** of the polar decomposition is the regrouping in which the scale and the boost form the first factor and the phase and the rotor the second:

$$
\tilde{Q} = \tilde Q_H\,\tilde Q_0 , \qquad \tilde Q_H = r\,\tilde U_{\mathrm b} \in \mathbb{M}_+ , \qquad \tilde Q_0 = \exp(i\alpha)\,\tilde u_{\mathrm r} \in \mathrm{U}(\mathbb{B}) .
$$

The first factor is a positive real times a Hermitian positive unit-norm element, hence Hermitian positive; the second is a central phase times a unit real quaternion, hence $*$-unitary. The word is the polar word with the two parentheses inserted after the boost, and the two non-central factors keep their order: the boost stays on the left of the rotor, and no conjugation appears.

### The Cartan Projection

The map that extracts the second factor has a standard name. The **Cartan projection** is

$$
\tilde Q\longmapsto\tilde Q_0=\tilde Q_H^{-1}\tilde Q ,
$$

the $*$-unitary component of the factorization $\mathbb{B}^{\times}=\{\tilde Q_H\}\,\mathrm{U}(\mathbb{B})$. It restricts to the identity on $\mathrm{U}(\mathbb{B})$ and is equivariant on the right, $(\tilde Q k)_0=\tilde Q_0 k$ for $k\in\mathrm{U}(\mathbb{B})$; the fibre over $\tilde Q_0$ is the left coset $\{\tilde Q_H\}\tilde Q_0$. The name is the one used for the $K$-component of the Cartan decomposition $G=PK$: for $G=\mathbb{B}^{\times}\cong GL_2(\mathbb{C})$ the subgroup $K=\mathrm{U}(\mathbb{B})\cong\mathrm{U}(2)$ is the maximal compact subgroup. The word *projection* is meant in that sense, not as a linear idempotent: the map is a retraction, not a homomorphism.

### The Statement

The pairing is stated by the one equation it solves. Multiplying the element by its Hermitian conjugate and using that ${}^{*}$ is an anti-automorphism, that the central phase is central and that the rotor satisfies $\tilde u_{\mathrm r}\tilde u_{\mathrm r}^{*} = e_t$,

$$
\tilde{Q}\tilde{Q}^{*} = \bigl(r \exp(i\alpha)\tilde U_{\mathrm b}\tilde u_{\mathrm r}\bigr)\bigl(r \exp(-i\alpha)\tilde u_{\mathrm r}^{*}\tilde U_{\mathrm b}^{*}\bigr) = r^{2}\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r}\tilde u_{\mathrm r}^{*}\,\tilde U_{\mathrm b}^{*} = r^{2}\tilde U_{\mathrm b}^{2} = \tilde Q_H^{2} ,
$$

using the Hermitian character $\tilde U_{\mathrm b}^{*} = \tilde U_{\mathrm b}$ of the boost. The product $\tilde{Q}\tilde{Q}^{*}$ is therefore the **square of the first factor**, and the first factor is recovered from the element by a square root,

$$
\boxed{\;\tilde Q_H = \sqrt{\tilde{Q}\tilde{Q}^{*}}\;}.
$$

This is the only equation the pairing solves directly; the second factor follows from the first by division.

### The Second Factor Is the Element Divided by the First

Because $\tilde Q_H = r\tilde U_{\mathrm b}$ is the polar modulus of the element and is invertible, the second factor is

$$
\tilde Q_0 = \tilde Q_H^{-1}\tilde{Q} .
$$

Its inverse is $\tfrac{1}{r}\tilde U_{\mathrm b}^{\natural}$, since $\tilde U_{\mathrm b}^{-1} = \tilde U_{\mathrm b}^{\natural}$ for a unit-norm boost; substituting the polar word, the second factor is therefore $\tilde Q_0 = \tfrac{1}{r}\tilde U_{\mathrm b}^{\natural}\tilde{Q} = \exp(i\alpha)\tilde u_{\mathrm r}$, $*$-unitary as it must be. The two relations $\tilde Q_H = \sqrt{\tilde{Q}\tilde{Q}^{*}}$ and $\tilde Q_0 = \tilde Q_H^{-1}\tilde{Q}$ recover the whole pairing from the element, and they are the reason the pairing needs no construction external to the algebra.

### The Reversed Word

The Hermitian conjugate of the element is not the product of the two factors in the other order,

$$
\tilde{Q}^{*} = \tilde Q_0^{*}\tilde Q_H^{*} = \tilde Q_0^{*}\tilde Q_H ,
$$

which is $\tilde Q_0^{*}\tilde Q_H$ and not $\tilde Q_H\,\tilde Q_0^{*}$ or $\tilde Q_H\,\tilde Q_0$, because the boost and the rotor do not commute and the conjugation reverses the order. Combining the two displays, $\tilde{Q}^{*}$ is the conjugate of the first factor by the inverse of the second on the left and by the second on the right,

$$
\tilde{Q}^{*} = \bigl(\tilde Q_0^{*}\tilde Q_H\,\tilde Q_0\bigr)\tilde Q_0^{*} ,
$$

and the two factors of $\tilde{Q}^{*}$ in the Cartan shape are therefore $\tilde Q_0^{*}\tilde Q_H\,\tilde Q_0$, Hermitian positive, and $\tilde Q_0^{*}$, $*$-unitary. The pairing of the conjugate element is a regrouping of the two factors of $\tilde{Q}$ only in this conjugated sense.

## The First Factor: Hermitian Positive

### The Hermitian Subspace

The Hermitian conjugation ${}^{*}$ is an involution, so the algebra splits into its fixed space and its anti-fixed space,

$$
\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_- , \qquad \mathbb{M}_\pm = \{\tilde{Q} : \tilde{Q}^{*} = \pm\tilde{Q}\} .
$$

This is the split of *Hermitian and Skew-Hermitian Elements*, §*The Two Halves*.

| subspace | condition | scalar part | vector part | matrix model | role |
|---|---|---|---|---|---|
| $\mathbb{M}_+$ | $\tilde{Q}^{*} = \tilde{Q}$ | real | purely imaginary | Hermitian matrices | the boosts and the scales |
| $\mathbb{M}_-$ | $\tilde{Q}^{*} = -\tilde{Q}$ | purely imaginary | real | anti-Hermitian matrices | the four-vectors and the exponents |

The first factor of the Cartan pairing is the element $\tilde Q_H = r\tilde U_{\mathrm b} = r\cosh\tfrac{\psi}{2}\,e_t + ir\sinh\tfrac{\psi}{2}\,\vec u_{\mathrm b}$: its scalar part $r\cosh\tfrac{\psi}{2}$ is real and its vector part $ir\sinh\tfrac{\psi}{2}\,\vec u_{\mathrm b}$ is purely imaginary, so $\tilde Q_H$ lies in $\mathbb{M}_+$.

### Positivity

The first factor is not merely Hermitian: it is **positive**. In the matrix model $\mathsf{M}_2(\tilde Q_H)$ is Hermitian with eigenvalues $r \exp(\pm\psi/2)$, both positive since $r>0$, so $\tilde Q_H$ is positive definite (*Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint*, §*The Polar Decomposition*). Its determinant is the norm

$$
\det\mathsf{M}_2(\tilde Q_H) = \langle\tilde Q_H\rangle_{\natural} = r^{2}\,\langle\tilde U_{\mathrm b}\rangle_{\natural} = r^{2} > 0 ,
$$

which is the squared scale and is positive. The scalar part of $\tilde Q_H$ carries the scale, and the traceless part carries the rapidity and the axis of the boost.

### The Scale and the Boost

The first factor is where the pairing keeps the **scale** and the **boost**. The scale $r$ is the positive modulus, $r = |\langle\tilde Q\rangle_{\natural}|^{1/2}$; the boost $\tilde U_{\mathrm b}$ is the Hermitian positive unit-norm element of the polar word. The first factor, which contains both, is the only factor of the pairing that is not compact. The norm of the first factor is the squared scale, and the two statements $\langle\tilde Q_H\rangle_{\natural} = r^{2}$ and $\det\mathsf{M}_2(\tilde Q_H) = r^{2}$ are the same statement in the algebra and in the matrix model.

| aspect | value |
|---|---|
| formula | $\tilde Q_H=r\tilde U_{\mathrm b}=\sqrt{\tilde Q\tilde Q^{*}}$ |
| kind | Hermitian positive |
| norm | $\langle\tilde Q_H\rangle_{\natural}=r^{2}$ |
| eigenvalues | $r\exp(\pm\psi/2)$ in the matrix model |
| conjugation | $\tilde Q_H^{*}=\tilde Q_H$, $\overline{\tilde Q_H}=\tilde Q_H^{\natural}=r\tilde U_{\mathrm b}^{\natural}$ |
| role | the scale and the boost, the only non-compact factor |

## The Second Factor: $*$-Unitary

### The $*$-Unitary Group

The $*$-unitary elements of the algebra are the elements fixed by the equation $\tilde Q_0^{*}\tilde Q_0 = e_t$,

$$ \mathrm{U}(\mathbb{B}) = \{\tilde Q_0 : \tilde Q_0^{*}\tilde Q_0 = e_t\} \cong \mathrm{U}(2) \cong \mathrm{U}(1)\cdot\mathrm{Sp}(1), $$

a compact group of real dimension four, the product of the central phase circle and the unit sphere of the real quaternions (*The Unitary Group of the Biquaternion Algebra*, §*The Structure of the $*$-Unitary Group*). The second factor of the Cartan pairing is such an element: $\tilde Q_0 = \exp(i\alpha)\tilde u_{\mathrm r}$ is the product of the central phase, of modulus one, and the unit real quaternion, and it satisfies $\tilde Q_0\,\tilde Q_0^{*} = e_t$. Its determinant has modulus one, $|\det\mathsf{M}_2(\tilde Q_0)| = 1$, as it must for a $*$-unitary matrix.

### The Phase and the Rotor

The second factor contains the **phase** and the **rotor**. The phase $\exp(i\alpha)$ is central, so it lies in the centre and commutes with everything; the rotor $\tilde u_{\mathrm r}$ is the unit real quaternion of the polar word, the only factor that lies in the quaternion subspace $\mathbb{H}_{\mathbb{B}}$ on the unit sphere, and the only one that is compact and non-central. The two constituents of the second factor commute with each other, the phase being central, so the second factor is itself a product of two exponentials that add, $\exp(i\alpha\,e_t)\exp(\tfrac{\theta}{2}\vec u_{\mathrm r})$.

| aspect | value |
|---|---|
| formula | $\tilde Q_0=\exp(i\alpha)\tilde u_{\mathrm r}=\tilde Q_H^{-1}\tilde Q$ |
| kind | $*$-unitary |
| norm | $\langle\tilde Q_0\rangle_{\natural}=\exp(2i\alpha)$ |
| determinant | $\lvert\det\mathsf{M}_2(\tilde Q_0)\rvert=1$ |
| constituents | the central phase and the unit real rotor |
| role | the phase and the rotor, the compact factor |

### The Two Factors and the Four-Factor Word

The pairing is the grouping of the four factors of the polar word into its two factors, and the grouping is the following.

| factor of the pairing | constituents | character | real dimension |
|---|---|---|---|
| $\tilde Q_H = r\,\tilde U_{\mathrm b}$ | the scale and the boost | Hermitian positive | $1+3 = 4$ |
| $\tilde Q_0 = \exp(i\alpha)\,\tilde u_{\mathrm r}$ | the phase and the rotor | $*$-unitary | $1+3 = 4$ |

The two dimensions add to $8 = \dim_{\mathbb{R}}\mathbb{B}$, and each factor carries two constituents of the same type: the first the non-compact scale and the non-compact boost, the second the compact phase and the compact rotor.

## Existence, Uniqueness and the Domain

### The Theorem

**Theorem (the Cartan pairing).** Let $\tilde{Q}\in\mathbb{B}$ with $\langle\tilde Q\rangle_{\natural}\neq0$. There are a unique $\tilde Q_H\in\mathbb{M}_+$ positive definite and a unique $\tilde Q_0\in \mathrm{U}(\mathbb{B})$ with $\tilde{Q} = \tilde Q_H\,\tilde Q_0$, and they are $\tilde Q_H = \sqrt{\tilde{Q}\tilde{Q}^{*}}$ and $\tilde Q_0 = \tilde Q_H^{-1}\tilde{Q}$.

### Uniqueness

The product $\tilde{Q}\tilde{Q}^{*}$ is Hermitian positive, and it is positive definite when the element is invertible; a positive definite Hermitian element has a unique positive definite Hermitian square root (*Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint*, §*The Polar Decomposition*), so $\tilde Q_H$ is unique. The second factor is then $\tilde Q_0 = \tilde Q_H^{-1}\tilde{Q}$, and it is $*$-unitary because $\tilde Q_0\,\tilde Q_0^{*} = \tilde Q_H^{-1}\tilde{Q}\tilde{Q}^{*}\tilde Q_H^{-1} = \tilde Q_H^{-1}\tilde Q_H^{2}\tilde Q_H^{-1} = e_t$. Both factors are functions of the element alone, and the pairing is unique within its domain.

### The Domain

The pairing is available on the whole complement of the null cone,

$$
\{\tilde{Q} : \langle\tilde Q\rangle_{\natural}\neq0\} ,
$$

which is the domain of the polar decomposition itself. The reason is that $\langle\tilde Q\rangle_{\natural} = \det\mathsf{M}_2(\tilde{Q})$, so the element is invertible exactly when its norm does not vanish, and an invertible element has a unique matrix polar decomposition. The Cartan pairing is the only one of the three whose construction needs no part of the element; the Hamilton representation and the quaternion construction fail on additional sets: the Hamilton axis cannot be normalised when the vector part is null, and the quaternion modulus cannot be constructed from $\tilde q_r$ when $\tilde q_r$ is not invertible.

### The Matrix Proof

In the matrix model the statement is the classical polar decomposition of an invertible complex matrix. For $\tilde{Q}$ with $\mathsf{M}_2(\tilde{Q})$ invertible, the matrix $(\mathsf{M}_2(\tilde{Q})\mathsf{M}_2(\tilde{Q})^{\dagger})^{1/2}$ is the unique positive definite Hermitian square root of $\mathsf{M}_2(\tilde{Q})\mathsf{M}_2(\tilde{Q})^{\dagger}$, and it is $\mathsf{M}_2(\tilde Q_H)$; the quotient $\mathsf{M}_2(\tilde Q_H)^{-1}\mathsf{M}_2(\tilde{Q})$ is $*$-unitary and is $\mathsf{M}_2(\tilde Q_0)$. Translating the two matrices back through the isomorphism $\mathbb{B}\cong\mathsf{M}_2(\mathbb{C})$ gives $\tilde Q_H$ and $\tilde Q_0$ above, the matrix adjoint $\dagger$ being the transport of the algebra conjugation ${}^{*}$. The proof is the matrix theorem and needs no separate existence argument.

## The Three Pairings

### The Three Bracketings

The four factors can be bracketed in exactly three ways, and each bracketing is a pairing. The table records the two factors and the norm each carries; the domains are the subject of the next subsection.

| pairing | first factor | second factor | norm of the first factor | norm of the second factor |
|---|---|---|---|---|
| Hamilton | $\Rho=r\exp(i\alpha)$, complex scalar | $\exp(\vec U\Theta)=\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ | $\Rho^{2}$ | $e_t$ |
| quaternion | $\tilde q=r\tilde u_{\mathrm r}$, real quaternion | $\exp(i\tilde\Psi)=\exp(i\alpha)\tilde u_{\mathrm r}^{-1}\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ | $r^{2}$ | $\exp(2i\alpha)$ |
| Cartan | $\tilde Q_H=r\tilde U_{\mathrm b}$, Hermitian positive | $\tilde Q_0=\exp(i\alpha)\tilde u_{\mathrm r}$, $*$-unitary | $r^{2}$ | $\exp(2i\alpha)$ |

The three rows split the same norm $\Rho^{2}=r^{2}\exp(2i\alpha)$ in three ways. The Cartan row splits it as the quaternion row does, but its first factor is Hermitian positive and its second $*$-unitary. The Hamilton row is the exception: it puts the whole norm in a central first factor. The three moduli are therefore a complex scalar, a real quaternion and a Hermitian positive element, and the four-factor word is their common reference.

### The Domains and the Witnesses

Five elements separate the cases. The Hamilton axis needs $B^{2}=\langle\vec Q,\vec Q\rangle_{\natural}\neq0$, the quaternion construction needs $\langle\tilde Q\rangle_{\natural}\neq0$ and $\tilde q_r\neq0$, and the Cartan pairing needs only $\langle\tilde Q\rangle_{\natural}\neq0$.

| element | $\langle\tilde Q\rangle_{\natural}$ | $\langle\vec Q,\vec Q\rangle_{\natural}$ | $\tilde q_r$ | Hamilton | quaternion construction | Cartan |
|---|---|---|---|---|---|---|
| $(1+i)e_t+\vec e_x+2\vec e_y$ | $5+2i$ | $5$ | $e_t+\vec e_x+2\vec e_y$ | yes | yes | yes |
| $1+\vec e_x+i\vec e_y$ | $1$ | $0$ | $1+\vec e_x$ | no | yes | yes |
| $i\vec e_x+i\vec e_y$ | $-2$ | $-2$ | $0$ | yes | no | yes |
| $i$ | $-1$ | $0$ | $0$ | no | no | yes |
| $e_t+i\vec e_x$ | $0$ | $-1$ | $e_t$ | no word | no word | no word |

The first line is the generic case. The second line separates the Hamilton pairing, the third the quaternion construction, and the fourth line is missed by both partial pairings and kept here. The fifth line is the null cone, where no word exists.

The two senses of partial are separated in the table.

| pairing | factorisation exists when | construction exists when |
|---|---|---|
| Hamilton | $\langle\tilde Q\rangle_{\natural}\neq0$ and $\langle\vec Q,\vec Q\rangle_{\natural}\neq0$ | the same |
| quaternion | $\langle\tilde Q\rangle_{\natural}\neq0$ | $\langle\tilde Q\rangle_{\natural}\neq0$ and $\tilde q_r\neq0$ |
| Cartan | $\langle\tilde Q\rangle_{\natural}\neq0$ | the same |

The Cartan row is partial in neither sense: both factors are functions of the element alone. The Hamilton row is partial in both, because its axis needs a non-null vector part; the quaternion row is partial in its construction only.

The Hamilton domain and the quaternion construction domain are not nested, and the Cartan domain contains both. Their union, together with the nonzero purely imaginary scalar elements, is the complement of the null cone: if $\tilde q_r=0$ then $Q_\mu=ib_\mu$ and $\langle\vec Q,\vec Q\rangle_{\natural}=-\sum_k b_k^2\le0$, so the two conditions fail together exactly on $\tilde Q=ib_0e_t$ with $b_0\neq0$.

### What This Pairing Carries

The Cartan row is the only one whose first factor is Hermitian positive and whose second factor is $*$-unitary. It is the matrix polar decomposition of the element, read in the algebra: the first factor is the positive square root of $\tilde Q\tilde Q^{*}$, and the second is $\tilde Q_H^{-1}\tilde Q$.

| claim | reason |
|---|---|
| the pairing loses nothing | both factors are functions of the element alone, $\tilde Q_H=\sqrt{\tilde Q\tilde Q^{*}}$ and $\tilde Q_0=\tilde Q_H^{-1}\tilde Q$ |
| its domain is the full domain | it is available on the whole complement of the null cone, whereas the Hamilton pairing needs a non-null vector part and the quaternion construction needs $\tilde q_r$ invertible |
| its factors are canonical | the two constituents of each factor commute, the phase being central, so each factor is a product of commuting exponentials |

The non-commutativity of the boost and the rotor shows up only between the two factors, and it is the reason the pairing is interesting.

## Behaviour Under the Three Conjugations

### The Three Conjugations

The algebra has three nontrivial conjugations: the quaternion conjugation ${}^{\natural}$, the anti-automorphism fixing the centre $\mathbb{C}_{\mathbb{B}}$; the coefficientwise conjugation $\bar{\cdot}$, the automorphism conjugating every coefficient; and the Hermitian conjugation ${}^{*} = {}^{\natural}\circ\bar{\cdot}$, the composite. The three act on the pairing in three different ways, and the difference is the difference between preserving the order and reversing it: the coefficientwise conjugation is an automorphism and keeps the order of the two factors, while the quaternion and the Hermitian conjugations are anti-automorphisms and reverse it.

### The Quaternion Conjugation

The quaternion conjugation reverses the order and does not touch the coefficients, so $\tilde{Q}^{\natural} = \tilde Q_0^{\natural}\tilde Q_H^{\natural}$; the two factors of $\tilde{Q}^{\natural}$ are the conjugates of the two factors of $\tilde{Q}$, taken in the reversed order. In the Cartan shape the first factor is $\tilde Q_0^{\natural}\tilde Q_H^{\natural}\tilde Q_0^{\natural*}$ and the second is $\tilde Q_0^{\natural}$, the conjugations of the two factors with the order restored by a conjugation.

### The Coefficientwise Conjugation

The coefficientwise conjugation is an automorphism and keeps the order, so $\overline{\tilde{Q}} = \overline{\tilde Q_H}\,\overline{\tilde Q_0}$ is already the Cartan shape: the first factor $\overline{\tilde Q_H} = r\tilde U_{\mathrm b}^{\natural}$ is Hermitian positive and the second $\overline{\tilde Q_0} = \exp(-i\alpha)\tilde u_{\mathrm r}$ is $*$-unitary, the real quaternion rotor being unchanged by the coefficientwise conjugation. The coefficientwise conjugation is therefore the one that preserves the pairing without a change of order.

| conjugation | first factor of the conjugate | second factor of the conjugate | order |
|---|---|---|---|
| ${}^{\natural}$ | $\tilde Q_0^{\natural}\tilde Q_H^{\natural}\tilde Q_0^{\natural*}$ | $\tilde Q_0^{\natural}$ | restored by a conjugation |
| $\bar{\cdot}$ | $\overline{\tilde Q_H} = r\tilde U_{\mathrm b}^{\natural}$ | $\overline{\tilde Q_0} = \exp(-i\alpha)\tilde u_{\mathrm r}$ | preserved |
| ${}^{*}$ | $\tilde Q_0^{*}\tilde Q_H\,\tilde Q_0$ | $\tilde Q_0^{*}$ | restored by a conjugation |

The two anti-automorphisms behave in the same way, each with its own conjugation of the Hermitian factor, and the automorphism is the exceptional one that needs no conjugation at all.

### The Hermitian Conjugation

The anti-automorphism reverses the order, and the computation is that of §*The Reversed Word*: the two factors of $\tilde{Q}^{*}$ in the Cartan shape are $\tilde Q_0^{*}\tilde Q_H\,\tilde Q_0$, Hermitian positive, and $\tilde Q_0^{*}$, $*$-unitary. Both factors change: the pairing is not a regrouping of the two factors of $\tilde{Q}$, because a Hermitian and a $*$-unitary element multiplied in the other order need not be the same element.

## The Hermitian and the Anti-Hermitian Exponents

### The Two Exponents

The pairing is a **Hermitian pairing** because the two exponents of its factors lie in the two involutive subspaces. Writing the exponents of the definition,

$$
\tilde Q_H = \exp(\mathcal H) , \qquad \mathcal H = \ln r\,e_t + i\tfrac{\psi}{2}\vec u_{\mathrm b} , \qquad \tilde Q_0 = \exp(\mathcal K) , \qquad \mathcal K = i\alpha\,e_t + \tfrac{\theta}{2}\vec u_{\mathrm r} ,
$$

the first exponent has a real scalar part $\ln r$ and a purely imaginary vector part $i\tfrac{\psi}{2}\vec u_{\mathrm b}$, and the second has a purely imaginary scalar part $i\alpha$ and a real vector part $\tfrac{\theta}{2}\vec u_{\mathrm r}$. The two exponents are therefore of the two opposite kinds.

| exponent | scalar part | vector part | subspace | related factor |
|---|---|---|---|---|
| $\mathcal H = \ln r\,e_t + i\tfrac{\psi}{2}\vec u_{\mathrm b}$ | real | purely imaginary | $\mathbb{M}_+$, Hermitian | $\tilde Q_H = \exp \mathcal H$, Hermitian positive |
| $\mathcal K = i\alpha\,e_t + \tfrac{\theta}{2}\vec u_{\mathrm r}$ | purely imaginary | real | $\mathbb{M}_-$, anti-Hermitian | $\tilde Q_0 = \exp \mathcal K$, $*$-unitary |

The first exponent is the sum of two Hermitian terms, $(\ln r)e_t\in\mathbb{M}_+$ and $i\tfrac{\psi}{2}\vec u_{\mathrm b}\in\mathbb{M}_+$; the second is the sum of two anti-Hermitian terms, $i\alpha\,e_t\in\mathbb{M}_-$ and $\tfrac{\theta}{2}\vec u_{\mathrm r}\in\mathbb{M}_-$. The split of the four factors two and two is the split of the four exponents two and two, and it is exactly the Cartan grouping. The two exponents do not commute in general, so the element is not the exponential of their sum; the two factors are computed from the element and not by adding the four exponents of the companion article.

### The Factors Are Not the Sectors

The two exponents lie in the two subspaces, but the two **factors** do not. The Hermitian exponent exponentiates to a Hermitian positive element, and the anti-Hermitian exponent exponentiates to a $*$-unitary element; the anti-Hermitian object of the pair is therefore the logarithm $\ln \tilde Q_0 = \mathcal K$, not the factor $\tilde Q_0$ itself. The distinction is worth stating because the two sectors $\mathbb{M}_+$ and $\mathbb{M}_-$ are linear subspaces and the second factor is not.

| object | Hermitian? | anti-Hermitian? | where it lies |
|---|---|---|---|
| $\mathcal H = \ln \tilde Q_H$ | yes | no | $\mathbb{M}_+$ |
| $\tilde Q_H = \exp \mathcal H$ | yes, and positive | no | $\mathbb{M}_+$, the positive cone |
| $\mathcal K = \ln \tilde Q_0$ | no | yes | $\mathbb{M}_-$ |
| $\tilde Q_0 = \exp \mathcal K$ | not in general | not in general | $\mathrm{U}(\mathbb{B})$, not a subspace |

The Hermitian factor $\exp \mathcal H$ is the exponential of a Hermitian element of one sign, the positive one; the $*$-unitary factor $\exp \mathcal K$ is the exponential of an anti-Hermitian element of compact type. This is the same asymmetry that the matrix polar decomposition exhibits between the positive definite factor and the $*$-unitary factor.

### The Matrix Reading

In the matrix model the two exponents are the Hermitian and the anti-Hermitian matrices of the algebra,

$$
\mathsf{M}_2(\mathcal H)^{*} = \mathsf{M}_2(\mathcal H) , \qquad \mathsf{M}_2(\mathcal K)^{*} = -\mathsf{M}_2(\mathcal K) ,
$$

and the split is the Cartan decomposition of the algebra as a real Lie algebra under the commutator,

$$ \mathfrak{gl}(2,\mathbb{C}) = \mathfrak{u}(2) \oplus \mathfrak{p} , \qquad \mathfrak{u}(2) = \mathfrak{su}(2)\oplus i\mathbb{R} , \qquad \mathfrak{p} = \{\text{Hermitian matrices}\}. $$

The compact summand $\mathfrak{u}(2)$ is spanned by the anti-Hermitian elements, the anti-Hermitian scalar $ie_t$ and the anti-Hermitian vectors $\tfrac{\theta}{2}\vec u_{\mathrm r}$; the non-compact summand $\mathfrak{p}$ is spanned by the Hermitian elements, the real scalar $\ln r\,e_t$ and the Hermitian vectors $i\tfrac{\psi}{2}\vec u_{\mathrm b}$. The two summands are of real dimension four each, and their sum is the real dimension $8$ of the algebra. The exponent of $\mathfrak{u}(2)$ is the $*$-unitary group $\mathrm{U}(2)$ and the exponent of $\mathfrak{p}$ is the positive cone of the Hermitian elements, so the Cartan decomposition of the algebra reads the pairing at the level of the group.

## The Cartan Decomposition of the Unit Group

### The Unit-Norm Case

For an element of unit norm, $\langle\tilde Q\rangle_{\natural} = e_t$, the scale and the phase are trivial, $r = 1$ and $\exp(i\alpha) = e_t$, and the Cartan pairing reduces to the product of the boost and the rotor,

$$
\boxed{\;\tilde{Q} = \tilde U_{\mathrm b}\,\tilde u_{\mathrm r} , \qquad \tilde U_{\mathrm b}\in\mathbb{M}_+ , \quad \tilde U_{\mathrm b}^{*} = \tilde U_{\mathrm b} , \quad \tilde u_{\mathrm r}\in\mathrm{Sp}(1)\;}.
$$

This is the **Cartan decomposition** of the unit group, $SL(2,\mathbb{C}) = \exp(\mathfrak{p}_0)SU(2)$ with $\mathfrak{p}_0=\mathfrak{p}\cap\mathfrak{sl}(2,\mathbb{C})$ the traceless Hermitian elements, read in the algebra: the unit-norm elements are the products of a Hermitian positive element of determinant one and an element of the maximal compact subgroup $SU(2) = \mathrm{Sp}(1)$.

### The Physical Interpretation

In the physics articles the unit-norm element is a Lorentz rotor, the Hermitian positive factor is a pure boost and the $*$-unitary real quaternion is a spatial rotation; the pairing is then the statement that every element of the restricted Lorentz group is a boost times a rotation, in that order. The two factors land in the two involutive sectors: the boost in the Hermitian subspace $\mathbb{M}_+$, which the physics articles call the informational sector, and the rotor's exponent in the anti-Hermitian subspace $\mathbb{M}_-$, which they call the material sector. The pairing is the algebraic home of the composition of a boost and a rotation, and the non-commutativity of the boosts is the reason the product of two boosts is a boost and a rotation and not a pure boost. The group statement is developed in *The Lorentz Group in Biquaternionic Form — Structure and Representations*.

## The Published Form of the Pairing

The pairing $\tilde Q_H\,\tilde Q_0$ is the factorisation proved by Sangwine and Hitzer for the unit semi-norm elements and, in the general case, by their Corollary 1, in the reversed word, angle first:

$$
\boxed{\;\tilde{Q} = |\tilde{Q}|\,\exp(\hat\alpha\theta_t)\,\exp(I\hat\beta\theta_\mathcal H)\;},
$$

with two pure real unit quaternions $\hat\alpha$ and $\hat\beta$ (the hats avoid the phase $\alpha$), a pure imaginary unit biquaternion $I\hat\beta$ (with $I$ an imaginary unit), and two real angles $\theta_t$ and $\theta_\mathcal H$. Translating their letters into those of the corpus, the trigonometric exponential $\exp(\hat\alpha\theta_t)$ is the rotor $\tilde u_{\mathrm r} = \exp(\tfrac{\theta}{2}\vec u_{\mathrm r})$, the hyperbolic exponential $\exp(I\hat\beta\theta_\mathcal H)$ is the boost about the axis rotated by the rotor, that is, the boost conjugated by the rotor, and their product is the boost followed by the rotor. Three differences are worth recording.

| difference | Sangwine–Hitzer | this article |
|---|---|---|
| order | angle first, $\exp(\hat\alpha\theta_t)\exp(I\hat\beta\theta_\mathcal H)$ | boost first, $\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ |
| count | $2+3+3=8$, the complex modulus kept whole | $1+1+3+3=8$, the phase split off |
| branch and uniqueness | neither stated; both orders admitted | $\alpha\in(-\pi/2,\pi/2]$; unique on the domain |

The mathematics of the pairing is the same in both places; what the corpus adds is the split of the modulus into a scale and a phase, the branch, and the uniqueness.

## Worked Examples

The examples are collected in the table, with the two factors and the norm of the first. The subsections give the computations.

| element | $\tilde Q_H$ | $\tilde Q_0$ | $\langle\tilde Q_H\rangle_{\natural}$ |
|---|---|---|---|
| $(1+i)e_t+\vec e_x+2\vec e_y$ | $2.488490\,e_t-0.401850\,i\,\vec e_x-0.803700\,i\,\vec e_y$ | $(0.462101+0.088993i)e_t+(0.387479+0.074622i)\vec e_x+(0.774959+0.149243i)\vec e_y$ | $5.385165$ |
| $1+\vec e_x+i\vec e_y$ | $1.414214\,e_t+0.707107\,i\,\vec e_y+0.707107\,i\,\vec e_z$ | $0.707107\,(e_t+\vec e_x)$ | $2$ |
| $i\vec e_x+i\vec e_y$ | $\sqrt{2}\,e_t$ | $i\,(\vec e_x+\vec e_y)/\sqrt{2}$ | $2$ |
| $i$ | $e_t$ | $i$ | $1$ |

### The Generic Element

Take $\tilde{Q} = (1+i)e_t+\vec e_x+2\vec e_y$, the worked example of the companion article. Its polar decomposition, computed there, is

$$
r = 2.320595787 , \quad \alpha = 0.190253189 , \quad \tilde U_{\mathrm b} = 1.072349609\,e_t - 0.173166789\,i\,\vec e_x - 0.346333577\,i\,\vec e_y , \quad \tilde u_{\mathrm r} = 0.470592172\,e_t+0.394599292\,\vec e_x+0.789198585\,\vec e_y .
$$

The Cartan pairing is

$$
\tilde Q_H = r\tilde U_{\mathrm b} = 2.488489985\,e_t - 0.401850120\,i\,\vec e_x - 0.803700241\,i\,\vec e_y ,
$$

Hermitian positive with $\langle\tilde Q_H\rangle_{\natural} = r^{2} = 5.385164807$, and

$$
\tilde Q_0 = \exp(i\alpha)\tilde u_{\mathrm r} = (0.462100989+0.088992519i)e_t + (0.387479295+0.074621694i)\vec e_x + (0.774958590+0.149243388i)\vec e_y .
$$

The first factor is Hermitian positive and the second is $*$-unitary, and the two are the two halves of the same four-factor word.

### The Element with a Null Vector Part

Take $\tilde{Q} = 1+\vec e_x+i\vec e_y$. Then $\langle\tilde Q\rangle_{\natural} = 1$ and $\langle\vec Q,\vec Q\rangle_{\natural} = 0$, so the Hamilton representation does not exist; the Cartan pairing does, with

$$
r = 1 , \qquad \alpha = 0 , \qquad \tilde Q_H = \tilde U_{\mathrm b} = 1.414213562\,e_t + 0.707106781\,i\,\vec e_y + 0.707106781\,i\,\vec e_z , \qquad \tilde Q_0 = \tilde u_{\mathrm r} = 0.707106781\,(e_t+\vec e_x) .
$$

The first factor is Hermitian positive and the second is $*$-unitary, and the element is the non-scalar witness of the quaternion pairing of the companion article.

### The Element with a Vanishing Real Part

Take $\tilde{Q} = i\vec e_x+i\vec e_y$. Then $\langle\tilde Q\rangle_{\natural} = -2$ and $\tilde q_r = 0$, so the construction of the quaternion pairing from the parts of the element fails; the Cartan pairing does not, and reads

$$
r = \sqrt{2} , \qquad \alpha = \frac{\pi}{2} , \qquad \tilde U_{\mathrm b} = e_t , \qquad \tilde u_{\mathrm r} = \frac{\vec e_x+\vec e_y}{\sqrt{2}} , \qquad \tilde Q_H = \sqrt{2}\,e_t , \qquad \tilde Q_0 = i\,\frac{\vec e_x+\vec e_y}{\sqrt{2}} .
$$

The first factor is the positive scalar $\sqrt{2}e_t$, Hermitian positive, and the second is the $*$-unitary imaginary quaternion $i(\vec e_x+\vec e_y)/\sqrt2$; their product is $\tilde{Q}$.

### The Scalar Imaginary

Take $\tilde{Q} = i$. Then $\langle\tilde Q\rangle_{\natural} = -1$, the element is invertible and the polar decomposition is $i = 1\cdot \exp(i\pi/2)\cdot e_t\cdot e_t$. The Cartan pairing reads $i = e_t\cdot i$, with $\tilde Q_H = e_t$ Hermitian positive and $\tilde Q_0 = i$ $*$-unitary: the central phase of the polar decomposition is absorbed into the $*$-unitary factor, which is the grouping that defines the Cartan pairing. The example is the clearest single illustration of the difference between having a pairing and being able to construct the modulus of a partial representation from the parts of the element.

## Summary

### Main Results

| item | result |
|---|---|
| domain | $\langle\tilde Q\rangle_{\natural}\neq0$ |
| first factor | $\tilde Q_H=r\tilde U_{\mathrm b}=\sqrt{\tilde Q\tilde Q^{*}}$, Hermitian positive |
| second factor | $\tilde Q_0=\exp(i\alpha)\tilde u_{\mathrm r}=\tilde Q_H^{-1}\tilde Q$, $*$-unitary |
| equation | $\tilde Q=\tilde Q_H\tilde Q_0$, with $\tilde Q\tilde Q^{*}=\tilde Q_H^{2}$ |
| uniqueness | unique on the complement of the null cone |
| complex conjugation | order preserved, both factors conjugate |
| quaternion conjugation | order reversed, both factors conjugate |
| Hermitian conjugation | order reversed, factors $\tilde Q_0^{*}\tilde Q_H\tilde Q_0$ and $\tilde Q_0^{*}$ |
| degenerate limits | none: the pairing exists on the whole complement of the null cone |
| classical case | the matrix polar decomposition |
| unit-norm case | the Cartan decomposition $\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ of the unit group |

The Cartan pairing groups the scale with the boost into the Hermitian positive factor $\tilde Q_H=r\tilde U_{\mathrm b}$ and the phase with the rotor into the $*$-unitary factor $\tilde Q_0=\exp(i\alpha)\tilde u_{\mathrm r}$. The first is the positive square root of $\tilde Q\tilde Q^{*}$, the second is $\tilde Q_H^{-1}\tilde Q$, and the pairing solves the single equation $\tilde Q\tilde Q^{*}=\tilde Q_H^{2}$. Both factors are functions of the element alone, and both are defined on the whole complement of the null cone. The Hamilton pairing is partial in both senses; the quaternion pairing is partial in its construction only; the Cartan pairing is total in both.

The pairing is Hermitian because the exponents of its factors lie in the two involutive subspaces: $\ln\tilde Q_H=\ln r\,e_t+i\frac{\psi}{2}\vec u_{\mathrm b}$ is Hermitian and $\ln\tilde Q_0=i\alpha\,e_t+\frac{\theta}{2}\vec u_{\mathrm r}$ is anti-Hermitian. This is the Cartan decomposition $\mathfrak{gl}(2,\mathbb{C})=\mathfrak{u}(2)\oplus\mathfrak{p}$. The factors themselves are not the sectors: the anti-Hermitian object is the logarithm of the second factor, not the second factor. In the unit-norm case the scale and the phase are trivial and the pairing becomes the Cartan decomposition $\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ of the unit group.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde{Q} = r \exp(i\alpha)\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ | the polar decomposition, four factors |
| $r$, $\exp(i\alpha)$, $\tilde U_{\mathrm b}$, $\tilde u_{\mathrm r}$ | scale, central phase, Hermitian positive boost, unit real quaternion rotor |
| $\tilde{Q} = \tilde Q_H \tilde Q_0$ | the Cartan pairing, two factors |
| $\tilde Q_H = r\tilde U_{\mathrm b}$ | the Hermitian positive factor, or first factor |
| $\tilde Q_0 = \exp(i\alpha)\tilde u_{\mathrm r}$ | the $*$-unitary factor, or second factor |
| $\Rho = r\exp(i\alpha)$, $\vec U$, $\Theta$ | the Hamilton modulus, its axis and its complex angle |
| $\lambda_\pm = Q_t\pm iB = \Rho\exp(\pm i\Theta)$ | the eigenvalues of $\tilde Q$, the coefficients of its eigenvalue decomposition |
| $\tilde q = r\tilde u_{\mathrm r}$, $\tilde\Psi$ | the quaternion modulus and the quaternion angle of the quaternion pairing |
| $\langle\tilde Q_H\rangle_{\natural} = r^{2}$ | the norm of the first factor, the squared scale |
| $\vec Q = Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ | the vector part of $\tilde{Q}$ |
| $\langle\vec Q,\vec Q\rangle_{\natural} = Q_x^2+Q_y^2+Q_z^2$ | the quaternionic bilinear square of the vector part |
| $\tilde q_r$ | the real quaternion part of $\tilde{Q}$, the element with the real parts of the four coefficients |
| $\mathbb{M}_\pm = \{\tilde{Q} : \tilde{Q}^{*} = \pm\tilde{Q}\}$ | the Hermitian and the anti-Hermitian subspaces |
| $\mathrm{U}(\mathbb{B})\cong \mathrm{U}(2)\cong \mathrm{U}(1)\cdot\mathrm{Sp}(1)$ | the $*$-unitary group of the algebra, home of the second factor |
| $\mathcal H = \ln \tilde Q_H = \ln r\,e_t + i\tfrac{\psi}{2}\vec u_{\mathrm b}$ | the Hermitian exponent, in $\mathbb{M}_+$ |
| $\mathcal K = \ln \tilde Q_0 = i\alpha\,e_t + \tfrac{\theta}{2}\vec u_{\mathrm r}$ | the anti-Hermitian exponent, in $\mathbb{M}_-$ |
| $\psi$, $\vec u_{\mathrm b}$ | rapidity and unit axis of the boost |
| $\theta$, $\vec u_{\mathrm r}$ | rotation angle and unit axis of the rotor |
| ${}^{\natural}$, $\bar{\cdot}$, ${}^{*}$ | quaternion, coefficientwise and Hermitian conjugation |
| $\mathsf{M}_2$ | the matrix model $\mathbb{B}\cong\mathsf{M}_2(\mathbb{C})$ |

## Further Reading

- [The Biquaternion Eigenvalue Decomposition](the-biquaternion-eigenvalue-decomposition.html), §*The Eigenvalues*, for the eigenvalues $\lambda_\pm=\Rho\exp(\pm i\Theta)$ and the pure unit element $\vec U=\vec Q/B$ of the Hamilton row.
- [Biquaternion Elementary Functions](biquaternion-elementary-functions.html), for the exponential, the logarithm and the principal branch that fix the two exponents of the pairing.
- [Exponential Polar Decomposition of a N-Regular, Spectrally Regular Biquaternion](exponential-polar-decomposition-of-an-n-regular-spectrally-regular-biquaternion.html), for the four exponentials and the existence and uniqueness of the word whose two halves the pairing regroups.
- [The Polar Decomposition of a N-Regular Biquaternion](the-polar-decomposition-of-an-n-regular-biquaternion.html), for the four factors, the modulus $\Rho = \sqrt{\langle\tilde Q\rangle_{\natural}}$, the exponential trichotomy and the domain.
- [The Hamilton Root Pairing of the Polar Decomposition of a N-Regular, Spectrally Regular Biquaternion](the-hamilton-root-pairing-of-the-polar-decomposition-of-a-n-regular-spectrally-regular-biquaternion.html) and [The Quaternion Pairing of the Polar Decomposition of a N-Regular, Spectrally Regular Biquaternion](the-quaternion-pairing-of-the-polar-decomposition-of-a-n-regular-spectrally-regular-biquaternion.html), for the Hamilton and quaternion pairings, the two partial pairings whose moduli are constructed from the parts of the element.
- [Hermitian and Skew-Hermitian Elements](hermitian-and-skew-hermitian-elements.html), for the involutive split $\mathbb{B} = \mathbb{M}_+\oplus\mathbb{M}_-$ and the two sectors.
- [The Unitary Group of the Biquaternion Algebra](the-unitary-group-of-the-biquaternion-algebra.html), for $\mathrm{U}(\mathbb{B})\cong \mathrm{U}(2)$ and the structure of the $*$-unitary elements.
- [Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint](positivity-and-the-hermitian-cone-of-the-biquaternion-algebra-with-hermitian-adjoint.html), for the positive cone of the Hermitian elements in which the first factor lies.
- [$M_2(\mathbb{C})$ Representation : The Conjugations and the Adjoints](m2c-representation-the-conjugations-and-the-adjoints.html), for the isomorphism $\mathbb{B}\cong\mathsf{M}_2(\mathbb{C})$ and the transport of the conjugation ${}^{*}$ to the matrix adjoint.
- [The Lorentz Group in Biquaternionic Form — Structure and Representations](../articles_physics/the-lorentz-group-in-biquaternionic-form-structure-and-representations.html), for the unit-norm case $\tilde Q_0 = \tilde U_{\mathrm b}\tilde u_{\mathrm r}$, the boost and the rotation of the physical interpretation.
- *The Polar Decomposition in Subspaces*, for the Cartan pairing restricted to the remarkable subspaces of the algebra.
- [The Polar Decomposition and Remarkable Subspaces](the-polar-decomposition-and-remarkable-subspaces.html), for the same restriction in the algebra: the four exponents against the four coordinate blocks and the six subspaces, the incidence of the exponents with the subspaces, and the polar data each subspace carries.
- [The Polar Decomposition of a N-Degenerate Biquaternion](the-polar-decomposition-of-an-n-degenerate-biquaternion.html), for the extension of this pairing to the cone, the partial isometry that replaces the $*$-unitary factor there and the scaled idempotent that replaces the positive factor.
- S. J. Sangwine and E. Hitzer, "Polar decomposition of complexified quaternions and octonions", *Advances in Applied Clifford Algebras* (2020), DOI 10.1007/s00006-020-1048-y; technical report CES-535, University of Essex (2019), for Theorem 1 and Corollary 1, the published form of the pairing.
