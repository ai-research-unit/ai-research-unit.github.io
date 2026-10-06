# __The Canonical Hermitian Form on the Regular Module of the Biquaternion Algebra__

## Introduction

An involution of a ring read on the regular module produces three structures at once: a **twist** that turns the left regular module into the right one, a **symmetry** of the regular bimodule with its swap through the involution, and a **complex sesquilinear form** on the module with values in the ring itself, whose isometries are the unitary elements acting on the right. For the biquaternion algebra the involution is the Hermitian conjugation ${}^{*}$, and the three structures are the right module isomorphism

$$
{}^{*}:({}_{\mathbb{B}}\mathbb{B})^{*}\longrightarrow\mathbb{B}_{\mathbb{B}},
$$

the bimodule isomorphism of ${}_{\mathbb{B}}\mathbb{B}_{\mathbb{B}}$ with its swap through ${}^{*}$, and the canonical form

$$
h(\tilde P,\tilde R)=\tilde P\tilde R^{*},
$$

with values in $\mathbb{B}$, of which the scalar Hermitian form of the layer is the scalar part, $h(\tilde P,\tilde R)$ having scalar part $\mathrm{Sc}(\tilde P \tilde R^{*})=\langle\tilde P,\tilde R\rangle_{*}$. The isometries of $h$ that are $\mathbb{B}$-linear are the right multiplications $R_{\tilde U}$ by the unitary elements $\tilde U\tilde U^{*}=e_0$, that is by the unitary group of *The Unitary Group of the Biquaternion Algebra*; a left multiplication $L_{\tilde U}$ is an isometry only for a central unitary element, which here means a complex scalar of modulus one.

The form takes its values in $\mathbb{B}$ and induces **no** topology; the scalar form that induces the Euclidean topology of the layer is *The Hermitian Form on the Biquaternion Algebra*, whose value on a pair is the scalar part of the form here. The article assumes the general construction of *The Regular Bimodule over an Involutive Ring* for the twist, the swap and the canonical form, *Modules over an Involutive Ring* for the twist of a general module, *Involutive Rings* for the definitions of an involution and of the unitary elements, *Biquaternions as a Module over Itself* for the module object and its endomorphisms, and *The Group of Involutions* for the four conjugations of the algebra. The positivity of the form, the Hilbert structure it completes and the operator theory that needs a norm are Part II and the following articles of this layer; no positivity, no norm and no topology is used here.

Throughout, $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ is the biquaternion algebra with complex basis $e_0,e_1,e_2,e_3$, a generic element is $\tilde Q$, an idempotent is $\tilde\Pi$, the scalar part is $\mathrm{Sc}$, the two one-sided multiplications are $L_{\tilde Q}(\tilde P)=\tilde Q\tilde P$ and $R_{\tilde Q}(\tilde P)=\tilde P\tilde Q$, and the Hermitian conjugation is ${}^{*}=\bar{\cdot}\circ{}^{\natural}$, the composite of the coefficient conjugation and the quaternion conjugation.

## The Involution of the Algebra

### The two involutions of the ring

An **involution** of a ring $A$ is an anti-automorphism of order two, so that $\sigma(\tilde P\tilde R)=\sigma(\tilde R)\sigma(\tilde P)$ and $\sigma^2=\mathrm{id}$ (*Involutive Rings*). Of the four conjugations of *The Group of Involutions* two are involutions of the ring $\mathbb{B}$, and two are not.

| conjugation | reverses the product? | what it is |
|---|---|---|
| quaternion conjugation ${}^{\natural}$ | yes, $(\tilde P\tilde R)^{\natural}=\tilde R^{\natural}\tilde P^{\natural}$ | a $\mathbb{C}$-linear involution |
| Hermitian conjugation ${}^{*}$ | yes, $(\tilde P\tilde R)^{*}=\tilde R^{*}\tilde P^{*}$ | a $\mathbb{C}$-antilinear involution |
| coefficient conjugation $\bar{\cdot}$ | no, $\overline{\tilde P\tilde R}=\bar{\tilde P}\bar{\tilde R}$ | a $\mathbb{C}$-antilinear automorphism |
| anti-Hermitian conjugation ${}^{\flat}=-{}^{*}$ | no, $(\tilde P\tilde R)^{\flat}=-\tilde R^{\flat}\tilde P^{\flat}$ | neither, a skew anti-map |

