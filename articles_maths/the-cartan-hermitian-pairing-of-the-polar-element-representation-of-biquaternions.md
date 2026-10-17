# __The Cartan Hermitian Pairing of the Polar Element Representation of Biquaternions__

## Introduction

**The Cartan Hermitian pairing** of the polar element representation is the grouping of the four factors that multiplies the scale into the boost and the phase into the rotor,

$$
\tilde{Q} = H\,U , \qquad H = r\,\tilde U_{\mathrm b} , \qquad U = \exp(i\alpha)\,\tilde u_{\mathrm r} .
$$

The two factors are of two different kinds. The first, $H$, is **Hermitian and positive**; the second, $U$, is **unitary**. The pairing is therefore the matrix polar decomposition of the biquaternion, read in the algebra, and it is the form of the polar word that the physics articles use for a unit-norm Lorentz rotor. It is called the **Cartan pairing** here because the two exponents of its factors lie in the two summands of the Cartan decomposition of the algebra as a real Lie algebra, one Hermitian and one anti-Hermitian; the Hermitian split of the exponents, and not the mere grouping of the factors, is what the name records.

The reference article of the series, *The Polar Element Representation of Biquaternions*, gives the polar word $\tilde{Q} = r\,\exp(i\alpha)\tilde U_{\mathrm b}\tilde u_{\mathrm r}$, with a positive real scale $r$, a central phase $\exp(i\alpha)$ on the branch $\alpha\in(-\tfrac{\pi}{2},\tfrac{\pi}{2}]$, a Hermitian positive unit-norm boost $\tilde U_{\mathrm b}$ and a unit real quaternion rotor $\tilde u_{\mathrm r}$; its four factors have three pairings, and the present article treats the one above.

**The approach.** The article establishes four things, in this order. The pairing and the algebra of its two factors are stated, and the equation it solves is computed, $\tilde{Q}\tilde{Q}^{*} = H^{2}$. The Hermitian positive factor and the unitary factor are described, each on its own, with the scale and the boost in the first and the phase and the rotor in the second. The two exponents are separated into their Hermitian and their anti-Hermitian parts, which is the Cartan decomposition of the algebra and the precise sense in which the pairing is a Hermitian pairing. The existence, the uniqueness and the domain of the pairing follow from the matrix polar decomposition, and the relation to the polar representation and to the two partial regroupings closes the account.

**The result, in one sentence.** For every biquaternion with $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}\neq0$ the word $\tilde{Q} = HU$ is unique with $H$ Hermitian positive and $U$ unitary; the first factor is the Hermitian positive square root $H = \sqrt{\tilde{Q}\tilde{Q}^{*}}$, the second is $U = H^{-1}\tilde{Q}$, the two exponents $\ln H$ and $\ln U$ lie in the Hermitian subspace $\mathbb{M}_+$ and the anti-Hermitian subspace $\mathbb{M}_-$ respectively, and the pairing is the matrix polar decomposition of $\mathsf{M}_2(\tilde{Q})$.

The pairing is the third of the three pairings of the four factors. The other two call a composite object the modulus and are available only where that object can be constructed from the parts of the element; they are *The Hamilton Root Pairing of the Polar Element Representation of Biquaternions* and *The Quaternion Pairing of the Polar Element Representation of Biquaternions*. The present pairing is **not** partial: it loses nothing, it is available on the whole complement of the null cone, and both of its factors are functions of the element alone. The unit-norm case, in which the scale and the phase are trivial, is the Cartan decomposition $\tilde{Q} = \tilde U_{\mathrm b}\tilde u_{\mathrm r}$ of the unit group, and the physical interpretation of the two factors is the Lorentz boost and the spatial rotation.

The article assumes the algebra, the four factors and the domain of the polar representation from the companion article and does not re-derive them. It is not the four-factor representation itself, and it is not the operator polar decomposition of *The Polar Decomposition of an Operator of the Form*, a different statement about a Tomita operator on a completion. No physics is invoked; the physical interpretation is recorded where it clarifies the algebra.

**Conventions.** $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has the basis $e_t,\vec e_x,\vec e_y,\vec e_z$ with $\vec e_x\vec e_y = \vec e_z$ and the central scalar imaginary $i$, $i^2 = -1$. An element is $\tilde{Q} = \sum_{\mu\in\{t,x,y,z\}}Q_\mu e_\mu = Q_te_t+\vec Q$ with $\vec Q = \sum_{k=1}^{3}Q_k\vec e_k$ and $Q_\mu\in\mathbb{C}$; the quaternion conjugation is $\tilde{Q}^{\natural} = Q_te_t-\vec Q$, the coefficientwise conjugation is $\overline{\tilde{Q}} = \overline{Q_t}e_t+\overline{\vec Q}$, and the Hermitian conjugation is $\tilde{Q}^{*} = \overline{\tilde{Q}^{\natural}}$, so that ${}^{*} = {}^{\natural}\circ\bar{\cdot}$ and the two operations commute. The norm of the polar series is $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = \sum_{\mu\in\{t,x,y,z\}}Q_\mu^{2}$, a complex number in general, and the domain of the representation is $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}\neq0$. The Hermitian and the anti-Hermitian subspaces are $\mathbb{M}_\pm = \{\tilde{Q} : \tilde{Q}^{*} = \pm\tilde{Q}\}$, and the unitary group of the algebra is $\mathrm{U}(\mathbb{B}) = \{\tilde{U} : \tilde{U}^{*}\tilde{U} = e_t\}$. The symbols $r$, $\exp(i\alpha)$, $\tilde U_{\mathrm b}$, $\tilde u_{\mathrm r}$, $\rho = r\exp(i\alpha)$, $\langle\cdot\rangle_{\natural}$ and $\mathbb{M}_\pm$ are those of the companion article, whose Hamilton axis keeps its glyph $\vec\Xi$. The first factor of the pairing is written $H$ and the unitary factor $U$.

