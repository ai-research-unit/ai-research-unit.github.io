# __The Tensor Product of Two Biquaternion Algebras__

## Introduction

The tensor product of two copies of $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ is not a biquaternion algebra, and there are two tensor products to compute. This article computes both: the complex one, $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}\cong M_4(\mathbb{C})$, of complex dimension sixteen, and the real one, $\mathbb{B}\otimes_{\mathbb{R}}\mathbb{B}\cong M_4(\mathbb{C})\oplus M_4(\mathbb{C})$, of real dimension sixty-four. It also computes what happens to the two structures the algebra carries: the star, which survives only in its total form, and the sector splitting, which does not survive at all but leaves a parity rule behind.

The article is the algebra behind the multi-qubit extension in the physics corpus. What is computed here is used there: [Composite Systems and the Multi-Qubit Extension](../articles_physics/composite-systems-and-the-multi-qubit-extension.html) for the two routes, [The Multi-Qubit Split, I](../articles_physics/the-multi-qubit-split-i-the-antilinear-obstruction-and-the-corner-collapse.html) for the obstruction and the collapse, and [The Multi-Qubit Split, II](../articles_physics/the-multi-qubit-split-ii-the-sign-condition-the-concurrence-form-and-the-central-bit.html) for the central bit. The algebra is in [The Biquaternion Algebra](introduction-to-the-algebra-of-biquaternions.html); the star is in [The Group of Involutions](the-group-of-involutions-of-the-biquaternion-algebra.html); the decompositions are in [Subspaces and Decompositions of the Biquaternion Algebra](subspaces-and-decompositions-of-the-biquaternion-algebra.html); the modules are in [The Category of Modules in the Biquaternion Algebra](the-category-of-modules-in-the-biquaternion-algebra.html).

**The four results.** First, the complex tensor product is a full matrix algebra of degree four, central simple with no non-trivial two-sided ideal, and not isomorphic to $\mathbb{B}$. Second, the partial star does not descend to it, so there is no per-factor sector label; the total star does descend, so one global label survives. Third, in the complex tensor product the four sector corners collapse pairwise, because a material unit of one factor is $i$ times an informational unit and $i\otimes i=-1$. Fourth, over $\mathbb{R}$ the algebra doubles and a central involution splits it into two matrix algebras, which is where the central bit of the physical description comes from.

## The Two Tensor Products

**Over $\mathbb{R}$.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ is a real algebra of dimension eight, with centre $\mathbb{C}e_t$ of real dimension two. The real tensor product $\mathbb{B}\otimes_{\mathbb{R}}\mathbb{B}$ has real dimension sixty-four and centre of real dimension four.

**Over $\mathbb{C}$.** The complex tensor product is the quotient

$$
\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}=\bigl(\mathbb{B}\otimes_{\mathbb{R}}\mathbb{B}\bigr)\big/\bigl(i\otimes e_t-e_t\otimes i\bigr),
$$

that is, the real tensor product with the two central scalars identified. Its dimension over $\mathbb{C}$ is sixteen, and over $\mathbb{R}$ thirty-two. The single relation is the whole difference between the two objects: every other product is untouched, so $e_t\otimes\vec e_x$ and $\vec e_x\otimes e_t$ remain distinct, and the quaternion units of the two factors do not commute by fiat.

**The universal property, stated to fix the reading.** For any complex algebra $A$ and any pair of $\mathbb{C}$-algebra maps $f_1,f_2:\mathbb{B}\to A$, there is a unique $\mathbb{C}$-algebra map $f:\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}\to A$ with $f(x\otimes e_t)=f_1(x)$ and $f(e_t\otimes y)=f_2(y)$. So the complex tensor product is the algebra of pairs of commuting copies of $\mathbb{B}$, and the real tensor product is the algebra of pairs of copies with independent centres.

**A dimension table.**