**Proposition.** The quaternion conjugation ${}^{\natural}$ and the Hermitian conjugation ${}^{*}$ are involutions of the ring $\mathbb{B}$; the coefficient conjugation $\bar{\cdot}$ is an automorphism of order two, since $\bar{\tilde P}\bar{\tilde R}=\overline{\tilde P\tilde R}$, and it reverses nothing; the flat ${}^{\flat}$ is an involution of the element layer, ${}^{\flat}{}^{\flat}=\mathrm{id}$, and it is not multiplicative, since $(\tilde P\tilde R)^{\flat}=-\tilde R^{\flat}\tilde P^{\flat}$ carries the central sign.

**Proof.** The reversal of ${}^{\natural}$ and of ${}^{*}$ and the sign of the flat are computed in *The Group of Involutions*. For the coefficient conjugation, both $\tilde P\tilde R$ and $\bar{\tilde P}\bar{\tilde R}$ have the coefficients $\sum_{\mu,\nu} (P_\mu Q_\nu)$ and $\sum_{\mu,\nu}(\bar P_\mu \bar Q_\nu)$ in the basis $e_\mu e_\nu=e_0,\pm e_1,\pm e_2,\pm e_3$, and coefficient-wise conjugation is a ring homomorphism of $\mathbb{C}$, so the two agree: $\bar{\cdot}$ is multiplicative and not an anti-automorphism. The flat is $-{}^{*}$ and the central sign $-e_0$ does not commute with the reversal, so it is not an anti-automorphism.

**Corollary (which theory applies).** The general theory of the regular bimodule over an involutive ring applies to $\mathbb{B}$ through ${}^{\natural}$ and through ${}^{*}$, and not through $\bar{\cdot}$ or ${}^{\flat}$. The two parallel structures are the two of this layer: the involution ${}^{*}$ gives the complex sesquilinear form of the articles of this group, and the involution ${}^{\natural}$ gives the quaternion bilinear form of the preceding group; the coefficient conjugation is a symmetry of the real form of the algebra, and the flat is the mark of the Krein pairing of *The Four Pairings of the Biquaternion Algebra*.

### The unitary elements

**Definition.** Let $\sigma$ be an involution of $\mathbb{B}$. An element $\tilde U\in\mathbb{B}$ is **$\sigma$-unitary** when $\tilde U\sigma(\tilde U)=e_0$; because $\sigma$ is an involution and $\tilde U\sigma(\tilde U)=e_0$ makes $\tilde U$ invertible with inverse $\sigma(\tilde U)$, the condition is two-sided. The $\sigma$-unitary elements form the **unitary group** $U_\sigma(\mathbb{B})$.

**Proposition.** For $\sigma={}^{*}$ the unitary elements are those of *The Unitary Group of the Biquaternion Algebra*, the maximal compact subgroup $U(2)$ of the unit group: the matrix model identifies $\Phi(\tilde U^{*})=\Phi(\tilde U)^{\dagger}$, so the condition $\tilde U\tilde U^{*}=e_0$ reads $UU^{*}=I$. For $\sigma={}^{\natural}$ the condition is $\tilde U\tilde U^{\natural}=e_0$; in the matrix model, where $\Phi(\tilde U^{\natural})=\varepsilon\,\Phi(\tilde U)^{\mathrm{T}}\varepsilon^{-1}$ with $\varepsilon=i\sigma_2$, it reads $\Phi(\tilde U)\,\varepsilon\,\Phi(\tilde U)^{\mathrm{T}}=\varepsilon$, so the $\natural$-unitary elements form the complex symplectic group $\mathrm{Sp}(2,\mathbb{C})\cong\mathrm{SL}_2(\mathbb{C})$, of which the real unit quaternions, the unit sphere $S^3$, are the compact part.

**Proof.** The statement for ${}^{*}$ is the definition of the unitary group of the algebra, recorded in *The Unitary Group of the Biquaternion Algebra*. For ${}^{\natural}$, the adjugate identity $\Phi(\tilde Q^{\natural})=\varepsilon\,\Phi(\tilde Q)^{\mathrm{T}}\varepsilon^{-1}$ is that of *Modules over the Biquaternion Algebra*, and it is an anti-automorphism of the matrix algebra; the condition $\tilde U\tilde U^{\natural}=e_0$ is therefore $\Phi(\tilde U)\,\varepsilon\,\Phi(\tilde U)^{\mathrm{T}}\varepsilon^{-1}=I$, which is the defining equation of the symplectic group in the basis selected by $\varepsilon$. A real unit quaternion has $\tilde q\tilde q^{\natural}=1$ because on the quaternion subspace the natural sign is the quaternion conjugation and the norm is positive definite, and the real unit quaternions are the unit sphere of $\mathbb{H}\cong\mathbb{R}^4$.

