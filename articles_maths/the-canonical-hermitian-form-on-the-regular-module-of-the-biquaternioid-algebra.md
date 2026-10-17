# __The Canonical Hermitian Form on the Regular Module of the Biquaternioid Algebra__

## Introduction

An involution of a ring read on the regular module produces three structures at once: a **twist** that turns the left regular module into the right one, a **symmetry** of the regular bimodule with its swap through the involution, and a **general plain sesquilinear form** on the module with values in the ring itself, whose automorphisms are the unitary elements acting on the right. For the biquaternion algebra the involution is the Hermitian conjugation ${}^{*}$, and the three structures are the right module isomorphism

$$
{}^{*}:({}_{\mathbb{B}}\mathbb{B})^{*}\longrightarrow\mathbb{B}_{\mathbb{B}},
$$

the bimodule isomorphism of ${}_{\mathbb{B}}\mathbb{B}_{\mathbb{B}}$ with its swap through ${}^{*}$, and the canonical form

$$
h(\tilde P,\tilde Q_2)=\tilde P\tilde Q_2^{*},
$$

with values in $\mathbb{B}$, of which the scalar Hermitian form of the layer is the scalar part, $h(\tilde P,\tilde Q_2)$ having scalar part $\mathrm{Sc}(\tilde P \tilde Q_2^{*})=\langle\tilde P,\tilde Q_2\rangle_{*}$. The automorphisms of $h$ that are $\mathbb{B}$-linear are the right multiplications $R_{\tilde U}$ by the unitary elements $\tilde U\tilde U^{*}=e_t$, that is by the unitary group of *The Unitary Group of the Biquaternion Algebra*; a left multiplication $L_{\tilde U}$ is a form-preserving map only for a central unitary element, which here means a complex scalar of modulus one.

The form takes its values in $\mathbb{B}$ and carries no definite form of its own; the scalar form of the layer is *The 4 Forms over the Biquaternioid $\mathbb{C}$ Space*, whose value on a pair is the scalar part of the form here. The article assumes the general construction of *The Regular Bimodule over an Involutive Ring* for the twist, the swap and the canonical form, *Modules over an Involutive Ring* for the twist of a general module, *Involutive Rings* for the definitions of an involution and of the unitary elements, *Modules over the Biquaternion Algebra* for the module object and its endomorphisms, and *The Group of Involutions* for the four conjugations of the algebra. The positivity of the form and the operator theory that needs a norm are Part II and the following articles of this layer; no positivity and no norm is used here.

Throughout, $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ is the biquaternion algebra with complex basis $e_t,\vec e_x,\vec e_y,\vec e_z$, a generic element is $\tilde Q$, an idempotent is $\tilde\Pi$, the scalar part is $\mathrm{Sc}$, the two one-sided multiplications are $L_{\tilde Q}(\tilde P)=\tilde Q\tilde P$ and $R_{\tilde Q}(\tilde P)=\tilde P\tilde Q$, and the Hermitian conjugation is ${}^{*}=\bar{\cdot}\circ{}^{\natural}$, the composite of the coefficient conjugation and the quaternion conjugation.

## The Involution of the Algebra

### The two involutions of the ring

An **involution** of a ring $A$ is an anti-automorphism of order two, so that $\sigma(\tilde P\tilde Q_2)=\sigma(\tilde Q_2)\sigma(\tilde P)$ and $\sigma^2=\mathrm{id}$ (*Involutive Rings*). Of the four conjugations of *The Group of Involutions* two are involutions of the ring $\mathbb{B}$, and two are not.

| conjugation | reverses the product? | what it is |
|---|---|---|
| quaternion conjugation ${}^{\natural}$ | yes, $(\tilde P\tilde Q_2)^{\natural}=\tilde Q_2^{\natural}\tilde P^{\natural}$ | a $\mathbb{C}$-linear involution |
| Hermitian conjugation ${}^{*}$ | yes, $(\tilde P\tilde Q_2)^{*}=\tilde Q_2^{*}\tilde P^{*}$ | a $\mathbb{C}$-antilinear involution |
| coefficient conjugation $\bar{\cdot}$ | no, $\overline{\tilde P\tilde Q_2}=\bar{\tilde P}\bar{\tilde Q_2}$ | a $\mathbb{C}$-antilinear automorphism |
| anti-Hermitian conjugation ${}^{\flat}=-{}^{*}$ | no, $(\tilde P\tilde Q_2)^{\flat}=-\tilde Q_2^{\flat}\tilde P^{\flat}$ | neither, a skew anti-map |