## The Pairing

### The Definition

The **Cartan pairing** of the polar representation is the regrouping in which the scale and the boost form the first factor and the phase and the rotor the second:

$$
\tilde{Q} = H\,U , \qquad H = r\,\tilde U_{\mathrm b} \in \mathbb{M}_+ , \qquad U = \exp(i\alpha)\,\tilde u_{\mathrm r} \in \mathrm{U}(\mathbb{B}) .
$$

The first factor is a positive real times a Hermitian positive unit-norm element, hence Hermitian positive; the second is a central phase times a unit real quaternion, hence unitary. The word is the polar word with the two parentheses inserted after the boost, and the two non-central factors keep their order: the boost stays on the left of the rotor, and no conjugation appears.

### The Equation the Pairing Solves

The pairing is the solution of one equation. Multiplying the element by its Hermitian conjugate and using that ${}^{*}$ is an anti-automorphism, that the central phase is central and that the rotor satisfies $\tilde u_{\mathrm r}\tilde u_{\mathrm r}^{*} = e_t$,

$$
\tilde{Q}\tilde{Q}^{*} = \bigl(r \exp(i\alpha)\tilde U_{\mathrm b}\tilde u_{\mathrm r}\bigr)\bigl(r \exp(-i\alpha)\tilde u_{\mathrm r}^{*}\tilde U_{\mathrm b}^{*}\bigr) = r^{2}\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r}\tilde u_{\mathrm r}^{*}\,\tilde U_{\mathrm b}^{*} = r^{2}\tilde U_{\mathrm b}^{2} = H^{2} ,
$$

using the Hermitian character $\tilde U_{\mathrm b}^{*} = \tilde U_{\mathrm b}$ of the boost. The product $\tilde{Q}\tilde{Q}^{*}$ is therefore the **square of the first factor**, and the first factor is recovered from the element by a square root,

$$
H = \sqrt{\tilde{Q}\tilde{Q}^{*}} .
$$

This is the only equation the pairing solves directly; the second factor follows from the first by division.

### The Second Factor Is the Element Divided by the First

Because $H = r\tilde U_{\mathrm b}$ is the polar modulus of the element and is invertible, the second factor is

$$
U = H^{-1}\tilde{Q} .
$$

Its inverse is $\tfrac{1}{r}\tilde U_{\mathrm b}^{\natural}$, since $\tilde U_{\mathrm b}^{-1} = \tilde U_{\mathrm b}^{\natural}$ for a unit-norm boost; substituting the polar word, the second factor is therefore $U = \tfrac{1}{r}\tilde U_{\mathrm b}^{\natural}\tilde{Q} = \exp(i\alpha)\tilde u_{\mathrm r}$, unitary as it must be. The two relations $H = \sqrt{\tilde{Q}\tilde{Q}^{*}}$ and $U = H^{-1}\tilde{Q}$ recover the whole pairing from the element, and they are the reason the pairing needs no construction external to the algebra.

### The Reversed Word

The Hermitian conjugate of the element is not the product of the two factors in the other order,

$$
\tilde{Q}^{*} = U^{*}H^{*} = U^{*}H ,
$$

which is $U^{*}H$ and not $HU^{*}$ or $HU$, because the boost and the rotor do not commute and the conjugation reverses the order. Combining the two displays, $\tilde{Q}^{*}$ is the conjugate of the first factor by the second on the left and by its inverse on the right,

$$
\tilde{Q}^{*} = \bigl(U^{*}HU\bigr)U^{*} ,
$$

and the two factors of $\tilde{Q}^{*}$ in the Cartan shape are therefore $U^{*}HU$, Hermitian positive, and $U^{*}$, unitary. The pairing of the conjugate element is a regrouping of the two factors of $\tilde{Q}$ only in this conjugated sense.

### The Two Factors Are Exponentiated

The two factors are the two **exponentials** of the two halves of the word. With the rapidity $\psi\ge0$ and unit axis $\vec u_{\mathrm b}$ of the boost, and the rotation angle $\theta\in[0,2\pi]$ and unit axis $\vec u_{\mathrm r}$ of the rotor,

$$
H = \exp\Bigl(\ln r\,e_t + i\tfrac{\psi}{2}\vec u_{\mathrm b}\Bigr) , \qquad U = \exp\Bigl(i\alpha\,e_t + \tfrac{\theta}{2}\vec u_{\mathrm r}\Bigr) .
$$

The first exponent collects the logarithms of the scale and the boost, the second those of the phase and the rotor. The pairing is a grouping of the four factors as exponentials, and the two exponents do not commute in general, so the pairing is not the exponential of a sum; the two exponentials above are computed from the element and not by adding the four exponents of the companion article.

## The Hermitian Positive Factor

### The Hermitian Subspace

The Hermitian conjugation ${}^{*}$ is an involution, so the algebra splits into its fixed space and its anti-fixed space,

$$
\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_- , \qquad \mathbb{M}_\pm = \{\tilde{Q} : \tilde{Q}^{*} = \pm\tilde{Q}\} .
$$