## The Twist of the Regular Module

**Definition.** The **twist** of a left $\mathbb{B}$-module $M$ by an involution $\sigma$ is the same additive group with the right scalar multiplication $\tilde P\cdot\tilde Q=\sigma(\tilde Q)\tilde P$ (*Modules over an Involutive Ring*).

**Proposition.** The involution $\sigma$ is an isomorphism of right $\mathbb{B}$-modules

$$
\sigma:({}_{\mathbb{B}}\mathbb{B})^{\sigma}\longrightarrow\mathbb{B}_{\mathbb{B}},\qquad \tilde P\mapsto\sigma(\tilde P),
$$

so the twist of the left regular module is the right regular module up to the comparison $\sigma$, and this comparison is exactly the involution.

**Proof.** The map $\sigma$ is bijective, being an involution, hence of order two; for the right actions, $\sigma(\tilde P\cdot\tilde Q)=\sigma(\sigma(\tilde Q)\tilde P)=\sigma(\tilde P)\sigma(\sigma(\tilde Q))=\sigma(\tilde P)\tilde Q$, which is the ordinary right action on $\sigma(\tilde P)$; and additivity is the additivity of $\sigma$.

**Corollary (the two cases).** Through the star the twist of ${}_{\mathbb{B}}\mathbb{B}$ is the right regular module $\mathbb{B}_{\mathbb{B}}$ under the antilinear comparison $\tilde P\mapsto\tilde P^{*}$; through the natural sign it is the same statement under a $\mathbb{C}$-linear comparison. The two one-sided regular modules, which the module theory of *Biquaternions as a Module over Itself* keeps apart as $\mathbb{B}$ and $\mathbb{B}^{\mathrm{op}}$, are interchangeable through an involution, and the statement $\mathbb{B}\cong\mathbb{B}^{\mathrm{op}}$ of the module theory is the twist read backwards.

## The Involution Is the Symmetry of the Bimodule

**Definition.** Let $\sigma$ be an involution of $\mathbb{B}$. The **$\sigma$-swap** of the regular bimodule, written ${}^{\mathrm{sw}}{}_{\mathbb{B}}\mathbb{B}_{\mathbb{B}}^{\sigma}$, is the same additive group with the left and the right actions interchanged and read through $\sigma$:

$$
\tilde A\cdot\tilde R=\tilde R\sigma(\tilde A),\qquad \tilde R\cdot\tilde B=\sigma(\tilde B)\tilde R .
$$

For the identity involution of a commutative ring the two actions are simply interchanged and the $\sigma$-swap is the **swap** of the bimodule; the involution is carried in the definition because over a noncommutative ring the two actions cannot be exchanged by themselves.

**Proposition.** An involution $\sigma$ is an isomorphism of bimodules

$$
\sigma:{}_{\mathbb{B}}\mathbb{B}_{\mathbb{B}}\longrightarrow{}^{\mathrm{sw}}{}_{\mathbb{B}}\mathbb{B}_{\mathbb{B}}^{\sigma},\qquad \sigma(\tilde A\tilde P\tilde B)=\sigma(\tilde B)\sigma(\tilde P)\sigma(\tilde A),
$$

and conversely every bimodule isomorphism ${}_{\mathbb{B}}\mathbb{B}_{\mathbb{B}}\to{}^{\mathrm{sw}}{}_{\mathbb{B}}\mathbb{B}_{\mathbb{B}}^{\sigma}$ is $\tilde P\mapsto\tilde D\,\sigma(\tilde P)$ with $\tilde D$ a central unit; it is an anti-automorphism, hence its own inverse when normalised at the unit, exactly when $\tilde D=e_0$. For the biquaternion algebra the central units are the non-zero complex scalars $\tilde D=\lambda e_0$, $\lambda\in\mathbb{C}^{\times}$, so each involution is one member of a one-parameter family of symmetries of the bimodule.