**Proposition.** The quaternion conjugation ${}^{\natural}$ and the Hermitian conjugation ${}^{*}$ are involutions of the ring $\mathbb{B}$; the coefficient conjugation $\bar{\cdot}$ is an automorphism of order two, since $\bar{\tilde P}\bar{\tilde Q_2}=\overline{\tilde P\tilde Q_2}$, and it reverses nothing; the flat ${}^{\flat}$ is an involution of the element layer, ${}^{\flat}{}^{\flat}=\mathrm{id}$, and it is not multiplicative, since $(\tilde P\tilde Q_2)^{\flat}=-\tilde Q_2^{\flat}\tilde P^{\flat}$ carries the central sign.

**Proof.** The reversal of ${}^{\natural}$ and of ${}^{*}$ and the sign of the flat are computed in *The Group of Involutions*. For the coefficient conjugation, both $\tilde P\tilde Q_2$ and $\bar{\tilde P}\bar{\tilde Q_2}$ have the coefficients $\sum_{\mu,\nu} (P_\mu Q_\nu)$ and $\sum_{\mu,\nu}(\bar P_\mu \bar Q_\nu)$ in the basis $e_\mu e_\nu=e_t,\pm \vec e_x,\pm \vec e_y,\pm \vec e_z$, and coefficient-wise conjugation is a ring homomorphism of $\mathbb{C}$, so the two agree: $\bar{\cdot}$ is multiplicative and not an anti-automorphism. The flat is $-{}^{*}$ and the central sign $-e_t$ does not commute with the reversal, so it is not an anti-automorphism.

**Corollary (which theory applies).** The general theory of the regular bimodule over an involutive ring applies to $\mathbb{B}$ through ${}^{\natural}$ and through ${}^{*}$, and not through $\bar{\cdot}$ or ${}^{\flat}$. The two parallel structures are the two of this layer: the involution ${}^{*}$ gives the general plain sesquilinear form of the articles of this group, and the involution ${}^{\natural}$ gives the general quaternionic bilinear form of the preceding group; the coefficient conjugation is a symmetry of the real form of the algebra, and the flat is the mark of the Krein pairing of *The 4 Forms over the Biquaternioid $\mathbb{C}$ Space*.

### The unitary elements

**Definition.** Let $\sigma$ be an involution of $\mathbb{B}$. An element $\tilde U\in\mathbb{B}$ is **$\sigma$-unitary** when $\tilde U\sigma(\tilde U)=e_t$; because $\sigma$ is an involution and $\tilde U\sigma(\tilde U)=e_t$ makes $\tilde U$ invertible with inverse $\sigma(\tilde U)$, the condition is two-sided. The $\sigma$-unitary elements form the **unitary group** $U_\sigma(\mathbb{B})$.

**Proposition.** For $\sigma={}^{*}$ the unitary elements are those of *The Unitary Group of the Biquaternion Algebra*, the unitary subgroup $\mathrm{U}(2)$ of the unit group: the matrix model identifies $\mathsf{M}_2(\tilde U^{*})=\mathsf{M}_2(\tilde U)^{\dagger}$, so the condition $\tilde U\tilde U^{*}=e_t$ reads $UU^{*}=I$. For $\sigma={}^{\natural}$ the condition is $\tilde U\tilde U^{\natural}=e_t$; in the matrix model, where $\mathsf{M}_2(\tilde U^{\natural})=\varepsilon\,\mathsf{M}_2(\tilde U)^{\mathrm{T}}\varepsilon^{-1}$ with $\varepsilon=i\sigma_2$, it reads $\mathsf{M}_2(\tilde U)\,\varepsilon\,\mathsf{M}_2(\tilde U)^{\mathrm{T}}=\varepsilon$, so the $\natural$-unitary elements form the complex symplectic group $\mathrm{Sp}(2,\mathbb{C})\cong\mathrm{SL}_2(\mathbb{C})$, whose subgroup of real unit quaternions is the group of elements of norm one.