| object | field | dimension | centre |
| --- | --- | --- | --- |
| $\mathbb{B}$ | $\mathbb{R}$ | $8$ | $2$ |
| $\mathbb{B}\otimes_{\mathbb{R}}\mathbb{B}$ | $\mathbb{R}$ | $64$ | $4$ |
| $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}$ | $\mathbb{C}$ | $16$ | $1$ |

## The Complex Tensor Product

**The theorem.** $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}\cong M_4(\mathbb{C})$.

*Proof.* $\mathbb{B}\cong M_2(\mathbb{C})$ as a complex algebra, and the tensor product of matrix algebras is the matrix algebra of the product of the degrees: $M_m(\mathbb{C})\otimes_{\mathbb{C}}M_n(\mathbb{C})\cong M_{mn}(\mathbb{C})$ through the Kronecker product. With $m=n=2$ the degree is four.

**The consequences of being a full matrix algebra.** $M_4(\mathbb{C})$ is simple, so it has no two-sided ideal other than $0$ and the whole algebra; it is central, so its centre is $\mathbb{C}\mathrm I_4$, of complex dimension one; it is the endomorphism algebra of a four-dimensional complex space, unique up to isomorphism; and every automorphism is inner, so $\operatorname{Aut}(M_4)=\mathrm{PGL}_4(\mathbb{C})$.

**The consequence that matters for the sectors.** A decomposition of an algebra into a direct sum of two-sided ideals is the same thing as a family of central idempotents summing to one. Since the centre of $M_4(\mathbb{C})$ is one-dimensional, its only idempotents are $0$ and $1$, so there is no such decomposition. **The complex tensor product admits no sector decomposition into two-sided ideals, at any level.**

**The explicit isomorphism.** In the Pauli model $e_t=\mathrm I_2$ and $\vec e_k=i\sigma_k$, so

$$
e_\mu\otimes e_\nu\;\longmapsto\;\mathsf M_2(e_\mu)\otimes\mathsf M_2(e_\nu)\in M_2(\mathbb{C})\otimes M_2(\mathbb{C})=M_4(\mathbb{C}),
$$

and the sixteen products $e_\mu\otimes e_\nu$ are a complex basis of the image. The identification of the two central scalars is the identification of $i\mathrm I_2\otimes\mathrm I_2$ with $\mathrm I_2\otimes i\mathrm I_2$, which is $i\mathrm I_4$ in both cases.

**The reading of the degree.** The degree of the tensor product is the product of the degrees, so $2\cdot2=4$. This is the whole of the obstruction to a biquaternion reading of two qubits: a biquaternion algebra has degree two, and no relabelling changes a degree. Four amplitudes per subsystem give sixteen amplitudes, which is the square of four and not four.

## The Star on the Complex Tensor Product

**The total star descends.** Let $\sigma_{\mathrm{tot}}={}^{*}\otimes{}^{*}$ on $\mathbb{B}\otimes_{\mathbb{R}}\mathbb{B}$. It preserves the quotient relation, since

$$
\sigma_{\mathrm{tot}}\bigl(i\otimes e_t-e_t\otimes i\bigr)=(-i)\otimes e_t-e_t\otimes(-i)=-\bigl(i\otimes e_t-e_t\otimes i\bigr),
$$

so it induces an involution $\bar\sigma_{\mathrm{tot}}$ of $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}$. Under the isomorphism with $M_4(\mathbb{C})$ it is the Hermitian adjoint $X\mapsto X^{\dagger}$, and its fixed space is $\mathrm{Herm}(M_4(\mathbb{C}))$, of real dimension sixteen, half of thirty-two.

**The partial star does not descend.** Let $\sigma_1={}^{*}\otimes\mathrm{id}$. Then

$$
\sigma_1\bigl(i\otimes e_t-e_t\otimes i\bigr)=(-i)\otimes e_t-e_t\otimes i ,
$$

whose class in the quotient is $-2\,(i\otimes e_t)$, that is $-2i\mathrm I_4$, which is nonzero. Since a map descends to a quotient exactly when it carries the ideal into itself, no induced map exists.