**Proof.** That $\sigma$ is bijective and additive is the definition of an involution. Inserting $\sigma$ into the target, $\tilde A\cdot\sigma(\tilde P)\cdot\tilde B=\bigl(\sigma(\tilde B)\sigma(\tilde P)\bigr)\sigma(\tilde A)=\sigma(\tilde B)\sigma(\tilde P)\sigma(\tilde A)$, which is the anti-multiplicativity of $\sigma$ applied to $\tilde A\tilde P\tilde B$; so $\sigma$ intertwines the two structures. For the converse, let $\varphi$ be such an isomorphism and put $\tilde D=\varphi(e_0)$. Left linearity gives $\varphi(\tilde A)=\tilde A\cdot\varphi(e_0)=\varphi(e_0)\sigma(\tilde A)=\tilde D\sigma(\tilde A)$, and right linearity gives $\varphi(\tilde B)=\varphi(e_0)\cdot\tilde B=\sigma(\tilde B)\varphi(e_0)=\sigma(\tilde B)\tilde D$; the two agree on every element exactly when $\tilde D$ commutes with every $\sigma(\tilde B)$, that is when $\tilde D$ is central, and it is a unit because $\varphi$ is bijective. Then $\varphi(\tilde A\tilde B)=\tilde D\sigma(\tilde A\tilde B)$ while $\varphi(\tilde B)\varphi(\tilde A)=\tilde D\sigma(\tilde B)\tilde D\sigma(\tilde A)=\tilde D^2\sigma(\tilde B)\sigma(\tilde A)$, so $\varphi$ is an anti-homomorphism exactly when $\tilde D=e_0$, and then it is the involution $\sigma$. The central units are the non-zero complex scalars by the centre computation of *Biquaternions as a Vector Space over $\mathbb{C}$*.

**Remark (why the involution cannot be dropped).** Over a noncommutative ring the untwisted swap, with the two actions exchanged and nothing else, is **not** the target of the involution: for the star of the biquaternion algebra the element $\tilde A=e_1$, $\tilde P=\tilde B=e_0$ gives $\sigma(\tilde A\tilde P\tilde B)=-e_1$ on the left and $\tilde B\,\sigma(\tilde P)\,\tilde A=e_1$ in the untwisted swap, so the two disagree. The plain swap is recovered from the $\sigma$-swap exactly when the involution is the identity, which requires the ring to be commutative; this is why the general statement carries the involution in the target.

**Corollary (three names for one datum).** An involution of $\mathbb{B}$, an isomorphism of $\mathbb{B}$ with its opposite ring and an isomorphism of the regular bimodule with its $\sigma$-swap are the same datum; the two involutions of the ring, the quaternion conjugation and the Hermitian conjugation, give the two symmetries, and the twist of the preceding section is the same statement read on the left module alone.

## The Canonical Hermitian Form

### The sesquilinear forms

**Definition.** Let $M$ be a left $\mathbb{B}$-module and $\sigma$ an involution of $\mathbb{B}$. A map $h:M\times M\to\mathbb{B}$ is **$\sigma$-sesquilinear** if it is additive in each variable and

$$
h(\tilde A\tilde P,\tilde R)=\tilde A\,h(\tilde P,\tilde R),\qquad h(\tilde P,\tilde A\tilde R)=h(\tilde P,\tilde R)\,\sigma(\tilde A);
$$

it is **Hermitian** if in addition $h(\tilde R,\tilde P)=\sigma\bigl(h(\tilde P,\tilde R)\bigr)$.

### The canonical form of the regular module

**Proposition.** On ${}_{\mathbb{B}}\mathbb{B}$ the formula

$$
h(\tilde P,\tilde R)=\tilde P\,\tilde R^{*}
$$

is a Hermitian ${}^{*}$-sesquilinear form with values in $\mathbb{B}$, and it is non-degenerate: $h(\tilde P,\tilde R)=0$ for all $\tilde R$ forces $\tilde P=0$, and $h(\tilde P,\tilde R)=0$ for all $\tilde P$ forces $\tilde R=0$.