**Proof.** The statement for ${}^{*}$ is the definition of the unitary group of the algebra, recorded in *The Unitary Group of the Biquaternion Algebra*. For ${}^{\natural}$, the adjugate identity $\mathsf{M}_2(\tilde Q^{\natural})=\varepsilon\,\mathsf{M}_2(\tilde Q)^{\mathrm{T}}\varepsilon^{-1}$ is that of *Modules over the Biquaternion Algebra*, and it is an anti-automorphism of the matrix algebra; the condition $\tilde U\tilde U^{\natural}=e_t$ is therefore $\mathsf{M}_2(\tilde U)\,\varepsilon\,\mathsf{M}_2(\tilde U)^{\mathrm{T}}\varepsilon^{-1}=I$, which is the defining equation of the symplectic group in the basis selected by $\varepsilon$. A real unit quaternion has $\tilde q\tilde q^{\natural}=1$ because on the quaternion subspace the natural sign is the quaternion conjugation and the norm is positive definite, and the real unit quaternions are the norm-one set of $\mathbb{H}\cong\mathbb{R}^4$.

## The Twist of the Regular Module

**Definition.** The **twist** of a left $\mathbb{B}$-module $M$ by an involution $\sigma$ is the same additive group with the right scalar multiplication $\tilde P\cdot\tilde Q=\sigma(\tilde Q)\tilde P$ (*Modules over an Involutive Ring*).

**Proposition.** The involution $\sigma$ is an isomorphism of right $\mathbb{B}$-modules

$$
\sigma:({}_{\mathbb{B}}\mathbb{B})^{\sigma}\longrightarrow\mathbb{B}_{\mathbb{B}},\qquad \tilde P\mapsto\sigma(\tilde P),
$$

so the twist of the left regular module is the right regular module up to the comparison $\sigma$, and this comparison is exactly the involution.

**Proof.** The map $\sigma$ is bijective, being an involution, hence of order two; for the right actions, $\sigma(\tilde P\cdot\tilde Q)=\sigma(\sigma(\tilde Q)\tilde P)=\sigma(\tilde P)\sigma(\sigma(\tilde Q))=\sigma(\tilde P)\tilde Q$, which is the ordinary right action on $\sigma(\tilde P)$; and additivity is the additivity of $\sigma$.

**Corollary (the two cases).** Through the star the twist of ${}_{\mathbb{B}}\mathbb{B}$ is the right regular module $\mathbb{B}_{\mathbb{B}}$ under the antilinear comparison $\tilde P\mapsto\tilde P^{*}$; through the natural sign it is the same statement under a $\mathbb{C}$-linear comparison. The two one-sided regular modules, which the module theory of *Modules over the Biquaternion Algebra* keeps apart as $\mathbb{B}$ and $\mathbb{B}^{\mathrm{opp}}$, are interchangeable through an involution, and the statement $\mathbb{B}\cong\mathbb{B}^{\mathrm{opp}}$ of the module theory is the twist read backwards.

## The Involution Is the Symmetry of the Bimodule

**Definition.** Let $\sigma$ be an involution of $\mathbb{B}$. The **$\sigma$-swap** of the regular bimodule, written ${}^{\mathrm{sw}}{}_{\mathbb{B}}\mathbb{B}_{\mathbb{B}}^{\sigma}$, is the same additive group with the left and the right actions interchanged and read through $\sigma$:

$$
\tilde A\cdot\tilde Q_2=\tilde Q_2\sigma(\tilde A),\qquad \tilde Q_2\cdot\tilde Q_1=\sigma(\tilde Q_1)\tilde Q_2 .
$$

For the identity involution of a commutative ring the two actions are simply interchanged and the $\sigma$-swap is the **swap** of the bimodule; the involution is carried in the definition because over a noncommutative ring the two actions cannot be exchanged by themselves.