**Why the partial star had no chance, in algebraic terms.** $\sigma_1$ is not an algebra map, because the star reverses the order of a product; and it is not an anti-algebra map either, since the reversal would have to be applied in both slots while $\sigma_1$ applies it in one. So the candidate for a per-factor label reverses the order in one factor and preserves it in the other, and no such map is an involution of an algebra of pairs. Its natural home is $\mathbb{B}^{\mathrm{op}}\otimes\mathbb{B}$, and the identification of $\mathbb{B}$ with its opposite does not carry the star to the identity.

**The count of the involutions.** Of the four maps built from the two stars — the identity, the two partial stars, the total star — the two partial ones fail to descend and the total one descends. So the tensor product carries exactly one sector involution, and its eigenspaces are the Hermitian and anti-Hermitian parts. The label that survives labels the whole and not a factor.

## The Real Tensor Product

**The theorem.** $\mathbb{B}\otimes_{\mathbb{R}}\mathbb{B}\cong M_4(\mathbb{C})\oplus M_4(\mathbb{C})$.

*Proof.* Factor the algebra: $\mathbb{B}\otimes_{\mathbb{R}}\mathbb{B}=(\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C})\otimes_{\mathbb{R}}(\mathbb{H}\otimes_{\mathbb{R}}\mathbb{H})$. The scalar extension is $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\oplus\mathbb{C}$ through $a\otimes b\mapsto(ab,\bar a b)$, and the quaternion tensor square is $\mathbb{H}\otimes_{\mathbb{R}}\mathbb{H}\cong M_4(\mathbb{R})$. Hence the algebra is $(\mathbb{C}\oplus\mathbb{C})\otimes_{\mathbb{R}}M_4(\mathbb{R})\cong M_4(\mathbb{C})\oplus M_4(\mathbb{C})$.

**The dimension check.** Each summand is sixteen over $\mathbb{C}$, that is thirty-two over $\mathbb{R}$, and there are two, for sixty-four, which is $8\cdot8$.

**The isomorphism made explicit.** $\mathbb{H}\otimes_{\mathbb{R}}\mathbb{H}\cong M_4(\mathbb{R})$ is the regular representation of one factor on the other, and the two copies of $\mathbb{C}$ are the two characters of $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$: the pairs $(a\otimes b)\mapsto ab$ and $(a\otimes b)\mapsto\bar ab$. So the two summands are the complex tensor product and the tensor product against the conjugate algebra.

## The Centre and the Central Involution

**The centre.** The centre of $\mathbb{B}\otimes_{\mathbb{R}}\mathbb{B}$ is $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$, of real dimension four, with real basis $e_t\otimes e_t$, $i\otimes e_t$, $e_t\otimes i$ and $i\otimes i$.

**The central involution.** Put $\mathsf J=i\otimes i$. Then

$$
\mathsf J^{2}=i^{2}\otimes i^{2}=(-e_t)\otimes(-e_t)=e_t\otimes e_t ,
$$

so $\mathsf J$ is an involution, and it is central because $i$ is central in each factor.

**The idempotents.**

$$
u=\tfrac12\bigl(e_t\otimes e_t+\mathsf J\bigr),\qquad v=\tfrac12\bigl(e_t\otimes e_t-\mathsf J\bigr),
$$

are central, idempotent, orthogonal and sum to the identity:

$$
u^{2}=u,\quad v^{2}=v,\quad uv=0,\quad u+v=e_t\otimes e_t .
$$

**The evaluation of $\mathsf J$.** Under $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\to\mathbb{C}\oplus\mathbb{C}$, $a\otimes b\mapsto(ab,\bar a b)$, the element $i\otimes i$ maps to $\bigl(i\cdot i,\ (-i)\cdot i\bigr)=(-1,+1)$. So $\mathsf J$ is $-1$ on the summand cut by $v$ and $+1$ on the summand cut by $u$; and since $\mathsf J=u-v$ on the centre, $u\mathsf J=u$ and $v\mathsf J=-v$.