**Proof.** Additivity in each variable is the distributivity of $\mathbb{B}$. For the two sesquilinearity laws, $h(\tilde A\tilde P,\tilde R)=\tilde A\tilde P\tilde R^{*}=\tilde A\,h(\tilde P,\tilde R)$ and $h(\tilde P,\tilde A\tilde R)=\tilde P(\tilde A\tilde R)^{*}=\tilde P\tilde R^{*}\tilde A^{*}=h(\tilde P,\tilde R)\tilde A^{*}$. Hermitianity is $\bigl(\tilde P\tilde R^{*}\bigr)^{*}=\tilde R\tilde P^{*}=h(\tilde R,\tilde P)$, using ${}^{*}{}^{*}=\mathrm{id}$. For non-degeneracy, $h(\tilde P,e_0)=\tilde P$ and $h(e_0,\tilde R)=\tilde R^{*}$; a vector killed on one side by every argument is killed at the unit, and a vector whose every pairing is zero is killed at the unit on the other side and is zero.

**Remark (the two values of the form).** The form is left $\mathbb{B}$-linear and right ${}^{*}$-semilinear, and it is Hermitian rather than symmetric. Its scalar part recovers the scalar pairing of the layer,

$$
\mathrm{Sc}\,h(\tilde P,\tilde R)=\mathrm{Sc}(\tilde P\tilde R^{*})=\mathrm{Sc}(\tilde R^{*}\tilde P)=\langle\tilde P,\tilde R\rangle_{*},
$$

the inner product of *The Hermitian Form on the Biquaternion Algebra*, and the diagonal value

$$
\mathrm{Sc}\,h(\tilde P,\tilde P)=\mathrm{Sc}(\tilde P\tilde P^{*})=\sum_{\mu=0}^{3}|P_\mu|^{2}
$$

is the positive definite scalar part that the Euclidean topology of the layer uses. The form $h$ is thus the module-level origin of the scalar form, and the B-valued object is the finer one: it carries the whole product $\tilde P\tilde R^{*}$, of which the topology sees only the scalar part.

### The associated quadratic form

**Definition.** The **associated quadratic form** of $h$ is $q(\tilde P)=h(\tilde P,\tilde P)=\tilde P\tilde P^{*}$, the Hermitian form of *The Hermitian Form on the Biquaternion Algebra*.

**Proposition.** The quadratic form satisfies $q(\tilde A\tilde P)=\tilde A\,q(\tilde P)\tilde A^{*}$, so it is not $\mathbb{C}$-linear but equivariant; it takes its values in the Hermitian subspace $\mathbb{M}_+$, since $q(\tilde P)^{*}=q(\tilde P)$; it vanishes only at $\tilde P=0$, its scalar part being the sum of the squared moduli; and it determines $h$ by the polarisation identity

$$
h(\tilde P,\tilde R)+h(\tilde R,\tilde P)^{*}=q(\tilde P+\tilde R)-q(\tilde P)-q(\tilde R)=2\,h(\tilde P,\tilde R),
$$

so that $h(\tilde P,\tilde R)=\tfrac12\bigl(q(\tilde P+\tilde R)-q(\tilde P)-q(\tilde R)\bigr)$.

**Proof.** The equivariance is $q(\tilde A\tilde P)=\tilde A\tilde P(\tilde A\tilde P)^{*}=\tilde A\tilde P\tilde P^{*}\tilde A^{*}=\tilde A q(\tilde P)\tilde A^{*}$. Hermitianity of the values is $(\tilde P\tilde P^{*})^{*}=\tilde P\tilde P^{*}$, which is the statement that the complex sesquilinear form of an element lies in $\mathbb{M}_+$. Vanishing only at zero and the scalar part are computed in *The Hermitian Form on the Biquaternion Algebra*. For the polarisation, expanding $q(\tilde P+\tilde R)$ gives $q(\tilde P)+q(\tilde R)+\tilde P\tilde R^{*}+\tilde R\tilde P^{*}$; the last two terms are $h(\tilde P,\tilde R)$ and $h(\tilde P,\tilde R)^{*}$, so their sum is $2h(\tilde P,\tilde R)$ by Hermitianity, and $2$ is invertible in $\mathbb{B}$.

## The Isometries Are the Unitary Elements

**Proposition.** The $\mathbb{B}$-linear isometries of $h$ are exactly the right multiplications $R_{\tilde U}$ by the unitary elements $\tilde U\in U_{{}^{*}}(\mathbb{B})$, and they form a group isomorphic to $U_{{}^{*}}(\mathbb{B})$. A left multiplication $L_{\tilde U}$ is an isometry exactly when $\tilde U$ is a central unitary element, that is $\tilde U=\lambda e_0$ with $|\lambda|=1$.