| subspace | condition | scalar part | vector part | matrix model | role |
|---|---|---|---|---|---|
| $\mathbb{M}_+$ | $\tilde{Q}^{*} = \tilde{Q}$ | real | purely imaginary | Hermitian matrices | the boosts and the scales |
| $\mathbb{M}_-$ | $\tilde{Q}^{*} = -\tilde{Q}$ | purely imaginary | real | anti-Hermitian matrices | the four-vectors and the exponents |

The first factor of the Cartan pairing is the element $H = r\tilde U_{\mathrm b} = r\cosh\tfrac{\psi}{2}\,e_t + ir\sinh\tfrac{\psi}{2}\,\vec u_{\mathrm b}$: its scalar part $r\cosh\tfrac{\psi}{2}$ is real and its vector part $ir\sinh\tfrac{\psi}{2}\,\vec u_{\mathrm b}$ is purely imaginary, so $H$ lies in $\mathbb{M}_+$.

### Positivity

The first factor is not merely Hermitian: it is **positive**. In the matrix model $\mathsf{M}_2(H)$ is Hermitian with eigenvalues $r \exp(\pm\psi/2)$, both positive since $r>0$, so $H$ is positive definite. Its determinant is the norm

$$
\det\mathsf{M}_2(H) = \langle H\rangle_{\natural} = \langle H,H\rangle_{\natural} = r^{2}\,\langle\tilde U_{\mathrm b},\tilde U_{\mathrm b}\rangle_{\natural} = r^{2} > 0 ,
$$

which is the squared scale and is positive. The scalar part of $H$ carries the scale, and the traceless part carries the rapidity and the axis of the boost.

### The Scale and the Boost

The first factor is where the pairing keeps the **scale** and the **boost**. The scale $r$ is the positive modulus, $r = |\langle\tilde{Q},\tilde{Q}\rangle_{\natural}|^{1/2}$; the boost $\tilde U_{\mathrm b}$ is the Hermitian positive unit-norm element of the polar word, and it is the only constituent of the pairing that is not compact. The norm of the first factor is the squared scale, and the two statements $\langle H\rangle_{\natural} = r^{2}$ and $\det\mathsf{M}_2(H) = r^{2}$ are the same statement in the algebra and in the matrix model.

## The Unitary Factor

### The Unitary Group

The unitary elements of the algebra are the elements fixed by the equation $\tilde{U}^{*}\tilde{U} = e_t$,

$$
\mathrm{U}(\mathbb{B}) = \{\tilde{U} : \tilde{U}^{*}\tilde{U} = e_t\} \cong \mathrm{U}(2) \cong \mathrm{U}(1)\cdot\mathrm{Sp}(1) ,
$$

a compact group of real dimension four, the product of the central phase circle and the unit sphere of the real quaternions. The second factor of the Cartan pairing is such an element: $U = \exp(i\alpha)\tilde u_{\mathrm r}$ is the product of the central phase, of modulus one, and the unit real quaternion, and it satisfies $UU^{*} = e_t$. Its determinant has modulus one, $|\det\mathsf{M}_2(U)| = 1$, which is the unitary condition in the matrix model.

### The Phase and the Rotor

The second factor contains the **phase** and the **rotor**. The phase $\exp(i\alpha)$ is central, so it lies in the centre and commutes with everything; the rotor $\tilde u_{\mathrm r}$ is the unit real quaternion of the polar word, the only factor that lies in the quaternion subspace $\mathbb{H}_{\mathbb{B}}$ on the unit sphere, and the only one that is compact and non-central. The two constituents of the second factor commute with each other, the phase being central, so the second factor is itself a product of two exponentials that add, $\exp(i\alpha\,e_t)\exp(\tfrac{\theta}{2}\vec u_{\mathrm r})$.

### The Two Factors and the Four-Factor Word

The pairing is the grouping of the four factors of the polar word into its two factors, and the grouping is the following.

| factor of the pairing | constituents | character | real dimension |
|---|---|---|---|
| $H = r\,\tilde U_{\mathrm b}$ | the scale and the boost | Hermitian positive | $1+3 = 4$ |
| $U = \exp(i\alpha)\,\tilde u_{\mathrm r}$ | the phase and the rotor | unitary | $1+3 = 4$ |

The two dimensions add to $8 = \dim_{\mathbb{R}}\mathbb{B}$, and each factor carries one compact and one non-compact constituent: the first the non-compact scale and the non-compact boost, the second the compact phase and the compact rotor.

## The Hermitian and the Anti-Hermitian Exponents

### The Two Exponents

The pairing is a **Hermitian pairing** because the two exponents of its factors lie in the two involutive subspaces. Writing the exponents of the definition,

$$
H = \exp(h) , \qquad h = \ln r\,e_t + i\tfrac{\psi}{2}\vec u_{\mathrm b} , \qquad U = \exp(u) , \qquad u = i\alpha\,e_t + \tfrac{\theta}{2}\vec u_{\mathrm r} ,
$$

the first exponent has a real scalar part $\ln r$ and a purely imaginary vector part $i\tfrac{\psi}{2}\vec u_{\mathrm b}$, and the second has a purely imaginary scalar part $i\alpha$ and a real vector part $\tfrac{\theta}{2}\vec u_{\mathrm r}$. The two exponents are therefore of the two opposite kinds.

| exponent | scalar part | vector part | subspace | related factor |
|---|---|---|---|---|
| $h = \ln r\,e_t + i\tfrac{\psi}{2}\vec u_{\mathrm b}$ | real | purely imaginary | $\mathbb{M}_+$, Hermitian | $H = \exp h$, Hermitian positive |
| $u = i\alpha\,e_t + \tfrac{\theta}{2}\vec u_{\mathrm r}$ | purely imaginary | real | $\mathbb{M}_-$, anti-Hermitian | $U = \exp u$, unitary |