**The two ideals.** The summands are $u(\mathbb{B}\otimes_{\mathbb{R}}\mathbb{B})$ and $v(\mathbb{B}\otimes_{\mathbb{R}}\mathbb{B})$, each of real dimension thirty-two, each isomorphic to $M_4(\mathbb{C})$.

## The Two Summands and the Physical One

**The summand cut by $v$ is the complex tensor product.** There $\mathsf J=-1$, so

$$
\mathsf J=(i\otimes e_t)(e_t\otimes i)
$$

is the product of the two central scalars, and each of them squares to $i^{2}=-1$. Two equal scalars therefore multiply to $-1$, and a scalar and its conjugate multiply to $-i\,i=+1$. So the value of $\mathsf J$ is exactly the verdict on whether the two scalars agree, and $\mathsf J=-1$ says they do. Agreement is the relation that defines $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}$, so this summand is the quotient, and it is $M_4(\mathbb{C})$.

**The summand cut by $u$ is the tensor product against the conjugate algebra.** There $\mathsf J=+1$, so $i\otimes e_t=-(e_t\otimes i)$: the second scalar is the negative of the first, that is the conjugate of the first. So the algebra is $\mathbb{B}\otimes_{\mathbb{C}}\overline{\mathbb{B}}$, of the same size and with the opposite complex structure.

**The naming is easy to invert, so the sign is checked against the explicit map.** With $a\otimes b\mapsto(ab,\bar a b)$ and $i\otimes i\mapsto\bigl(i^{2},\bar i\,i\bigr)=(-1,+1)$, the first entry corresponds to the product $ab$, in which the two scalars are taken as they are, and the second to $\bar a b$, in which the first is conjugated. Since $u=\tfrac12(e_t\otimes e_t+\mathsf J)$ maps to $(0,1)$ and $v=\tfrac12(e_t\otimes e_t-\mathsf J)$ to $(1,0)$, the first entry — and therefore the summand with $\mathsf J=-1$, cut by $v$ — is the one in which the scalars agree. That is the complex tensor product.

**Stated once, unambiguously.** The physical summand, the complex tensor product $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}$, is the one on which $\mathsf J=-1$, cut by $v=\tfrac12(e_t\otimes e_t-\mathsf J)$. The other summand, on which $\mathsf J=+1$ and cut by $u$, is $\mathbb{B}\otimes_{\mathbb{C}}\overline{\mathbb{B}}$.

## The Corners and the Parity Rule

**The four corners.** For $a,b\in\mathbb{B}_\Psi$ and $a',b'\in\mathbb{B}_\Phi$, the four real subspaces

$$
C_{\Psi\Psi}=\operatorname{span}_{\mathbb{R}}\{a\otimes b\},\quad
C_{\Phi\Phi}=\operatorname{span}_{\mathbb{R}}\{a'\otimes b'\},\quad
C_{\Psi\Phi},\quad C_{\Phi\Psi},
$$

each of real dimension sixteen, are the corners that a per-factor sector decomposition would separate.

**The corner identity.** For a quaternion unit $\vec e_\mu$ the material element is $\vec e_\mu$ itself and the informational element it generates is $i\vec e_\mu$; in the complex tensor product $i\otimes i=-e_t\otimes e_t$, so

$$
(i\vec e_\mu)\otimes(i\vec e_\mu)=(i\otimes i)\bigl(\vec e_\mu\otimes\vec e_\mu\bigr)=-\bigl(\vec e_\mu\otimes\vec e_\mu\bigr).
$$

Hence $C_{\Psi\Psi}=C_{\Phi\Phi}$ and, by the same computation with one slot moved, $C_{\Psi\Phi}=C_{\Phi\Psi}$. **The four corners are two spaces**, each of real dimension sixteen, and together they are the whole algebra of thirty-two.