**Proposition.** An involution $\sigma$ is an isomorphism of bimodules

$$
\sigma:{}_{\mathbb{B}}\mathbb{B}_{\mathbb{B}}\longrightarrow{}^{\mathrm{sw}}{}_{\mathbb{B}}\mathbb{B}_{\mathbb{B}}^{\sigma},\qquad \sigma(\tilde A\tilde P\tilde Q_1)=\sigma(\tilde Q_1)\sigma(\tilde P)\sigma(\tilde A),
$$

and conversely every bimodule isomorphism ${}_{\mathbb{B}}\mathbb{B}_{\mathbb{B}}\to{}^{\mathrm{sw}}{}_{\mathbb{B}}\mathbb{B}_{\mathbb{B}}^{\sigma}$ is $\tilde P\mapsto\tilde D\,\sigma(\tilde P)$ with $\tilde D$ a central unit; it is an anti-automorphism, hence its own inverse when normalised at the unit, exactly when $\tilde D=e_t$. For the biquaternion algebra the central units are the non-zero complex scalars $\tilde D=\lambda e_t$, $\lambda\in\mathbb{C}^{\times}$, so each involution is one member of a one-parameter family of symmetries of the bimodule.

**Proof.** That $\sigma$ is bijective and additive is the definition of an involution. Inserting $\sigma$ into the target, $\tilde A\cdot\sigma(\tilde P)\cdot\tilde Q_1=\bigl(\sigma(\tilde Q_1)\sigma(\tilde P)\bigr)\sigma(\tilde A)=\sigma(\tilde Q_1)\sigma(\tilde P)\sigma(\tilde A)$, which is the anti-multiplicativity of $\sigma$ applied to $\tilde A\tilde P\tilde Q_1$; so $\sigma$ intertwines the two structures. For the converse, let $\varphi$ be such an isomorphism and put $\tilde D=\varphi(e_t)$. Left linearity gives $\varphi(\tilde A)=\tilde A\cdot\varphi(e_t)=\varphi(e_t)\sigma(\tilde A)=\tilde D\sigma(\tilde A)$, and right linearity gives $\varphi(\tilde Q_1)=\varphi(e_t)\cdot\tilde Q_1=\sigma(\tilde Q_1)\varphi(e_t)=\sigma(\tilde Q_1)\tilde D$; the two agree on every element exactly when $\tilde D$ commutes with every $\sigma(\tilde Q_1)$, that is when $\tilde D$ is central, and it is a unit because $\varphi$ is bijective. Then $\varphi(\tilde A\tilde Q_1)=\tilde D\sigma(\tilde A\tilde Q_1)$ while $\varphi(\tilde Q_1)\varphi(\tilde A)=\tilde D\sigma(\tilde Q_1)\tilde D\sigma(\tilde A)=\tilde D^2\sigma(\tilde Q_1)\sigma(\tilde A)$, so $\varphi$ is an anti-homomorphism exactly when $\tilde D=e_t$, and then it is the involution $\sigma$. The central units are the non-zero complex scalars by the centre computation of *The Biquaternioid as a Vector Space over $\mathbb{C}$*.

**Remark (why the involution cannot be dropped).** Over a noncommutative ring the untwisted swap, with the two actions exchanged and nothing else, is **not** the target of the involution: for the star of the biquaternion algebra the element $\tilde A=\vec e_x$, $\tilde P=\tilde Q_1=e_t$ gives $\sigma(\tilde A\tilde P\tilde Q_1)=-\vec e_x$ on the left and $\tilde Q_1\,\sigma(\tilde P)\,\tilde A=\vec e_x$ in the untwisted swap, so the two disagree. The plain swap is recovered from the $\sigma$-swap exactly when the involution is the identity, which requires the ring to be commutative; this is why the general statement carries the involution in the target.

**Corollary (three names for one datum).** An involution of $\mathbb{B}$, an isomorphism of $\mathbb{B}$ with its opposite ring and an isomorphism of the regular bimodule with its $\sigma$-swap are the same datum; the two involutions of the ring, the quaternion conjugation and the Hermitian conjugation, give the two symmetries, and the twist of the preceding section is the same statement read on the left module alone.

