
# __Split-Complex Exponential and Lie Group Structure__

## Introduction

This article develops the Lie theory of the split-complex algebra $\mathbb{D} = \mathbb{R}[x]/(x^2-1)$. The algebra article defined $\mathbb{D}$ with basis $1$, $j$, $j^2 = +1$; the norm article identified the units $\mathbb{D}^\times$ with the elements of nonzero norm $N(A) = a^2-a'^2$; and the idempotent article supplied the decomposition $\mathbb{D}\cong\mathbb{R}\oplus\mathbb{R}$. Here these are assembled into the standard theory of $\mathbb{D}^\times$ as a Lie group, of $\mathbb{D}$ as its abelian Lie algebra, and of the exponential map. It is the two-dimensional counterpart of the biquaternion Lie-algebra and Lie-group theory of *The 12 Products of the Biquaternion Complex Space* and *Biquaternion Lie Group and Exponential Structure*, and every statement is a special case of the elementary Lie theory of $\mathbb{R}^\times$ and its square.

The one point that governs everything below is that $\mathbb{D}$ is **commutative**. Its commutator bracket vanishes, so it is an abelian Lie algebra; the exponential of a sum is the product of the exponentials; and the exponential map is a local diffeomorphism everywhere but is injective, unlike the matrix case. The price is a small unit group: $\mathbb{D}^\times$ has **four components** rather than being connected, and the exponential reaches only the identity component. The article states this geometry exactly.

The article owns the abelian Lie algebra structure of $\mathbb{D}$, the exponential and its closed forms in the two bases, the group of units and its exponential parametrisation, the four components, the non-compact hyperbolic subgroup, the one-parameter subgroups of the geometry slot, and the comparison with $\mathbb{C}$ and $\mathbb{B}$. It assumes the norm and invertibility theory of *Split-Complex Norm and Invertibility*, the idempotents of *Split-Complex Idempotents and Projections*, and the exponential parametrisation of the units; the hyperbolic one-parameter group is the subject of *Hyperbolic Rotations*, and the automorphisms and derivations are treated in *Split-Complex Automorphisms and Derivations*.

**Conventions.** $A = a+ja'$, $a,a'\in\mathbb{R}$; conjugate $\bar A = a-ja'$; idempotents $\Pi_\pm = \tfrac12(1\pm j)$; idempotent coordinates $A_\pm = a\pm a'$, with $A = A_+\Pi_1 + A_-\Pi_2$; norm $N(A) = A\bar A = a^2-a'^2$; group of units $\mathbb{D}^\times = \{A : N(A)\neq 0\}$; unit-norm set $\mathbb{D}^{(1)} = \{A : N(A) = 1\}$. The identity component of a group $G$ is written $G_0$.

## The Algebra as an Abelian Lie Algebra

**Definition.** The **commutator bracket** on $\mathbb{D}$ is

$$
[A,B] = AB - BA, \qquad A, B \in \mathbb{D}.
$$

**Proposition.** The bracket is identically zero, and $(\mathbb{D}, [\ ,\ ])$ is the abelian real Lie algebra of dimension $2$.

**Proof.** $\mathbb{D}$ is commutative, so $AB = BA$ for all $A,B$ and every bracket vanishes. A Lie algebra with zero bracket is abelian, and the underlying real vector space is two-dimensional.

**Remark.** The bracket rules out every phenomenon of the biquaternion case that depends on noncommutativity: there are no nontrivial inner derivations, no Baker–Campbell–Hausdorff correction, no Ad-action distinct from the identity, and no $\mathrm{SL}$-summand. In the idempotent basis the Lie algebra is the direct sum of two one-dimensional abelian Lie algebras, $\mathbb{D} = \mathrm{I}_+ \oplus \mathrm{I}_-$ with $\mathrm{I}_\pm = \mathbb{R}\Pi_\pm$, and every subspace is an abelian ideal.

## The Exponential: Series and Closed Form

**Definition.** The **exponential** of $A \in \mathbb{D}$ is the sum of the absolutely convergent series

$$
\exp(A) = \sum_{n=0}^{\infty} \frac{A^n}{n!},
$$

convergent in the Euclidean topology of $\mathbb{D}\cong\mathbb{R}^2$.

**Theorem (closed form).** For $A = A_+\Pi_1 + A_-\Pi_2$ and for $A = a+ja'$,