**The parity rule.** For $n$ factors and a decomposable tensor,

$$
\bigl(x_1\otimes\cdots\otimes x_n\bigr)^{*\otimes n}=(-1)^{k}\,x_1\otimes\cdots\otimes x_n ,
$$

where $k$ is the number of material factors. So the real span indexed by $k$ is the eigenspace of the total star for $(-1)^{k}$, and the $2^{n}$ corners collapse onto

$$
\bigoplus_{k\ \mathrm{even}}C_k=\mathrm{Herm}\bigl(M_{2^{n}}(\mathbb{C})\bigr),\qquad
\bigoplus_{k\ \mathrm{odd}}C_k=\operatorname{anti\text{-}Herm}\bigl(M_{2^{n}}(\mathbb{C})\bigr),
$$

of real dimension $2^{2n-1}$ each.

**A basis check at $n=2$.** The sixteen tensors $e_\mu\otimes e_\nu$ with $e_\mu\in\{e_t,i\vec e_x,i\vec e_y,i\vec e_z\}$ are Hermitian and independent, since in the Pauli model they are the products of two real bases of $\mathrm{Herm}(2)$, which form a real basis of $\mathrm{Herm}(2)\otimes_{\mathbb{R}}\mathrm{Herm}(2)\cong\mathrm{Herm}(4)$. So the corner has the dimension the count gives, and the equality of the two aligned corners is an equality of sixteen-dimensional spaces and not a containment.

## The Star on Each Summand

**The star preserves the summands.** Since $\mathsf J^{*}=\mathsf J$ — each $i$ changes sign and there are two of them — the idempotents satisfy $u^{*}=u$ and $v^{*}=v$, so the total star restricts to each summand.

**On either summand it is an involution of the second kind.** The summand is a complex algebra and the star multiplies the complex scalar by $-1$; hence it is conjugate-linear, an involution, and its fixed space has real dimension sixteen, half of thirty-two. In the matrix model it is the Hermitian adjoint, and its fixed space is the Hermitian part.

**What this does not give.** An involution of the second kind is not a sector decomposition: its two eigenspaces are the Hermitian and anti-Hermitian parts, and the eigenspaces of a conjugate-linear map are real subspaces exchanged by multiplication by $i$, not ideals. So even on the summand where the labels would be expected, the surviving structure is one real grading and not a family of sectors.

## What the Tensor Product Is Not

**It is not a biquaternion algebra.** Its degree is four and a biquaternion algebra's degree is two. Consequently no element of it is a two-qubit state in the sense in which an element of $\mathbb{B}_\Psi$ is a one-qubit state: the Hermitian part has real dimension sixteen, and the state space has real dimension fifteen, so the states are a positivity cone inside it and not the whole of a slice that dimension alone would call the state space.

**It has no sector decomposition.** By simplicity there is no non-trivial central idempotent, hence no splitting into two-sided ideals. The corners exist as real subspaces and collapse; they are not ideals, and they are not stable under multiplication by $i$.

**It has no per-factor star.** By the non-descent theorem there is no involution of the quotient that acts as the star on one factor. So the object that a two-system sector structure would need does not exist, and the failure is a statement about the quotient and not about a choice of basis.

**What it does have, and this is not nothing.** It has the total star, hence one global label; it has the corners, hence a parity rule; and over $\mathbb{R}$ it has the central involution, hence a bit. The three are the exact residues of the sector structure, and each is computed above.

## Summary