## The Canonical Hermitian Form

### The sesquilinear forms

**Definition.** Let $M$ be a left $\mathbb{B}$-module and $\sigma$ an involution of $\mathbb{B}$. A map $h:M\times M\to\mathbb{B}$ is **$\sigma$-sesquilinear** if it is additive in each variable and

$$
h(\tilde A\tilde P,\tilde Q_2)=\tilde A\,h(\tilde P,\tilde Q_2),\qquad h(\tilde P,\tilde A\tilde Q_2)=h(\tilde P,\tilde Q_2)\,\sigma(\tilde A);
$$

it is **Hermitian** if in addition $h(\tilde Q_2,\tilde P)=\sigma\bigl(h(\tilde P,\tilde Q_2)\bigr)$.

### The canonical form of the regular module

**Proposition.** On ${}_{\mathbb{B}}\mathbb{B}$ the formula

$$
h(\tilde P,\tilde Q_2)=\tilde P\,\tilde Q_2^{*}
$$

is a Hermitian ${}^{*}$-sesquilinear form with values in $\mathbb{B}$, and it is non-degenerate: $h(\tilde P,\tilde Q_2)=0$ for all $\tilde Q_2$ forces $\tilde P=0$, and $h(\tilde P,\tilde Q_2)=0$ for all $\tilde P$ forces $\tilde Q_2=0$.

**Proof.** Additivity in each variable is the distributivity of $\mathbb{B}$. For the two sesquilinearity laws, $h(\tilde A\tilde P,\tilde Q_2)=\tilde A\tilde P\tilde Q_2^{*}=\tilde A\,h(\tilde P,\tilde Q_2)$ and $h(\tilde P,\tilde A\tilde Q_2)=\tilde P(\tilde A\tilde Q_2)^{*}=\tilde P\tilde Q_2^{*}\tilde A^{*}=h(\tilde P,\tilde Q_2)\tilde A^{*}$. Hermitianity is $\bigl(\tilde P\tilde Q_2^{*}\bigr)^{*}=\tilde Q_2\tilde P^{*}=h(\tilde Q_2,\tilde P)$, using ${}^{*}{}^{*}=\mathrm{id}$. For non-degeneracy, $h(\tilde P,e_t)=\tilde P$ and $h(e_t,\tilde Q_2)=\tilde Q_2^{*}$; a vector killed on one side by every argument is killed at the unit, and a vector whose every pairing is zero is killed at the unit on the other side and is zero.

**Remark (the two values of the form).** The form is left $\mathbb{B}$-linear and right ${}^{*}$-semilinear, and it is Hermitian rather than symmetric. Its scalar part recovers the scalar pairing of the layer,

$$
\mathrm{Sc}\,h(\tilde P,\tilde Q_2)=\mathrm{Sc}(\tilde P\tilde Q_2^{*})=\mathrm{Sc}(\tilde Q_2^{*}\tilde P)=\langle\tilde P,\tilde Q_2\rangle_{*},
$$

the inner product of *The 4 Forms over the Biquaternioid $\mathbb{C}$ Space*, and the diagonal value

$$
\mathrm{Sc}\,h(\tilde P,\tilde P)=\mathrm{Sc}(\tilde P\tilde P^{*})=\sum_{\mu\in\{t,x,y,z\}}|P_\mu|^{2}
$$

is the positive definite scalar part of the layer. The form $h$ is thus the module-level origin of the scalar form, and the B-valued object is the finer one: it carries the whole product $\tilde P\tilde Q_2^{*}$, of which the scalar form sees only the scalar part.

### The associated quadratic form

**Definition.** The **associated quadratic form** of $h$ is $\mathfrak{Q}(\tilde P)=h(\tilde P,\tilde P)=\tilde P\tilde P^{*}$, the Hermitian form of *The 4 Forms over the Biquaternioid $\mathbb{C}$ Space*.