**Proof.** The $\mathbb{B}$-linear endomorphisms of ${}_{\mathbb{B}}\mathbb{B}$ are the right multiplications $R_{\tilde B}$, $\operatorname{End}_{\mathbb{B}}({}_{\mathbb{B}}\mathbb{B})\cong\mathbb{B}^{\mathrm{op}}$, by *Biquaternions as a Module over Itself*. Now

$$
h(\tilde P\tilde B,\tilde R\tilde B)=\tilde P\tilde B(\tilde R\tilde B)^{*}=\tilde P\tilde B\tilde B^{*}\tilde R^{*}=\tilde P\,(\tilde B\tilde B^{*})\,\tilde R^{*},
$$

so $R_{\tilde B}$ preserves $h$ for all $\tilde P,\tilde R$ exactly when $\tilde B\tilde B^{*}=e_0$, the unitary condition. For a left multiplication $h(\tilde U\tilde P,\tilde U\tilde R)=\tilde U\,h(\tilde P,\tilde R)\tilde U^{*}$; testing at $\tilde P=\tilde R=e_0$ gives $\tilde U\tilde U^{*}=e_0$, and then $\tilde U\tilde S\tilde U^{*}=\tilde S$ for every $\tilde S$ in the image of $h$, which is all of $\mathbb{B}$ because $h(e_0,\tilde R)=\tilde R^{*}$ is surjective; multiplying $\tilde U\tilde S\tilde U^{*}=\tilde S$ on the right by $\tilde U$ and using $\tilde U^{*}\tilde U=e_0$ gives $\tilde U\tilde S=\tilde S\tilde U$, so $\tilde U$ is central. A central element of $\mathbb{B}$ is a complex scalar $\lambda e_0$, and $\tilde U\tilde U^{*}=|\lambda|^{2}e_0=e_0$ is $|\lambda|=1$.

**Corollary (the two readings of one element).** A unitary element that is not central acts as an isometry through $R_{\tilde U}$ and not through $L_{\tilde U}$, so the two one-sided readings of the same element differ as soon as the element is non-central. The right regular representation carries the unitary group $U_{{}^{*}}(\mathbb{B})\cong U(2)$ into the isometry group of $h$, and the left regular representation carries only its centre, the circle $U(1)$ of complex scalars of modulus one. This is the one-sided distinction of *One-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint* read on the form rather than on the operators.

**Remark (the parallel bilinear case).** The same construction with the natural sign gives the canonical form $h_{{}^{\natural}}(\tilde P,\tilde R)=\tilde P\tilde R^{\natural}$, whose scalar part is the quaternion bilinear form $\mathrm{Sc}(\tilde P\tilde R^{\natural})$ of *The Bilinear Form on the Biquaternion Algebra*, and whose $\mathbb{B}$-linear isometries are the right multiplications by the elements $\tilde U\tilde U^{\natural}=e_0$. The Hermitian case here and the bilinear case there are the two readings of one theorem, taken with the two involutions of the algebra; the form of the first is sesquilinear and positive on the diagonal, the form of the second is bilinear and indefinite, and the two agree on the quaternion subspace and differ by a sign on the anti-quaternion subspace, which is the comparison table of *Biquaternion Norm and Invertibility*.

## Summary