The complex tensor product is $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}\cong M_4(\mathbb{C})$, central simple of degree four, with centre $\mathbb{C}\mathrm I_4$; it is not a biquaternion algebra, and it has no non-trivial two-sided ideal, hence no sector decomposition. The partial star $\sigma_1={}^{*}\otimes\mathrm{id}$ does not descend, since it sends the relation $i\otimes e_t-e_t\otimes i$ to $-2i\mathrm I_4\neq0$; the total star ${}^{*}\otimes{}^{*}$ does descend, and is the Hermitian adjoint with fixed space of real dimension sixteen. In the quotient the corner identity $(i\vec e_\mu)\otimes(i\vec e_\mu)=-\vec e_\mu\otimes\vec e_\mu$ collapses the four corners onto two spaces of real dimension sixteen, and the parity rule generalises this to $n$ factors, where the $2^{n}$ corners collapse onto the Hermitian and anti-Hermitian parts of $M_{2^{n}}(\mathbb{C})$, of real dimension $2^{2n-1}$ each. Over $\mathbb{R}$ the algebra is $M_4(\mathbb{C})\oplus M_4(\mathbb{C})$, split by the central involution $\mathsf J=i\otimes i$, which is $-1$ on the summand where the two scalars agree and $+1$ on the summand where they are conjugate; the complex tensor product is the summand with $\mathsf J=-1$, cut by $v=\tfrac12(e_t\otimes e_t-\mathsf J)$. For $n$ factors there are $2^{n-1}$ summands.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}\otimes_{\mathbb{R}}\mathbb{B}$ | the real tensor product, real dimension sixty-four, centre of dimension four |
| $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}\cong M_4(\mathbb{C})$ | the quotient by $i\otimes e_t-e_t\otimes i$, complex dimension sixteen |
| $\sigma_1={}^{*}\otimes\mathrm{id}$ | the partial star; it does not descend |
| $\sigma_{\mathrm{tot}}={}^{*}\otimes{}^{*}$ | the total star; it descends, and is the Hermitian adjoint |
| $\mathsf J=i\otimes i$ | the central involution of the real tensor product |
| $u=\tfrac12(e_t\otimes e_t+\mathsf J)$ | the idempotent of the summand where the scalars are conjugate |
| $v=\tfrac12(e_t\otimes e_t-\mathsf J)$ | the idempotent of the summand where the scalars agree, that is the complex tensor product |
| $C_{\Psi\Psi}=C_{\Phi\Phi}=\mathrm{Herm}(M_4)$ | the corner collapse |
| $(-1)^{k}$ | the eigenvalue of ${}^{*\otimes n}$ on a tensor with $k$ material factors |
| $2^{2n-1}$ | the real dimension of each surviving space at $n$ factors |
| $2^{n-1}$ | the number of summands of $\mathbb{B}^{\otimes_{\mathbb{R}}n}$ |

## Further Reading

- [The Biquaternion Algebra](introduction-to-the-algebra-of-biquaternions.html), for the algebra, its basis and its structure map.
- [The Group of Involutions](the-group-of-involutions-of-the-biquaternion-algebra.html), for the star, the quaternion conjugation and their Klein group.
- [Subspaces and Decompositions of the Biquaternion Algebra](subspaces-and-decompositions-of-the-biquaternion-algebra.html), for the six subspaces and the blocks $A_1,A_2,B_1,B_2$ used in the parity rule.
- [The Category of Modules in the Biquaternion Algebra](the-category-of-modules-in-the-biquaternion-algebra.html), for the module theory, including the fact that every module over $M_4(\mathbb{C})$ is a sum of copies of $\mathbb{C}^4$.
- [Families of Matrix Representations](families-of-matrix-representations.html), for the left and right families behind the explicit isomorphism.
- [The Three Canonical Forms on $\mathbb{C}^2$](the-three-canonical-forms-on-c2.html), for the forms on the space the tensor product acts on.
- [Composite Systems and the Multi-Qubit Extension](../articles_physics/composite-systems-and-the-multi-qubit-extension.html), [The Multi-Qubit Split, I](../articles_physics/the-multi-qubit-split-i-the-antilinear-obstruction-and-the-corner-collapse.html) and [The Multi-Qubit Split, II](../articles_physics/the-multi-qubit-split-ii-the-sign-condition-the-concurrence-form-and-the-central-bit.html), for what these computations are for.