The first exponent is the sum of two Hermitian terms, $(\ln r)e_t\in\mathbb{M}_+$ and $i\tfrac{\psi}{2}\vec u_{\mathrm b}\in\mathbb{M}_+$; the second is the sum of two anti-Hermitian terms, $i\alpha\,e_t\in\mathbb{M}_-$ and $\tfrac{\theta}{2}\vec u_{\mathrm r}\in\mathbb{M}_-$. The split of the four factors two and two is the split of the four exponents two and two, and it is exactly the Cartan grouping.

### The Factors Are Not the Sectors

The two exponents lie in the two subspaces, but the two **factors** do not. The Hermitian exponent exponentiates to a Hermitian positive element, and the anti-Hermitian exponent exponentiates to a unitary element; the anti-Hermitian object of the pair is therefore the logarithm $\ln U = u$, not the factor $U$ itself. The distinction is worth stating because the two sectors $\mathbb{M}_+$ and $\mathbb{M}_-$ are linear subspaces and the second factor is not.

| object | Hermitian? | anti-Hermitian? | where it lies |
|---|---|---|---|
| $h = \ln H$ | yes | no | $\mathbb{M}_+$ |
| $H = \exp h$ | yes, and positive | no | $\mathbb{M}_+$, the positive cone |
| $u = \ln U$ | no | yes | $\mathbb{M}_-$ |
| $U = \exp u$ | no | no | $\mathrm{U}(\mathbb{B})$, not a subspace |

The Hermitian factor $\exp h$ is the exponential of a Hermitian element of one sign, the positive one; the unitary factor $\exp u$ is the exponential of an anti-Hermitian element of compact type. This is the same asymmetry that the matrix polar decomposition exhibits between the positive definite factor and the unitary factor.

### The Matrix Reading

In the matrix model the two exponents are the Hermitian and the anti-Hermitian matrices of the algebra,

$$
\mathsf{M}_2(h)^{*} = \mathsf{M}_2(h) , \qquad \mathsf{M}_2(u)^{*} = -\mathsf{M}_2(u) ,
$$

and the split is the Cartan decomposition of the algebra as a real Lie algebra under the commutator,

$$
\mathfrak{gl}(2,\mathbb{C}) = \mathfrak{u}(2) \oplus \mathfrak{p} , \qquad \mathfrak{u}(2) = \mathfrak{su}(2)\oplus i\mathbb{R} , \qquad \mathfrak{p} = \{\text{Hermitian matrices}\} .
$$

The compact summand $\mathfrak{u}(2)$ is spanned by the anti-Hermitian elements, the anti-Hermitian scalar $ie_t$ and the anti-Hermitian vectors $\tfrac{\theta}{2}\vec u_{\mathrm r}$; the non-compact summand $\mathfrak{p}$ is spanned by the Hermitian elements, the real scalar $\ln r\,e_t$ and the Hermitian vectors $i\tfrac{\psi}{2}\vec u_{\mathrm b}$. The two summands are of real dimension four each, and their sum is the real dimension $8$ of the algebra. The exponent of $\mathfrak{u}(2)$ is the unitary group $\mathrm{U}(2)$ and the exponent of $\mathfrak{p}$ is the positive cone of the Hermitian elements, so the Cartan decomposition of the algebra reads the pairing at the level of the group.

## Existence, Uniqueness and the Domain

### The Theorem

**Theorem (the Cartan pairing).** Let $\tilde{Q}\in\mathbb{B}$ with $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}\neq0$. There are a unique $H\in\mathbb{M}_+$ positive definite and a unique $U\in \mathrm{U}(\mathbb{B})$ with $\tilde{Q} = HU$, and they are $H = \sqrt{\tilde{Q}\tilde{Q}^{*}}$ and $U = H^{-1}\tilde{Q}$.

### The Uniqueness of the First Factor

The product $\tilde{Q}\tilde{Q}^{*}$ is Hermitian positive, and it is positive definite when the element is invertible; a positive definite Hermitian element has a unique positive definite Hermitian square root, so $H$ is unique. The second factor is then $U = H^{-1}\tilde{Q}$, and it is unitary because $UU^{*} = H^{-1}\tilde{Q}\tilde{Q}^{*}H^{-1} = H^{-1}H^{2}H^{-1} = e_t$. Both factors are functions of the element alone, and the pairing is unique within its domain.

### The Domain

The pairing is available on the whole complement of the null cone,

$$
\{\tilde{Q} : \langle\tilde{Q},\tilde{Q}\rangle_{\natural}\neq0\} ,
$$

which is the domain of the polar representation itself. The reason is that $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \det\mathsf{M}_2(\tilde{Q})$, so the element is invertible exactly when its norm does not vanish, and an invertible element has a unique matrix polar decomposition. The Cartan pairing is the only one of the three pairings of the four factors with this domain; the Hamilton and complex pairings fail on additional sets, on which their moduli cannot be constructed from the parts of the element.

### The Matrix Proof