**Proposition.** The quadratic form satisfies $\mathfrak{Q}(\tilde A\tilde P)=\tilde A\,\mathfrak{Q}(\tilde P)\tilde A^{*}$, so it is not $\mathbb{C}$-linear but equivariant; it takes its values in the Hermitian subspace $\mathbb{M}_+$, since $\mathfrak{Q}(\tilde P)^{*}=\mathfrak{Q}(\tilde P)$; it vanishes only at $\tilde P=0$, its scalar part being the sum of the squared moduli; and it determines $h$ by the polarisation identity

$$
h(\tilde P,\tilde Q_2)+h(\tilde Q_2,\tilde P)^{*}=\mathfrak{Q}(\tilde P+\tilde Q_2)-\mathfrak{Q}(\tilde P)-\mathfrak{Q}(\tilde Q_2)=2\,h(\tilde P,\tilde Q_2),
$$

so that $h(\tilde P,\tilde Q_2)=\tfrac12\bigl(\mathfrak{Q}(\tilde P+\tilde Q_2)-\mathfrak{Q}(\tilde P)-\mathfrak{Q}(\tilde Q_2)\bigr)$.

**Proof.** The equivariance is $\mathfrak{Q}(\tilde A\tilde P)=\tilde A\tilde P(\tilde A\tilde P)^{*}=\tilde A\tilde P\tilde P^{*}\tilde A^{*}=\tilde A \mathfrak{Q}(\tilde P)\tilde A^{*}$. Hermitianity of the values is $(\tilde P\tilde P^{*})^{*}=\tilde P\tilde P^{*}$, which is the statement that the general plain sesquilinear form of an element lies in $\mathbb{M}_+$. Vanishing only at zero and the scalar part are computed in *Norm and Invertibility in the General Quaternionic Algebra*. For the polarisation, expanding $\mathfrak{Q}(\tilde P+\tilde Q_2)$ gives $\mathfrak{Q}(\tilde P)+\mathfrak{Q}(\tilde Q_2)+\tilde P\tilde Q_2^{*}+\tilde Q_2\tilde P^{*}$; the last two terms are $h(\tilde P,\tilde Q_2)$ and $h(\tilde P,\tilde Q_2)^{*}$, so their sum is $2h(\tilde P,\tilde Q_2)$ by Hermitianity, and $2$ is invertible in $\mathbb{B}$.

## The Automorphisms Are the Unitary Elements

**Proposition.** The $\mathbb{B}$-linear automorphisms of $h$ are exactly the right multiplications $R_{\tilde U}$ by the unitary elements $\tilde U\in U_{{}^{*}}(\mathbb{B})$, and they form a group isomorphic to $U_{{}^{*}}(\mathbb{B})$. A left multiplication $L_{\tilde U}$ is a form-preserving map exactly when $\tilde U$ is a central unitary element, that is $\tilde U=\lambda e_t$ with $|\lambda|=1$.

**Proof.** The $\mathbb{B}$-linear endomorphisms of ${}_{\mathbb{B}}\mathbb{B}$ are the right multiplications $R_{\tilde Q_1}$, $\operatorname{End}_{\mathbb{B}}({}_{\mathbb{B}}\mathbb{B})\cong\mathbb{B}^{\mathrm{opp}}$, by *Modules over the Biquaternion Algebra*. Now

$$
h(\tilde P\tilde Q_1,\tilde Q_2\tilde Q_1)=\tilde P\langle\tilde Q_2\tilde Q_1\rangle^{*}=\tilde P\tilde Q_1\tilde Q_1^{*}\tilde Q_2^{*}=\tilde P\,(\tilde Q_1\tilde Q_1^{*})\,\tilde Q_2^{*},
$$