For an involution $\sigma$ of the biquaternion algebra and the left regular module ${}_{\mathbb{B}}\mathbb{B}$, the general theory of *The Regular Bimodule over an Involutive Ring* gives three structures, and the two involutions that are anti-automorphisms of the ring give them concretely. The twist $({}_{\mathbb{B}}\mathbb{B})^{\sigma}$ is the right regular module $\mathbb{B}_{\mathbb{B}}$ up to the comparison $\sigma$, an isomorphism of right modules. The involution is a bimodule isomorphism of ${}_{\mathbb{B}}\mathbb{B}_{\mathbb{B}}$ onto its $\sigma$-swap, $\sigma(\tilde A\tilde P\tilde B)=\sigma(\tilde B)\sigma(\tilde P)\sigma(\tilde A)$, and conversely every bimodule isomorphism of the regular bimodule onto its $\sigma$-swap is $\tilde P\mapsto\tilde D\sigma(\tilde P)$ with $\tilde D$ a central unit, the involution itself being the case $\tilde D=e_0$; over a noncommutative ring the involution must be carried in the target, the plain swap being its commutative case. The regular module carries the canonical Hermitian form $h(\tilde P,\tilde R)=\tilde P\tilde R^{*}$, ${}^{*}$-sesquilinear, Hermitian and non-degenerate, with associated quadratic form $q(\tilde P)=\tilde P\tilde P^{*}$ taking its values in the Hermitian subspace and polarisation identity with the factor $\tfrac12$. Its $\mathbb{B}$-linear isometries are the right multiplications $R_{\tilde U}$ by the unitary elements $\tilde U\tilde U^{*}=e_0$, forming the unitary group $U(2)$; a left multiplication is an isometry only for a central unitary, the complex scalars of modulus one. The scalar part of the form is the inner product of the layer, so the form here is the B-valued origin of the scalar Hermitian form, and the parallel construction with the quaternion conjugation is the origin of the quaternion bilinear form of the preceding group.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| ${}^{*}=\bar{\cdot}\circ{}^{\natural}$ | the Hermitian conjugation, the involution read here |
| ${}^{\natural}$, $\bar{\cdot}$, ${}^{\flat}$ | quaternion conjugation, coefficient conjugation, flat |
| $(\tilde P\tilde R)^{*}=\tilde R^{*}\tilde P^{*}$ | the star reverses the product |
| $\bar{\tilde P}\bar{\tilde R}=\overline{\tilde P\tilde R}$ | the bar reverses nothing, an automorphism |
| $({}_{\mathbb{B}}\mathbb{B})^{\sigma}$, $\tilde P\cdot\tilde Q=\sigma(\tilde Q)\tilde P$ | the twist of the left regular module |
| $\sigma:({}_{\mathbb{B}}\mathbb{B})^{\sigma}\to\mathbb{B}_{\mathbb{B}}$ | the twist of the left regular module is the right one |
| ${}^{\mathrm{sw}}{}_{\mathbb{B}}\mathbb{B}_{\mathbb{B}}^{\sigma}$ | the $\sigma$-swap of the regular bimodule |
| $\sigma(\tilde A\tilde P\tilde B)=\sigma(\tilde B)\sigma(\tilde P)\sigma(\tilde A)$ | the involution is the bimodule $\sigma$-swap isomorphism |
| $\varphi(\tilde P)=\tilde D\,\sigma(\tilde P)$, $\tilde D$ central unit | every bimodule $\sigma$-swap isomorphism, $\tilde D=\lambda e_0$ |
| $h(\tilde P,\tilde R)=\tilde P\tilde R^{*}$ | the canonical Hermitian form on ${}_{\mathbb{B}}\mathbb{B}$ |
| $h(\tilde A\tilde P,\tilde R)=\tilde A h$, $h(\tilde P,\tilde A\tilde R)=h\tilde A^{*}$ | ${}^{*}$-sesquilinearity |
| $h(\tilde R,\tilde P)=h(\tilde P,\tilde R)^{*}$ | Hermitianity |
| $q(\tilde P)=\tilde P\tilde P^{*}$, $q(\tilde A\tilde P)=\tilde A q\tilde A^{*}$ | the associated quadratic form, in $\mathbb{M}_+$ |
| $\mathrm{Sc}\,h(\tilde P,\tilde R)=\langle\tilde P,\tilde R\rangle_{*}$ | the scalar part is the inner product of the layer |
| $U_{{}^{*}}(\mathbb{B})=\{\tilde U:\tilde U\tilde U^{*}=e_0\}\cong U(2)$ | the unitary group, the isometries $R_{\tilde U}$ |
| $L_{\tilde U}$ is an isometry $\iff \tilde U=\lambda e_0$, $|\lambda|=1$ | the central unitary elements only |
| $h_{{}^{\natural}}(\tilde P,\tilde R)=\tilde P\tilde R^{\natural}$ | the parallel bilinear form, with scalar part $\langle\cdot,\cdot\rangle_{\natural}$ |

## Further Reading

- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for involutions, sesquilinear and Hermitian forms, and the unitary group.
- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the symmetric and the skew elements and the structure of rings with involution.
- Nathan Jacobson, *Structure of Rings* (American Mathematical Society, 1956), for the regular module of a ring with involution and the forms on it.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for involutions, the forms they define and the unitary groups.
- Tsit-Yuen Lam, *Lectures on Modules and Rings* (Springer, 1999), for the regular module, its endomorphism ring and the sesquilinear forms over a ring with involution.