In the matrix model the statement is the classical polar decomposition of an invertible complex matrix. For $\tilde{Q}$ with $\mathsf{M}_2(\tilde{Q})$ invertible, the matrix $(\mathsf{M}_2(\tilde{Q})\mathsf{M}_2(\tilde{Q})^{\dagger})^{1/2}$ is the unique positive definite Hermitian square root of $\mathsf{M}_2(\tilde{Q})\mathsf{M}_2(\tilde{Q})^{\dagger}$, and it is $\mathsf{M}_2(H)$; the quotient $\mathsf{M}_2(H)^{-1}\mathsf{M}_2(\tilde{Q})$ is unitary and is $\mathsf{M}_2(U)$. Translating the two matrices back through the isomorphism $\mathbb{B}\cong\mathsf{M}_2(\mathbb{C})$ gives $H$ and $U$ above, the matrix adjoint $\dagger$ being the transport of the algebra conjugation ${}^{*}$. The proof is the matrix theorem and needs no separate existence argument.

## Relation to the Polar and the Two Partial Representations

### The Three Pairings

The four factors of the polar representation have exactly three pairings, obtained by inserting the two parentheses into the word $\tilde{Q} = r \exp(i\alpha)\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ and recording a conjugation when the rotor has crossed the boost:

$$
\tilde{Q} = \bigl(r \exp(i\alpha)\bigr)\bigl(\tilde U_{\mathrm b}\tilde u_{\mathrm r}\bigr) , \qquad \tilde{Q} = \bigl(r\tilde u_{\mathrm r}\bigr)\bigl(\exp(i\alpha)\tilde u_{\mathrm r}^{-1}\tilde U_{\mathrm b}\tilde u_{\mathrm r}\bigr) , \qquad \tilde{Q} = \bigl(r\tilde U_{\mathrm b}\bigr)\bigl(\exp(i\alpha)\tilde u_{\mathrm r}\bigr) .
$$

The first is the Hamilton representation, with the complex scalar modulus $R = r\exp(i\alpha)$; the second is the complex representation, with the real quaternion modulus $Q = r\tilde u_{\mathrm r}$; the third is the Cartan pairing of the present article, with the Hermitian positive factor $H = r\tilde U_{\mathrm b}$ and the unitary factor $U = \exp(i\alpha)\tilde u_{\mathrm r}$.

### The Cartan Pairing Is Not Partial

The first two pairings are the **partial** representations: each calls a composite object the modulus, and each is available only where that object can be constructed from the parts of the element. The Cartan pairing is of a different kind.

- **It loses nothing.** Both factors are functions of the element alone, $H = \sqrt{\tilde{Q}\tilde{Q}^{*}}$ and $U = H^{-1}\tilde{Q}$, so the four factors are recovered from the two with no choice and no extra data.
- **Its domain is the full domain.** It is available on the whole complement of the null cone, whereas the Hamilton pairing needs the vector part non-null and the complex pairing as constructed needs the real quaternion part invertible.
- **Its factors are canonical.** The two constituents of each factor commute, the phase being central, so the two factors are unambiguous; the non-commutativity of the boost and the rotor shows up only between the two factors, and it is the reason the pairing is interesting.

The Cartan pairing is therefore the polar representation with the two parentheses inserted, in the most economical of the three ways, and the word *partial* of the companion article names the other two.

### The Comparison

The three pairings differ in the modulus they name and in the domain on which the modulus is computable from the parts of the element.

| pairing | first factor | second factor | condition on $\tilde{Q}$ |
|---|---|---|---|
| Hamilton | $R = r\,\exp(i\alpha)$, complex scalar | $\exp(\vec\Xi\Theta) = \tilde U_{\mathrm b}\tilde u_{\mathrm r}$ | the vector part is non-null |
| complex | $Q = r\,\tilde u_{\mathrm r}$, real quaternion | $\exp(i\Psi) = \exp(i\alpha)\tilde u_{\mathrm r}^{-1}\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ | the real quaternion part is invertible |
| Cartan | $H = r\,\tilde U_{\mathrm b}$, Hermitian positive | $U = \exp(i\alpha)\,\tilde u_{\mathrm r}$, unitary | $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}\neq0$ |

The three domains are not nested. The Cartan domain contains the other two; the Hamilton and complex domains overlap without containing each other, and the elements that both miss are the nonzero purely imaginary complex scalars, on which $Q_r = 0$ and the vector part is null, $(\vec Q,\vec Q) = 0$. Each such element lies in the Cartan domain, with $H = |b_0|e_t$ and $U = \pm ie_t$ for $\tilde{Q} = ib_0e_t$.

## Behaviour Under the Three Conjugations

### The Three Conjugations

The algebra has three nontrivial conjugations: the quaternion conjugation ${}^{\natural}$, the anti-automorphism fixing the centre $\mathbb{C}_{\mathbb{B}}$; the coefficientwise conjugation $\bar{\cdot}$, the automorphism conjugating every coefficient; and the Hermitian conjugation ${}^{*} = {}^{\natural}\circ\bar{\cdot}$, the composite. The three act on the pairing in three different ways, and the difference is the difference between preserving the order and reversing it: the coefficientwise conjugation is an automorphism and keeps the order of the two factors, while the quaternion and the Hermitian conjugations are anti-automorphisms and reverse it.

### The Hermitian Conjugation

The Hermitian conjugate of the element is

$$
\tilde{Q}^{*} = \bigl(U^{*}HU\bigr)U^{*} ,
$$

so the two factors of $\tilde{Q}^{*}$ in the Cartan shape are the conjugate $U^{*}HU$ of the first factor, Hermitian positive, and $U^{*}$, unitary. Both factors change: the pairing is not a regrouping of the two factors of $\tilde{Q}$, because a Hermitian and a unitary element multiplied in the other order is a different element.