so $R_{\tilde Q_1}$ preserves $h$ for all $\tilde P,\tilde Q_2$ exactly when $\tilde Q_1\tilde Q_1^{*}=e_t$, the unitary condition. For a left multiplication $h(\tilde U\tilde P,\tilde U\tilde Q_2)=\tilde U\,h(\tilde P,\tilde Q_2)\tilde U^{*}$; testing at $\tilde P=\tilde Q_2=e_t$ gives $\tilde U\tilde U^{*}=e_t$, and then $\tilde U\tilde S\tilde U^{*}=\tilde S$ for every $\tilde S$ in the image of $h$, which is all of $\mathbb{B}$ because $h(e_t,\tilde Q_2)=\tilde Q_2^{*}$ is surjective; multiplying $\tilde U\tilde S\tilde U^{*}=\tilde S$ on the right by $\tilde U$ and using $\tilde U^{*}\tilde U=e_t$ gives $\tilde U\tilde S=\tilde S\tilde U$, so $\tilde U$ is central. A central element of $\mathbb{B}$ is a complex scalar $\lambda e_t$, and $\tilde U\tilde U^{*}=|\lambda|^{2}e_t=e_t$ is $|\lambda|=1$.

**Corollary (the two readings of one element).** A unitary element that is not central acts as a form-preserving map through $R_{\tilde U}$ and not through $L_{\tilde U}$, so the two one-sided readings of the same element differ as soon as the element is non-central. The right regular representation carries the unitary group $U_{{}^{*}}(\mathbb{B})\cong \mathrm{U}(2)$ into the automorphism group of $h$, and the left regular representation carries only its centre, the circle $\mathrm{U}(1)$ of complex scalars of modulus one. This is the one-sided distinction of *One-Sided Operators on the General Plain Sesqualgebra* read on the form rather than on the operators.

**Remark (the parallel bilinear case).** The same construction with the natural sign gives the canonical form $h_{{}^{\natural}}(\tilde P,\tilde Q_2)=\tilde P\tilde Q_2^{\natural}$, whose scalar part is the general quaternionic bilinear form $\mathrm{Sc}(\tilde P\tilde Q_2^{\natural})$ of *The 4 Forms over the Biquaternioid $\mathbb{C}$ Space*, and whose $\mathbb{B}$-linear automorphisms are the right multiplications by the elements $\tilde U\tilde U^{\natural}=e_t$. The Hermitian case here and the bilinear case there are the two readings of one theorem, taken with the two involutions of the algebra; the form of the first is sesquilinear and positive on the diagonal, the form of the second is bilinear and indefinite, and the two agree on the quaternion subspace and differ by a sign on the anti-quaternion subspace, which is the comparison table of *Norm and Invertibility in the General Quaternionic Algebra*.

## Summary