$$
\exp(A) = e^{A_+} \Pi_1 + e^{A_-} \Pi_2, \qquad \exp(a+ja') = e^{a}\bigl(\cosh a' + j \sinh a'\bigr) = e^{a}\cosh a' + e^{a}\sinh a'\, j .
$$

**Proof.** The idempotents satisfy $\Pi_\pm^2 = \Pi_\pm$ and $\Pi_1\Pi_2 = 0$, so for $n \geq 0$

$$
A^n = (A_+\Pi_1 + A_-\Pi_2)^n = A_+^n \Pi_1 + A_-^n \Pi_2,
$$

and summing the two geometric pieces gives $\exp(A) = \bigl(\sum_n A_+^n/n!\bigr)\Pi_1 + \bigl(\sum_n A_-^n/n!\bigr)\Pi_2 = e^{A_+}\Pi_1 + e^{A_-}\Pi_2$. For the second form, substitute $A_+ = a+a'$, $A_- = a-a'$ and rewrite in the basis $\{1, j\}$:

$$
e^{a+a'}\Pi_1 + e^{a-a'}\Pi_2 = e^{a}\bigl(e^{a'}\Pi_1 + e^{-a'}\Pi_2\bigr) = e^{a}\bigl(\cosh a'\,(\Pi_1 + \Pi_2) + \sinh a'\,(\Pi_1 - \Pi_2)\bigr) = e^{a}\bigl(\cosh a' + j\sinh a'\bigr),
$$

since $\Pi_1 + \Pi_2 = 1$ and $\Pi_1 - \Pi_2 = j$.

**Corollary (the norm of an exponential is positive).** For every $A$,

$$
N(\exp(A)) = \exp(A_+)\exp(A_-) = e^{A_+ + A_-} = e^{2a} > 0 .
$$

So $\exp(\mathbb{D})$ lies in the component of positive norm, and in particular $\exp$ never produces a zero divisor. This is the elementary statement, in the group, that $\exp$ takes values in $\mathbb{D}^\times$ with $N>0$.

## The Group of Units

**Definition.** The **group of units** of $\mathbb{D}$ is $\mathbb{D}^\times = \{A \in \mathbb{D} : N(A)\neq 0\}$, with the multiplication of the algebra.

**Theorem.** The idempotent-coordinate map is an isomorphism of groups

$$
\mathbb{D}^\times \;\cong\; \mathbb{R}^\times \times \mathbb{R}^\times, \qquad A \longmapsto (A_+, A_-),
$$

and consequently $\mathbb{D}^\times$ is an abelian real Lie group of dimension $2$, non-compact, with four connected components.

**Proof.** In the idempotent basis multiplication is componentwise, $(AB)_\pm = A_\pm B_\pm$, and $A$ is a unit iff $A_+ A_- = N(A) \neq 0$ iff both $A_+ \neq 0$ and $A_- \neq 0$. The map to $\mathbb{R}^\times \times \mathbb{R}^\times$ is therefore a group isomorphism onto its image, which is all of $\mathbb{R}^\times\times\mathbb{R}^\times$. Each factor $\mathbb{R}^\times$ is a one-dimensional Lie group with two components, so the product has dimension $2$ and $2\times 2 = 4$ components; it is non-compact because $\mathbb{R}^\times$ is.

**Corollary (component count).** The four components are the products of the two signs of the idempotent coordinates,

$$
(\mathbb{D}^\times)_{(\varepsilon_+,\varepsilon_-)} = \{A : \varepsilon_+ A_+ > 0, \ \varepsilon_- A_- > 0\}, \qquad \varepsilon_\pm \in \{\pm 1\},
$$

so $\pi_0(\mathbb{D}^\times) \cong (\mathbb{Z}/2)^2$. Each component is an open quadrant in the $(A_+, A_-)$ coordinates, hence contractible and diffeomorphic to $\mathbb{R}^2$; in particular every component is simply connected, and the identity component is

$$
(\mathbb{D}^\times)_0 = \{A : A_+ > 0, \ A_- > 0\} = \{a > \lvert a'\rvert\} = \{N(A) > 0, \ a > 0\},
$$

the open cone of positive norm pointing along the real axis.

## The Exponential Map: Image and Kernel

**Theorem (the exponential is a diffeomorphism onto the identity component).** The exponential restricts to a diffeomorphism of smooth manifolds

$$
\exp : \mathbb{D} \longrightarrow (\mathbb{D}^\times)_0, \qquad (a,a') \longmapsto \bigl(e^a\cosh a', \ e^a\sinh a'\bigr),
$$

whose inverse is

$$
\exp^{-1}(a + ja') = \tfrac12 \ln(a^2 - a'^2) + \operatorname{artanh}\!\Bigl(\frac{a'}{a}\Bigr) j, \qquad a > \lvert a'\rvert .
$$

**Proof.** On the identity component $a > \lvert a'\rvert$ one has $a^2 - a'^2 > 0$ and $\lvert a'/a\rvert < 1$, so the stated inverse is defined and smooth. Composing the two maps in either order returns the argument, using $\cosh^2 a' - \sinh^2 a' = 1$ and the addition formulas for $\cosh$ and $\sinh$; hence both are bijections and, being smooth with smooth inverse, diffeomorphisms.

**Corollary (the exponential is injective, and not surjective).** If $\exp(A) = 1$ then $e^{A_+} = e^{A_-} = 1$, and since the real exponential is injective this gives $A_+ = A_- = 0$, so $A = 0$: the kernel of $\exp$ is trivial. The image is the identity component only, so $\exp$ is not surjective onto $\mathbb{D}^\times$ and misses the three components of negative $A_+$ or negative $A_-$.

**Remark (the group law).** Because the algebra is abelian, the exponential satisfies $\exp(A)\exp(B) = \exp(A+B)$ for all $A, B$, with no correction term; equivalently $\exp$ is a group isomorphism $(\mathbb{D}, +) \to ((\mathbb{D}^\times)_0, \cdot)$. The identity component is therefore an exponential group, and the whole unit group is its product with the finite group $(\mathbb{Z}/2)^2$ of components, $\mathbb{D}^\times \cong (\mathbb{D}^\times)_0 \times (\mathbb{Z}/2)^2$. This is the sharpest contrast with the biquaternion algebra, where the exponential is surjective onto $GL(2,\mathbb{C})$ but has a large kernel and $\exp(A)\exp(B)\neq\exp(A+B)$ in general.

**Remark (the Lie correspondence).** Since $\exp : \mathbb{D}\to(\mathbb{D}^\times)_0$ is a diffeomorphism and a group isomorphism, the Lie functor recovers the algebra. The Lie algebra of the unit group is $\operatorname{Lie}(\mathbb{D}^\times) = \mathbb{D}$ with the zero bracket, and $\exp$ is the exponential map of the Lie group. This is the two-dimensional quantity that the algebra contributes to the Lie picture, in place of the vanishing derivation space of *Split-Complex Automorphisms and Derivations*.

## The Exponential Parametrisation

**Definition.** The **modulus** of $A\in\mathbb{D}^\times$ is $\rho(A) = \sqrt{\lvert N(A)\rvert} > 0$, and the **direction** is $u(A) = A/\rho(A)$, an element of the unit-modulus set

$$
\mathbb{D}^{(\pm 1)} = \{u : \lvert N(u)\rvert = 1\} = \mathbb{D}^{(1)} \cup (-\mathbb{D}^{(1)}), \qquad \mathbb{D}^{(1)} = \{u : N(u) = 1\}.
$$

**Theorem (exponential parametrisation of the units).** Every unit factors uniquely as

$$
A = \rho\, u, \qquad \rho = \sqrt{\lvert N(A)\rvert} > 0, \quad \lvert N(u)\rvert = 1,
$$

and the direction takes one of four branch forms, according to the component of $A$:

$$
u = \pm\, e^{j\theta} \ (\text{if } N(A) > 0), \qquad u = \pm\, j\, e^{j\theta} \ (\text{if } N(A) < 0), \qquad \theta \in \mathbb{R},
$$

so that

$$
A = \pm\, \sqrt{N(A)}\; e^{j\theta} \ (N(A) > 0), \qquad A = \pm\, \sqrt{-N(A)}\; j\, e^{j\theta} \ (N(A) < 0).
$$

**Proof.** Set $\rho = \sqrt{\lvert N(A)\rvert}$, which is positive for a unit, and $u = A/\rho$, so that $N(u) = N(A)/\rho^2 = \pm 1$, giving $\lvert N(u)\rvert = 1$ and the uniqueness of the factorisation. If $N(A) > 0$ then $N(u) = 1$, and $\lvert a\rvert > \lvert a'\rvert$; on the branch $a > 0$ write $a/\rho = \cosh\theta$, $a'/\rho = \sinh\theta$ for the unique $\theta\in\mathbb{R}$ with $\operatorname{sgn}\theta = \operatorname{sgn} a'$, and then $u = \cosh\theta + j\sinh\theta = e^{j\theta}$; the branch $a<0$ gives the sign $-$. If $N(A) < 0$ then $N(u) = -1$ and $\lvert a'\rvert > \lvert a\rvert$; write $a'/\rho = \pm\cosh\theta$, $a/\rho = \sinh\theta$, giving $u = \sinh\theta + j\cosh\theta = j e^{j\theta}$ up to the sign. The four cases are exactly the four components.

**Remark (two regimes).** The polar parametrisation has two regimes, hyperbolic-rotation-like on the components $N > 0$ and hyperbolic-translation-like on the components $N < 0$; the modulus is $\sqrt{\lvert N\rvert}$ and the angle is $\operatorname{artanh}(a'/a)$ in the first regime and $\operatorname{arcoth}$-like in the second. The present article records only the group factorisation $\mathbb{D}^\times \cong \mathbb{R}_{>0}\times \mathbb{D}^{(\pm 1)}$ that the parametrisation supplies.

## The Unit-Norm Group and the Hyperbolic Subgroup

**Definition.** The **unit-norm group** is $\mathbb{D}^{(1)} = \{A : N(A) = 1\}$, and the **hyperbolic subgroup** is its identity component

$$
\mathbb{D}^{(1)}_0 = \{A : N(A) = 1, \ a > 0\} = \{e^{jt} : t\in\mathbb{R}\}, \qquad e^{jt} = \cosh t + j\sinh t .
$$

**Theorem.** The unit-norm group is the abelian Lie group

$$
\mathbb{D}^{(1)} \;\cong\; \mathbb{Z}/2 \times \mathbb{R} \;\cong\; \{\pm 1\}\times\{e^{jt}\},
$$

with two connected components $\mathbb{D}^{(1)}_0 = \{e^{jt}\}$ and $-\mathbb{D}^{(1)}_0 = \{-e^{jt}\}$. The hyperbolic subgroup $\mathbb{D}^{(1)}_0 \cong (\mathbb{R}, +)$ is a **non-compact** one-parameter group, and $\pi_0(\mathbb{D}^{(1)}) = \mathbb{Z}/2$, $\pi_1(\mathbb{D}^{(1)}) = 0$.

**Proof.** $N(A) = 1$ is the hyperbola $a^2 - a'^2 = 1$ with the two branches $a = \pm\sqrt{1+a'^2} > 0$ or $< 0$; the branch $a>0$ is parametrised bijectively by $a' = \sinh t$, $a = \cosh t$, and equals $\{e^{jt}\}$ by the closed form of the exponential. The branch $a<0$ is its negative. The parametrisation $t\mapsto e^{jt}$ is a group isomorphism onto the first branch because $e^{jt}e^{js} = e^{j(t+s)}$, and $\mathbb{R}$ is non-compact and contractible.

**Corollary (the decomposition of the unit group).** Combining the component count with the hyperbolic subgroup,

$$
\mathbb{D}^\times \;\cong\; \mathbb{R}_{>0}\times\mathbb{R}_{>0}\times(\mathbb{Z}/2)^2 \;\cong\; (\mathbb{D}^\times)_0 \times (\mathbb{Z}/2)^2,
$$

with $(\mathbb{D}^\times)_0 \cong \mathbb{R}^2$ the identity component. The unit group is non-compact, has four components, each simply connected, so $\pi_0(\mathbb{D}^\times) = (\mathbb{Z}/2)^2$ and $\pi_1(\mathbb{D}^\times) = 0$.

## One-Parameter Subgroups and the Geometry Slot

**Proposition (the one-parameter subgroups).** Every one-parameter subgroup of $\mathbb{D}^\times$ is of the form

$$
t \longmapsto \exp(tA), \qquad A \in \mathbb{D},
$$

and the infinitesimal generator $A$ is recovered as $\phi'(0)$. Explicitly, for $A = a + j a'$,

$$
\exp(tA) = e^{a t}\bigl(\cosh(a' t) + j\sinh(a' t)\bigr),
$$

so the one-parameter subgroups are the exponentials of the straight lines through the origin of the abelian Lie algebra; as unparametrised subgroups they are indexed by the directions $\mathbb{R}A$ in $\mathbb{D}$, a real projective line.

**Proof.** A one-parameter subgroup is a continuous homomorphism $\phi : (\mathbb{R},+)\to\mathbb{D}^\times$; being differentiable by continuity, it has an infinitesimal generator $A = \phi'(0)\in\operatorname{Lie}(\mathbb{D}^\times) = \mathbb{D}$, and the standard Lie-theoretic argument gives $\phi(t) = \exp(tA)$. Because $\exp$ is injective on $\mathbb{D}$, the image $\exp(\mathbb{R}A)$ determines the line $\mathbb{R}A$, while replacing $A$ by a nonzero scalar multiple reparametrises the same image; hence the homomorphism determines $A$ uniquely and the subgroup determines the direction. The displayed formula is the closed form applied to $tA = a t + a' t j$.

**The geometry slot.** The parameter $A = j$ generates the hyperbolic rotation subgroup

$$
t \longmapsto e^{jt} = \cosh t + j\sinh t,
$$

the group of **hyperbolic rotations** of the split-complex plane, which preserves the norm: $N(e^{jt}A) = N(A)$. This is the one-parameter group of the geometry; its action is the linear map $\begin{pmatrix} \cosh t & \sinh t \\ \sinh t & \cosh t \end{pmatrix}$ on coordinates, the group $SO^+(1,1)$, and it is non-compact because the hyperbolic angle is unbounded. The parameters $A = 1$ and $A = j$ are independent, and $\{e^{t}\}$ is the scaling subgroup $A\mapsto e^t A$, so every one-parameter subgroup is a combination of a hyperbolic rotation and a scaling. The hyperbolic rotations are developed as the geometry of the algebra in *Hyperbolic Rotations*.

## Comparison with the Complex and Biquaternion Cases

The three algebras have the same dimension statement over $\mathbb{R}$ only in the first two, and the Lie theory separates them by the shape of their unit groups. The complex field $\mathbb{C}$ is the definite analogue: $\mathbb{C}^\times = \mathbb{C}\setminus\{0\}$ is connected, its unit-norm group is the compact circle $U(1) = S^1$ with $\pi_1 = \mathbb{Z}$, and $\exp : \mathbb{C}\to\mathbb{C}^\times$ is surjective with kernel $2\pi i\mathbb{Z}$. The biquaternion algebra $\mathbb{B}$ is the noncommutative, four-complex-dimensional analogue: $\mathbb{B}^\times\cong GL(2,\mathbb{C})$, connected, with $\exp$ surjective and kernel the $2\pi i$-lattice, and the norm-one group $SL(2,\mathbb{C})$ is non-compact and non-abelian. The split-complex algebra sits at the commutative and definite-sign-changed corner.

| feature | $\mathbb{C}$ | $\mathbb{D}$ | $\mathbb{B}$ |
|---|---|---|---|
| Lie algebra | $(\mathbb{C}, 0)$, dim $2$ real | $(\mathbb{D}, 0)$, dim $2$ real | $\mathrm{GL}(2,\mathbb{C})$, dim $4$ complex |
| unit group | $\mathbb{C}^\times$, connected | $\mathbb{D}^\times\cong(\mathbb{R}^\times)^2$, four components | $GL(2,\mathbb{C})$, connected |
| norm-one subgroup | $U(1) = S^1$, compact | $\mathbb{D}^{(1)}\cong\mathbb{Z}/2\times\mathbb{R}$, non-compact | $SL(2,\mathbb{C})$, non-compact |
| identity component of the units | $\mathbb{C}$ | $\{a>\lvert a'\rvert\}$ | $GL(2,\mathbb{C})$ |
| $\exp$ surjective? | yes | no (image = identity component) | yes |
| $\exp$ injective? | no (kernel $2\pi i\mathbb{Z}$) | yes | no |
| component count of units | $1$ | $4$ | $1$ |
| abelian? | yes | yes | no |

The two systematic differences from $\mathbb{C}$ are that the norm is indefinite, which cuts the unit group into four components, and that the exponential is injective on a commutative algebra, so that it reaches only one of them. The systematic difference from $\mathbb{B}$ is commutativity: it makes the bracket zero, the exponential a group isomorphism onto the identity component, and the whole Lie theory elementary.

## Summary

The split-complex algebra is the abelian real Lie algebra of dimension $2$: its commutator bracket vanishes, and in the idempotent basis it is the direct sum of the two one-dimensional abelian Lie algebras $\mathbb{R}\Pi_1$ and $\mathbb{R}\Pi_2$. The exponential has the closed forms $\exp(A_+\Pi_1 + A_-\Pi_2) = e^{A_+}\Pi_1 + e^{A_-}\Pi_2$ and $\exp(a+ja') = e^a(\cosh a' + j\sinh a')$, has positive norm $N(\exp A) = e^{2a} > 0$, is injective, and is a diffeomorphism of $\mathbb{D}$ onto the identity component $(\mathbb{D}^\times)_0 = \{a > \lvert a'\rvert\}$ of the unit group, with an explicit inverse. It is a group isomorphism $(\mathbb{D}, +)\to((\mathbb{D}^\times)_0,\cdot)$.

The group of units is $\mathbb{D}^\times\cong\mathbb{R}^\times\times\mathbb{R}^\times$, a non-compact abelian Lie group of dimension $2$ with four components, given by the four sign choices of the idempotent coordinates; each component is contractible, so $\pi_0(\mathbb{D}^\times) = (\mathbb{Z}/2)^2$ and $\pi_1(\mathbb{D}^\times) = 0$. The polar parametrisation writes every unit as $A = \rho u$ with modulus $\rho = \sqrt{\lvert N(A)\rvert}$ and direction $u$ of unit modulus, in two regimes according to the sign of the norm. The unit-norm group is $\mathbb{D}^{(1)}\cong\mathbb{Z}/2\times\mathbb{R}$, with non-compact hyperbolic subgroup $\{e^{jt}\}\cong(\mathbb{R},+)$, the group of hyperbolic rotations of the geometry slot and the group $SO^+(1,1)$; every one-parameter subgroup is an exponential $\exp(tw)$ of a line in the Lie algebra. The comparison with $\mathbb{C}$ isolates the indefinite sign and the four components, and the comparison with $\mathbb{B}$ isolates commutativity, which makes the exponential injective onto a single component.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}$ | Split complex algebra, abelian Lie algebra of dimension $2$ |
| $A = a + ja'$ | General split complex number |
| $[A,B] = AB - BA$ | Commutator; identically zero |
| $N(A) = a^2 - a'^2$ | Norm |
| $\Pi_\pm = \tfrac12(1\pm j)$ | Idempotents, basis of the abelian decomposition |
| $A_\pm = a\pm a'$ | Idempotent coordinates |
| $\exp(A)$ | Exponential; $= e^{A_+}\Pi_1 + e^{A_-}\Pi_2$ |
| $\mathbb{D}^\times = \{N\neq 0\}$ | Group of units, $(\mathbb{R}^\times)^2$-shaped |
| $(\mathbb{D}^\times)_0 = \{a>\lvert a'\rvert\}$ | Identity component, image of $\exp$ |
| $\mathbb{D}^{(1)} = \{N = 1\}$ | Unit-norm group $\cong\mathbb{Z}/2\times\mathbb{R}$ |
| $\mathbb{D}^{(1)}_0 = \{e^{jt}\}$ | Hyperbolic subgroup $\cong(\mathbb{R},+)$ |
| $\rho(A) = \sqrt{\lvert N(A)\rvert}$ | Modulus |
| $u = A/\rho(A)$ | Direction, of unit modulus |
| $e^{jt} = \cosh t + j\sinh t$ | Hyperbolic rotation |
| $\pi_0, \pi_1$ | Components and fundamental group |
| $\mathrm{GL}(2,\mathbb{C})$, $SO^+(1,1)$ | Lie algebra of $\mathbb{B}^\times$ in the comparison table; rotation group of the geometry slot |

## Further Reading

- John Stillwell, *Naive Lie Theory* (Springer, Undergraduate Texts in Mathematics, 2008), for the Lie theory of low-dimensional abelian and matrix groups, and for $SO(1,1)$.
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations* (Springer, Graduate Texts in Mathematics 222, 2nd ed. 2015), for the exponential map, one-parameter subgroups and the Lie correspondence.
- Wulf Rossmann, *Lie Groups: An Introduction Through Linear Groups* (Oxford University Press, 2002), for the abelian case and the topology of matrix Lie groups.
- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the hyperbolic rotation group of the split complex plane.
- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for the exponential in a finite-dimensional real algebra and the group of units.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the split complex algebra and its unit group.