### The Quaternion Conjugation

The quaternion conjugation reverses the order and does not touch the coefficients, so $\tilde{Q}^{\natural} = U^{\natural}H^{\natural}$; the two factors of $\tilde{Q}^{\natural}$ are the conjugates of the two factors of $\tilde{Q}$, taken in the reversed order. In the Cartan shape the first factor is $U^{\natural}H^{\natural}U^{\natural*}$ and the second is $U^{\natural}$, the conjugations of the two factors with the order restored by a conjugation.

### The Coefficientwise Conjugation

The coefficientwise conjugation is an automorphism and keeps the order, so $\overline{\tilde{Q}} = \overline{H}\,\overline{U}$ is already the Cartan shape: the first factor $\overline{H} = r\tilde U_{\mathrm b}^{\natural}$ is Hermitian positive and the second $\overline{U} = \exp(-i\alpha)\tilde u_{\mathrm r}$ is unitary, the real quaternion rotor being unchanged by the coefficientwise conjugation. The coefficientwise conjugation is therefore the one that preserves the pairing without a change of order.

| conjugation | first factor of the conjugate | second factor of the conjugate | order |
|---|---|---|---|
| ${}^{*}$ | $U^{*}HU$ | $U^{*}$ | restored by a conjugation |
| ${}^{\natural}$ | $U^{\natural}H^{\natural}U^{\natural*}$ | $U^{\natural}$ | restored by a conjugation |
| $\bar{\cdot}$ | $\overline{H} = r\tilde U_{\mathrm b}^{\natural}$ | $\overline{U} = \exp(-i\alpha)\tilde u_{\mathrm r}$ | preserved |

The two anti-automorphisms behave in the same way, each with its own conjugation of the Hermitian factor, and the automorphism is the exceptional one that needs no conjugation at all.

## The Cartan Decomposition of the Unit Group

### The Unit-Norm Case

For an element of unit norm, $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = e_t$, the scale and the phase are trivial, $r = 1$ and $\exp(i\alpha) = e_t$, and the Cartan pairing reduces to the product of the boost and the rotor,

$$
\tilde{Q} = \tilde U_{\mathrm b}\,\tilde u_{\mathrm r} , \qquad \tilde U_{\mathrm b}\in\mathbb{M}_+ , \quad \tilde U_{\mathrm b}^{*} = \tilde U_{\mathrm b} , \quad \tilde u_{\mathrm r}\in\mathrm{Sp}(1) .
$$

This is the **Cartan decomposition** of the unit group, $SL(2,\mathbb{C}) = SU(2)\exp(\mathfrak{p})$, read in the algebra: the unit-norm elements are the products of a Hermitian positive element, which is the exponential of a traceless Hermitian element, and an element of the maximal compact subgroup $SU(2) = \mathrm{Sp}(1)$.

### The Physical Interpretation

In the physics articles the unit-norm element is a Lorentz rotor, the Hermitian positive factor is a pure boost and the unitary real quaternion is a spatial rotation; the pairing is then the statement that every element of the restricted Lorentz group is a boost times a rotation, in that order. The two factors land in the two involutive sectors: the boost in the Hermitian subspace $\mathbb{M}_+$, which the physics articles call the informational sector, and the rotor's exponent in the anti-Hermitian subspace $\mathbb{M}_-$, which they call the material sector. The pairing is the algebraic home of the composition of a boost and a rotation, and the non-commutativity of the two factors is the reason the product of two boosts is a boost and a rotation and not a pure boost. The group statement is developed in *The Lorentz Group in Biquaternionic Form — Structure and Representations*.

## The Published Form of the Pairing

The pairing $HU$ is the factorisation proved by Sangwine and Hitzer for the unit semi-norm elements and, in the general case, by their Corollary 1, in the reversed word, angle first:

$$
\tilde{Q} = |\tilde{Q}|\,\exp(\alpha\theta_t)\,\exp(I\beta\theta_h) ,
$$

with two pure real unit quaternions $\alpha$ and $\beta$, a pure imaginary unit biquaternion $I\beta$ (with $I$ an imaginary unit), and two real angles $\theta_t$ and $\theta_h$. Translating their letters into those of the corpus, the trigonometric exponential $\exp(\alpha\theta_t)$ is the rotor $\tilde u_{\mathrm r} = \exp(\tfrac{\theta}{2}\vec u_{\mathrm r})$, the hyperbolic exponential $\exp(I\beta\theta_h)$ is the boost about the axis rotated by the rotor, and their product is the boost conjugated by the rotor. Three differences are worth recording.

- **The order is reversed.** The two non-central factors are written angle first in the paper and boost first in the corpus, and the two words are related by a conjugation by the rotor.
- **The count differs.** Their $2+3+3 = 8$ keeps the complex modulus whole, where the corpus writes $1+1+3+3 = 8$ with the phase split off.
- **The branch and the uniqueness** of the general form are fixed here, at $\alpha\in(-\tfrac{\pi}{2},\tfrac{\pi}{2}]$, and the paper states neither and admits both orders.

The mathematics of the pairing is the same in both places; what the corpus adds is the split of the modulus into a scale and a phase, the branch, and the uniqueness.

## Worked Examples

### The Generic Element

Take $\tilde{Q} = (1+i)e_t+\vec e_x+2\vec e_y$, the generic element of the companion article. Its polar representation, computed there, is