For an involution $\sigma$ of the biquaternion algebra and the left regular module ${}_{\mathbb{B}}\mathbb{B}$, the general theory of *The Regular Bimodule over an Involutive Ring* gives three structures, and the two involutions that are anti-automorphisms of the ring give them concretely. The twist $({}_{\mathbb{B}}\mathbb{B})^{\sigma}$ is the right regular module $\mathbb{B}_{\mathbb{B}}$ up to the comparison $\sigma$, an isomorphism of right modules. The involution is a bimodule isomorphism of ${}_{\mathbb{B}}\mathbb{B}_{\mathbb{B}}$ onto its $\sigma$-swap, $\sigma(\tilde A\tilde P\tilde Q_1)=\sigma(\tilde Q_1)\sigma(\tilde P)\sigma(\tilde A)$, and conversely every bimodule isomorphism of the regular bimodule onto its $\sigma$-swap is $\tilde P\mapsto\tilde D\sigma(\tilde P)$ with $\tilde D$ a central unit, the involution itself being the case $\tilde D=e_t$; over a noncommutative ring the involution must be carried in the target, the plain swap being its commutative case. The regular module carries the canonical Hermitian form $h(\tilde P,\tilde Q_2)=\tilde P\tilde Q_2^{*}$, ${}^{*}$-sesquilinear, Hermitian and non-degenerate, with associated quadratic form $\mathfrak{Q}(\tilde P)=\tilde P\tilde P^{*}$ taking its values in the Hermitian subspace and polarisation identity with the factor $\tfrac12$. Its $\mathbb{B}$-linear automorphisms are the right multiplications $R_{\tilde U}$ by the unitary elements $\tilde U\tilde U^{*}=e_t$, forming the unitary group $\mathrm{U}(2)$; a left multiplication is a form-preserving map only for a central unitary, the complex scalars of modulus one. The scalar part of the form is the inner product of the layer, so the form here is the B-valued origin of the scalar Hermitian form, and the parallel construction with the quaternion conjugation is the origin of the general quaternionic bilinear form of the preceding group.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| ${}^{*}=\bar{\cdot}\circ{}^{\natural}$ | the Hermitian conjugation, the involution read here |
| ${}^{\natural}$, $\bar{\cdot}$, ${}^{\flat}$ | quaternion conjugation, coefficient conjugation, flat |
| $(\tilde P\tilde Q_2)^{*}=\tilde Q_2^{*}\tilde P^{*}$ | the star reverses the product |
| $\bar{\tilde P}\bar{\tilde Q_2}=\overline{\tilde P\tilde Q_2}$ | the bar reverses nothing, an automorphism |
| $({}_{\mathbb{B}}\mathbb{B})^{\sigma}$, $\tilde P\cdot\tilde Q=\sigma(\tilde Q)\tilde P$ | the twist of the left regular module |
| $\sigma:({}_{\mathbb{B}}\mathbb{B})^{\sigma}\to\mathbb{B}_{\mathbb{B}}$ | the twist of the left regular module is the right one |
| ${}^{\mathrm{sw}}{}_{\mathbb{B}}\mathbb{B}_{\mathbb{B}}^{\sigma}$ | the $\sigma$-swap of the regular bimodule |
| $\sigma(\tilde A\tilde P\tilde Q_1)=\sigma(\tilde Q_1)\sigma(\tilde P)\sigma(\tilde A)$ | the involution is the bimodule $\sigma$-swap isomorphism |
| $\varphi(\tilde P)=\tilde D\,\sigma(\tilde P)$, $\tilde D$ central unit | every bimodule $\sigma$-swap isomorphism, $\tilde D=\lambda e_t$ |
| $h(\tilde P,\tilde Q_2)=\tilde P\tilde Q_2^{*}$ | the canonical Hermitian form on ${}_{\mathbb{B}}\mathbb{B}$ |
| $h(\tilde A\tilde P,\tilde Q_2)=\tilde A h$, $h(\tilde P,\tilde A\tilde Q_2)=h\tilde A^{*}$ | ${}^{*}$-sesquilinearity |
| $h(\tilde Q_2,\tilde P)=h(\tilde P,\tilde Q_2)^{*}$ | Hermitianity |
| $\mathfrak{Q}(\tilde P)=\tilde P\tilde P^{*}$, $\mathfrak{Q}(\tilde A\tilde P)=\tilde A\mathfrak{Q}(\tilde P)\tilde A^{*}$ | the associated quadratic form, in $\mathbb{M}_+$ |
| $\mathrm{Sc}\,h(\tilde P,\tilde Q_2)=\langle\tilde P,\tilde Q_2\rangle_{*}$ | the scalar part is the inner product of the layer |
| $U_{{}^{*}}(\mathbb{B})=\{\tilde U:\tilde U\tilde U^{*}=e_t\}\cong \mathrm{U}(2)$ | the unitary group, the automorphisms $R_{\tilde U}$ |
| $L_{\tilde U}$ is a form-preserving map $\iff \tilde U=\lambda e_t$, $\lvert\lambda\rvert=1$ | the central unitary elements only |
| $h_{{}^{\natural}}(\tilde P,\tilde Q_2)=\tilde P\tilde Q_2^{\natural}$ | the parallel bilinear form, with scalar part $\langle\cdot,\cdot\rangle_{\natural}$ |

## Further Reading

- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for involutions, sesquilinear and Hermitian forms, and the unitary group.
- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the symmetric and the skew elements and the structure of rings with involution.
- Nathan Jacobson, *Structure of Rings* (American Mathematical Society, 1956), for the regular module of a ring with involution and the forms on it.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for involutions, the forms they define and the unitary groups.
- Tsit-Yuen Lam, *Lectures on Modules and Rings* (Springer, 1999), for the regular module, its endomorphism ring and the sesquilinear forms over a ring with involution.