$$
r = 2.320595787 , \quad \alpha = 0.190253189 , \quad \tilde U_{\mathrm b} = 1.072349609\,e_t - 0.173166789\,i\,\vec e_x - 0.346333577\,i\,\vec e_y , \quad \tilde u_{\mathrm r} = 0.470592172\,e_t+0.394599292\,\vec e_x+0.789198585\,\vec e_y .
$$

The Cartan pairing is

$$
H = r\tilde U_{\mathrm b} = 2.488489985\,e_t - 0.401850120\,i\,\vec e_x - 0.803700241\,i\,\vec e_y ,
$$

Hermitian positive with $\langle H\rangle_{\natural} = r^{2} = 5.385164807$, and

$$
U = \exp(i\alpha)\tilde u_{\mathrm r} = (0.462100989+0.088992519i)e_t + (0.387479295+0.074621694i)\vec e_x + (0.774958590+0.149243388i)\vec e_y .
$$

The first factor is Hermitian positive and the second is unitary, and the two are the two halves of the same four-factor word.

### The Element with a Null Vector Part

Take $\tilde{Q} = 1+\vec e_x+i\vec e_y$. Then $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = 1$ and $(\vec Q,\vec Q) = 0$, so the Hamilton representation does not exist; the Cartan pairing does, with

$$
r = 1 , \qquad \alpha = 0 , \qquad H = \tilde U_{\mathrm b} = 1.414213562\,e_t + 0.707106781\,i\,\vec e_y + 0.707106781\,i\,\vec e_z , \qquad U = \tilde u_{\mathrm r} = 0.707106781\,(e_t+\vec e_x) .
$$

The first factor is Hermitian positive and the second is unitary, and the element is the non-scalar witness of the section on the complex representation of the companion article.

### The Element with a Vanishing Real Part

Take $\tilde{Q} = i\vec e_x+i\vec e_y$. Then $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = -2$ and $Q_r = 0$, so the construction of the complex representation from the parts of the element fails; the Cartan pairing does not, and reads

$$
r = \sqrt{2} , \qquad \alpha = \frac{\pi}{2} , \qquad \tilde U_{\mathrm b} = e_t , \qquad \tilde u_{\mathrm r} = \frac{\vec e_x+\vec e_y}{\sqrt{2}} , \qquad H = \sqrt{2}\,e_t , \qquad U = i\,\frac{\vec e_x+\vec e_y}{\sqrt{2}} .
$$

The first factor is the positive scalar $\sqrt{2}e_t$, Hermitian positive, and the second is the unitary imaginary quaternion $i(\vec e_x+\vec e_y)/\sqrt2$; their product is $\tilde{Q}$.

### The Scalar Imaginary

Take $\tilde{Q} = i$. Then $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = -1$, the element is invertible and the polar representation is $i = 1\cdot \exp(i\pi/2)\cdot e_t\cdot e_t$. The Cartan pairing reads $i = e_t\cdot i$, with $H = e_t$ Hermitian positive and $U = i$ unitary: the central phase of the polar representation is absorbed into the unitary factor, which is the grouping that defines the Cartan pairing. The example is the clearest single illustration of the difference between having a pairing and being able to construct the modulus of a partial representation from the parts of the element.

## Summary

The polar representation of a biquaternion with non-vanishing norm has four factors and three pairings, and the Cartan pairing groups the scale with the boost and the phase with the rotor into the two factors $\tilde{Q} = HU$, $H = r\tilde U_{\mathrm b}$ and $U = \exp(i\alpha)\tilde u_{\mathrm r}$. The first factor is Hermitian positive, with norm $\langle H\rangle_{\natural} = r^{2}$ and matrix image the positive definite Hermitian square root of $\mathsf{M}_2(\tilde{Q})\mathsf{M}_2(\tilde{Q})^{\dagger}$; the second is unitary, an element of $\mathrm{U}(\mathbb{B})\cong \mathrm{U}(2)$ carrying the central phase and the spatial rotation. The pairing solves the single equation $\tilde{Q}\tilde{Q}^{*} = H^{2}$, whence $H = \sqrt{\tilde{Q}\tilde{Q}^{*}}$ and $U = H^{-1}\tilde{Q}$, and it is unique on the complement of the null cone.

The pairing is a Hermitian pairing because the two exponents of its factors lie in the two involutive subspaces: $\ln H = \ln r\,e_t + i\tfrac{\psi}{2}\vec u_{\mathrm b}$ is Hermitian and $\ln U = i\alpha\,e_t + \tfrac{\theta}{2}\vec u_{\mathrm r}$ is anti-Hermitian, which is the Cartan decomposition $\mathfrak{gl}(2,\mathbb{C}) = \mathfrak{u}(2)\oplus\mathfrak{p}$ of the algebra as a real Lie algebra. The factors themselves are not the sectors: the Hermitian exponent gives a Hermitian positive factor, the anti-Hermitian exponent gives a unitary factor, and the anti-Hermitian object of the pair is the logarithm of the second factor and not the second factor.

The Cartan pairing is not a partial representation. The Hamilton and complex pairings of the companion article are available only where their moduli can be constructed from the parts of the element, whereas the Cartan pairing is available on the whole complement of the null cone and recovers both of its factors from the element and its Hermitian conjugate. In the unit-norm case the scale and the phase are trivial and the pairing becomes the Cartan decomposition of the unit group, which the physics articles read as a Lorentz boost times a spatial rotation.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde{Q} = r \exp(i\alpha)\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ | the polar representation, four factors |
| $r$, $\exp(i\alpha)$, $\tilde U_{\mathrm b}$, $\tilde u_{\mathrm r}$ | scale, central phase, Hermitian positive boost, unit real quaternion rotor |
| $\tilde{Q} = H U$ | the Cartan pairing, two factors |
| $H = r\tilde U_{\mathrm b}$ | the Hermitian positive factor, or first factor |
| $U = \exp(i\alpha)\tilde u_{\mathrm r}$ | the unitary factor, or second factor |
| $R = r\exp(i\alpha)$, $\vec\Xi$, $\Theta$ | the Hamilton modulus, its axis and its complex angle |
| $Q = r\tilde u_{\mathrm r}$, $\Psi$ | the complex modulus and the angle of the complex exponential |
| $\langle H\rangle_{\natural} = \langle H,H\rangle_{\natural} = r^{2}$ | the norm of the first factor, the squared scale |
| $\vec Q = Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ | the vector part of $\tilde{Q}$ |
| $(\vec Q,\vec Q) = Q_x^2+Q_y^2+Q_z^2$ | the general plain bilinear square of the vector part |
| $Q_r$ | the real quaternion part of $\tilde{Q}$, the element with the real parts of the four coefficients |
| $\mathbb{M}_\pm = \{\tilde{Q} : \tilde{Q}^{*} = \pm\tilde{Q}\}$ | the Hermitian and the anti-Hermitian subspaces |
| $\mathrm{U}(\mathbb{B})\cong \mathrm{U}(2)\cong \mathrm{U}(1)\cdot\mathrm{Sp}(1)$ | the unitary group of the algebra, home of the second factor |
| $h = \ln H = \ln r\,e_t + i\tfrac{\psi}{2}\vec u_{\mathrm b}$ | the Hermitian exponent, in $\mathbb{M}_+$ |
| $u = \ln U = i\alpha\,e_t + \tfrac{\theta}{2}\vec u_{\mathrm r}$ | the anti-Hermitian exponent, in $\mathbb{M}_-$ |
| $\psi$, $\vec u_{\mathrm b}$ | rapidity and unit axis of the boost |
| $\theta$, $\vec u_{\mathrm r}$ | rotation angle and unit axis of the rotor |
| ${}^{\natural}$, $\bar{\cdot}$, ${}^{*}$ | quaternion, coefficientwise and Hermitian conjugation |
| $\mathsf{M}_2$ | the matrix model $\mathbb{B}\cong\mathsf{M}_2(\mathbb{C})$ |

## Further Reading

- *The Polar Element Representation of Biquaternions* (`articles_maths/the-polar-element-representation-of-biquaternions.md`), for the four factors, the modulus $\rho = \sqrt{\langle\tilde{Q},\tilde{Q}\rangle_{\natural}}$, the exponential trichotomy and the domain.
- *The Hamilton Root Pairing of the Polar Element Representation of Biquaternions* (`articles_maths/the-hamilton-root-pairing-of-the-polar-element-representation-of-biquaternions.md`) and *The Quaternion Pairing of the Polar Element Representation of Biquaternions* (`articles_maths/the-quaternion-pairing-of-the-polar-element-representation-of-biquaternions.md`), for the Hamilton and quaternion pairings, the two partial pairings whose moduli are constructed from the parts of the element.
- *Hermitian and Skew-Hermitian Elements* (`articles_maths/hermitian-and-skew-hermitian-elements.md`), for the involutive split $\mathbb{B} = \mathbb{M}_+\oplus\mathbb{M}_-$ and the two sectors.
- *The Unitary Group of the Biquaternion Algebra* (`articles_maths/the-unitary-group-of-the-biquaternion-algebra.md`), for $\mathrm{U}(\mathbb{B})\cong \mathrm{U}(2)$ and the structure of the unitary elements.
- *Positivity and the Hermitian Cone of the Biquaternioid Algebra with Hermitian Adjoint* (`articles_maths/positivity-and-the-hermitian-cone-of-the-biquaternioid-algebra-with-hermitian-adjoint.md`), for the positive cone of the Hermitian elements in which the first factor lies.
- *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* (`articles_maths/introduction-to-the-2x2-matrix-element-representation-of-biquaternions.md`), for the isomorphism $\mathbb{B}\cong\mathsf{M}_2(\mathbb{C})$ and the transport of the conjugation ${}^{*}$ to the matrix adjoint.
- *Biquaternion Elementary Functions* (`articles_maths/biquaternion-elementary-functions.md`), for the exponential, the logarithm and the principal branch that fix the two exponents of the pairing.
- *The Lorentz Group in Biquaternionic Form — Structure and Representations* (`articles_physics/the-lorentz-group-in-biquaternionic-form-structure-and-representations.md`), for the unit-norm case $\tilde{U} = \tilde{B}\tilde u_{\mathrm r}$, the boost and the rotation of the physical interpretation.
- *The Polar Element Representation in Subspaces* (`articles_physics/the-polar-element-representation-in-subspaces.md`), for the Cartan pairing restricted to the remarkable subspaces of the algebra.
- *The Polar Element Representation and Remarkable Subspaces* (`articles_maths/the-polar-element-representation-and-remarkable-subspaces.md`), for the same restriction in the algebra: the four exponents against the four coordinate blocks and the six subspaces, the incidence of the exponents with the subspaces, and the polar data each subspace carries.
- S. J. Sangwine and E. Hitzer, "Polar decomposition of complexified quaternions and octonions", *Advances in Applied Clifford Algebras* (2020), DOI 10.1007/s00006-020-1048-y; technical report CES-535, University of Essex (2019), for Theorem 1 and Corollary 1, the published form of the pairing.
