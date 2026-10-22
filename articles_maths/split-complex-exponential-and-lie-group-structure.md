
# __Split-Complex Exponential and Lie Group Structure__

## Introduction

This article develops the Lie theory of the split-complex algebra $\mathbb{D} = \mathbb{R}[x]/(x^2-1)$. The algebra article defined $\mathbb{D}$ with basis $1$, $j$, $j^2 = +1$; the norm article identified the units $\mathbb{D}^\times$ with the elements of nonzero norm $\langle Q\rangle_{*} = q^2-q'^2$; and the idempotent article supplied the decomposition $\mathbb{D}\cong\mathbb{R}\oplus\mathbb{R}$. Here these are assembled into the standard theory of $\mathbb{D}^\times$ as a Lie group, of $\mathbb{D}$ as its abelian Lie algebra, and of the exponential map. It is the two-dimensional counterpart of the Lie theory of the higher members of the family, and every statement is a special case of the elementary Lie theory of $\mathbb{R}^\times$ and its square.

The one point that governs everything below is that $\mathbb{D}$ is **commutative**. Its commutator bracket vanishes, so it is an abelian Lie algebra; the exponential of a sum is the product of the exponentials; and the exponential map is a local diffeomorphism everywhere but is injective, unlike the matrix case. The price is a small unit group: $\mathbb{D}^\times$ has **four components** rather than being connected, and the exponential reaches only the identity component. The article states this geometry exactly.

The article owns the abelian Lie algebra structure of $\mathbb{D}$, the exponential and its closed forms in the two bases, the group of units and its exponential parametrisation, the four components, the non-compact hyperbolic subgroup, the one-parameter subgroups of the geometry slot, and the comparison with $\mathbb{C}$. It assumes the norm and invertibility theory of *Split-Complex Norm and Invertibility*, the idempotents of *Split-Complex Idempotents and Projections*, and the exponential parametrisation of the units; the hyperbolic one-parameter group is the subject of *Hyperbolic Rotations*, and the automorphisms and derivations are treated in *Split-Complex Automorphisms and Derivations*.

**Conventions.** $Q = q+jq'$, $q,q'\in\mathbb{R}$; conjugate $\bar Q = q-jq'$; idempotents $\Pi_\pm = \tfrac12(1\pm j)$; idempotent coordinates $Q_\pm = q\pm q'$, with $Q = Q_+\Pi_+ + Q_-\Pi_-$; norm $\langle Q\rangle_{*} = Q\bar Q = q^2-q'^2$; group of units $\mathbb{D}^\times = \{Q : \langle Q\rangle_{*}\neq 0\}$; unit-norm set $\mathbb{D}^{(1)} = \{Q : \langle Q\rangle_{*} = 1\}$. The identity component of a group $G$ is written $G_0$.

## The Algebra as an Abelian Lie Algebra

**Definition.** The **commutator bracket** on $\mathbb{D}$ is

$$
[Q,B] = QB - BQ, \qquad Q, B \in \mathbb{D}.
$$

**Proposition.** The bracket is identically zero, and $(\mathbb{D}, [\ ,\ ])$ is the abelian real Lie algebra of dimension $2$.

**Proof.** $\mathbb{D}$ is commutative, so $QB = BQ$ for all $Q,B$ and every bracket vanishes. A Lie algebra with zero bracket is abelian, and the underlying real vector space is two-dimensional.

**Remark.** The bracket rules out every phenomenon that depends on noncommutativity: there are no nontrivial inner derivations, no Baker–Campbell–Hausdorff correction, no Ad-action distinct from the identity, and no $\mathrm{SL}$-summand. In the idempotent basis the Lie algebra is the direct sum of two one-dimensional abelian Lie algebras, $\mathbb{D} = \mathrm{I}_+ \oplus \mathrm{I}_-$ with $\mathrm{I}_\pm = \mathbb{R}\Pi_\pm$, and every subspace is an abelian ideal.

## The Exponential: Series and Closed Form

**Definition.** The **exponential** of $Q \in \mathbb{D}$ is the sum of the absolutely convergent series

$$
\exp(Q) = \sum_{n=0}^{\infty} \frac{Q^n}{n!},
$$

convergent in the Euclidean topology of $\mathbb{D}\cong\mathbb{R}^2$.

**Theorem (closed form).** For $Q = Q_+\Pi_+ + Q_-\Pi_-$ and for $Q = q+jq'$,

$$
\exp(Q) = \exp(Q_+) \Pi_+ + \exp(Q_-) \Pi_-, \qquad \exp(q+jq') = \exp(q)\bigl(\cosh q' + j \sinh q'\bigr) = \exp(q)\cosh q' + \exp(q)\sinh q'\, j .
$$

**Proof.** The idempotents satisfy $\Pi_\pm^2 = \Pi_\pm$ and $\Pi_+\Pi_- = 0$, so for $n \geq 0$

$$
Q^n = (Q_+\Pi_+ + Q_-\Pi_-)^n = Q_+^n \Pi_+ + Q_-^n \Pi_-,
$$

and summing the two geometric pieces gives $\exp(Q) = \bigl(\sum_n Q_+^n/n!\bigr)\Pi_+ + \bigl(\sum_n Q_-^n/n!\bigr)\Pi_- = \exp(Q_+)\Pi_+ + \exp(Q_-)\Pi_-$. For the second form, substitute $Q_+ = q+q'$, $Q_- = q-q'$ and rewrite in the basis $\{1, j\}$:

$$
\exp(q+q')\Pi_+ + \exp(q-q')\Pi_- = \exp(q)\bigl(\exp(q')\Pi_+ + \exp(-q')\Pi_-\bigr) = \exp(q)\bigl(\cosh q'\,(\Pi_+ + \Pi_-) + \sinh q'\,(\Pi_+ - \Pi_-)\bigr) = \exp(q)\bigl(\cosh q' + j\sinh q'\bigr),
$$

since $\Pi_+ + \Pi_- = 1$ and $\Pi_+ - \Pi_- = j$.

**Corollary (the norm of an exponential is positive).** For every $Q$,

$$
\langle \exp(Q)\rangle_{*} = \exp(Q_+)\exp(Q_-) = \exp(Q_+ + Q_-) = \exp(2q) > 0 .
$$

So $\exp(\mathbb{D})$ lies in the component of positive norm, and in particular $\exp$ never produces a zero divisor. This is the elementary statement, in the group, that $\exp$ takes values in $\mathbb{D}^\times$ with $\langle Q\rangle_{*}>0$.

## The Group of Units

**Definition.** The **group of units** of $\mathbb{D}$ is $\mathbb{D}^\times = \{Q \in \mathbb{D} : \langle Q\rangle_{*}\neq 0\}$, with the multiplication of the algebra.

**Theorem.** The idempotent-coordinate map is an isomorphism of groups

$$
\mathbb{D}^\times \;\cong\; \mathbb{R}^\times \times \mathbb{R}^\times, \qquad Q \longmapsto (Q_+, Q_-),
$$

and consequently $\mathbb{D}^\times$ is an abelian real Lie group of dimension $2$, non-compact, with four connected components.

**Proof.** In the idempotent basis multiplication is componentwise, $(QB)_\pm = Q_\pm B_\pm$, and $Q$ is a unit iff $Q_+ Q_- = \langle Q\rangle_{*} \neq 0$ iff both $Q_+ \neq 0$ and $Q_- \neq 0$. The map to $\mathbb{R}^\times \times \mathbb{R}^\times$ is therefore a group isomorphism onto its image, which is all of $\mathbb{R}^\times\times\mathbb{R}^\times$. Each factor $\mathbb{R}^\times$ is a one-dimensional Lie group with two components, so the product has dimension $2$ and $2\times 2 = 4$ components; it is non-compact because $\mathbb{R}^\times$ is.

**Corollary (component count).** The four components are the products of the two signs of the idempotent coordinates,

$$
(\mathbb{D}^\times)_{(\varepsilon_+,\varepsilon_-)} = \{Q : \varepsilon_+ Q_+ > 0, \ \varepsilon_- Q_- > 0\}, \qquad \varepsilon_\pm \in \{\pm 1\},
$$

so $\pi_0(\mathbb{D}^\times) \cong (\mathbb{Z}/2)^2$. Each component is an open quadrant in the $(Q_+, Q_-)$ coordinates, hence contractible and diffeomorphic to $\mathbb{R}^2$; in particular every component is simply connected, and the identity component is

$$
(\mathbb{D}^\times)_0 = \{Q : Q_+ > 0, \ Q_- > 0\} = \{q > \lvert q'\rvert\} = \{\langle Q\rangle_{*} > 0, \ q > 0\},
$$

the open cone of positive norm pointing along the real axis.

## The Exponential Map: Image and Kernel

**Theorem (the exponential is a diffeomorphism onto the identity component).** The exponential restricts to a diffeomorphism of smooth manifolds

$$
\exp : \mathbb{D} \longrightarrow (\mathbb{D}^\times)_0, \qquad (q,q') \longmapsto \bigl(\exp(q)\cosh q', \ \exp(q)\sinh q'\bigr),
$$

whose inverse is

$$
\exp^{-1}(q + jq') = \tfrac12 \ln(q^2 - q'^2) + \operatorname{artanh}\!\Bigl(\frac{q'}{q}\Bigr) j, \qquad q > \lvert q'\rvert .
$$

**Proof.** On the identity component $q > \lvert q'\rvert$ one has $q^2 - q'^2 > 0$ and $\lvert q'/q\rvert < 1$, so the stated inverse is defined and smooth. Composing the two maps in either order returns the argument, using $\cosh^2 q' - \sinh^2 q' = 1$ and the addition formulas for $\cosh$ and $\sinh$; hence both are bijections and, being smooth with smooth inverse, diffeomorphisms.

**Corollary (the exponential is injective, and not surjective).** If $\exp(Q) = 1$ then $\exp(Q_+) = \exp(Q_-) = 1$, and since the real exponential is injective this gives $Q_+ = Q_- = 0$, so $Q = 0$: the kernel of $\exp$ is trivial. The image is the identity component only, so $\exp$ is not surjective onto $\mathbb{D}^\times$ and misses the three components of negative $Q_+$ or negative $Q_-$.

**Remark (the group law).** Because the algebra is abelian, the exponential satisfies $\exp(Q)\exp(B) = \exp(Q+B)$ for all $Q, B$, with no correction term; equivalently $\exp$ is a group isomorphism $(\mathbb{D}, +) \to ((\mathbb{D}^\times)_0, \cdot)$. The identity component is therefore an exponential group, and the whole unit group is its product with the finite group $(\mathbb{Z}/2)^2$ of components, $\mathbb{D}^\times \cong (\mathbb{D}^\times)_0 \times (\mathbb{Z}/2)^2$.

**Remark (the Lie correspondence).** Since $\exp : \mathbb{D}\to(\mathbb{D}^\times)_0$ is a diffeomorphism and a group isomorphism, the Lie functor recovers the algebra. The Lie algebra of the unit group is $\operatorname{Lie}(\mathbb{D}^\times) = \mathbb{D}$ with the zero bracket, and $\exp$ is the exponential map of the Lie group. This is the two-dimensional quantity that the algebra contributes to the Lie picture, in place of the vanishing derivation space of *Split-Complex Automorphisms and Derivations*.

## The Exponential Parametrisation

**Definition.** The **modulus** of $Q\in\mathbb{D}^\times$ is $\rho(Q) = \sqrt{\lvert \langle Q\rangle_{*}\rvert} > 0$, and the **direction** is $u(Q) = Q/\rho(Q)$, an element of the unit-modulus set

$$
\mathbb{D}^{(\pm 1)} = \{u : \lvert \langle u\rangle_{*}\rvert = 1\} = \mathbb{D}^{(1)} \cup (-\mathbb{D}^{(1)}), \qquad \mathbb{D}^{(1)} = \{u : \langle u\rangle_{*} = 1\}.
$$

**Theorem (exponential parametrisation of the units).** Every unit factors uniquely as

$$
Q = \rho\, u, \qquad \rho = \sqrt{\lvert \langle Q\rangle_{*}\rvert} > 0, \quad \lvert \langle u\rangle_{*}\rvert = 1,
$$

and the direction takes one of four branch forms, according to the component of $Q$:

$$
u = \pm\, \exp(j\theta) \ (\text{if } \langle Q\rangle_{*} > 0), \qquad u = \pm\, j\, \exp(j\theta) \ (\text{if } \langle Q\rangle_{*} < 0), \qquad \theta \in \mathbb{R},
$$

so that

$$
Q = \pm\, \sqrt{\langle Q\rangle_{*}}\; \exp(j\theta) \ (\langle Q\rangle_{*} > 0), \qquad Q = \pm\, \sqrt{-\langle Q\rangle_{*}}\; j\, \exp(j\theta) \ (\langle Q\rangle_{*} < 0).
$$

**Proof.** Set $\rho = \sqrt{\lvert \langle Q\rangle_{*}\rvert}$, which is positive for a unit, and $u = Q/\rho$, so that $\langle u\rangle_{*} = \langle Q\rangle_{*}/\rho^2 = \pm 1$, giving $\lvert \langle u\rangle_{*}\rvert = 1$ and the uniqueness of the factorisation. If $\langle Q\rangle_{*} > 0$ then $\langle u\rangle_{*} = 1$, and $\lvert q\rvert > \lvert q'\rvert$; on the branch $q > 0$ write $q/\rho = \cosh\theta$, $q'/\rho = \sinh\theta$ for the unique $\theta\in\mathbb{R}$ with $\operatorname{sgn}\theta = \operatorname{sgn} q'$, and then $u = \cosh\theta + j\sinh\theta = \exp(j\theta)$; the branch $q<0$ gives the sign $-$. If $\langle Q\rangle_{*} < 0$ then $\langle u\rangle_{*} = -1$ and $\lvert q'\rvert > \lvert q\rvert$; write $q'/\rho = \pm\cosh\theta$, $q/\rho = \sinh\theta$, giving $u = \sinh\theta + j\cosh\theta = j \exp(j\theta)$ up to the sign. The four cases are exactly the four components.

**Remark (two regimes).** The polar parametrisation has two regimes, hyperbolic-rotation-like on the components $\langle Q\rangle_{*} > 0$ and hyperbolic-translation-like on the components $\langle Q\rangle_{*} < 0$; the modulus is $\sqrt{\lvert \langle Q\rangle_{*}\rvert}$ and the angle is $\operatorname{artanh}(q'/q)$ in the first regime and $\operatorname{arcoth}$-like in the second. The present article records only the group factorisation $\mathbb{D}^\times \cong \mathbb{R}_{>0}\times \mathbb{D}^{(\pm 1)}$ that the parametrisation supplies.

## The Unit-Norm Group and the Hyperbolic Subgroup

**Definition.** The **unit-norm group** is $\mathbb{D}^{(1)} = \{Q : \langle Q\rangle_{*} = 1\}$, and the **hyperbolic subgroup** is its identity component

$$
\mathbb{D}^{(1)}_0 = \{Q : \langle Q\rangle_{*} = 1, \ q > 0\} = \{\exp(jt) : t\in\mathbb{R}\}, \qquad \exp(jt) = \cosh t + j\sinh t .
$$

**Theorem.** The unit-norm group is the abelian Lie group

$$
\mathbb{D}^{(1)} \;\cong\; \mathbb{Z}/2 \times \mathbb{R} \;\cong\; \{\pm 1\}\times\{\exp(jt)\},
$$

with two connected components $\mathbb{D}^{(1)}_0 = \{\exp(jt)\}$ and $-\mathbb{D}^{(1)}_0 = \{-\exp(jt)\}$. The hyperbolic subgroup $\mathbb{D}^{(1)}_0 \cong (\mathbb{R}, +)$ is a **non-compact** one-parameter group, and $\pi_0(\mathbb{D}^{(1)}) = \mathbb{Z}/2$, $\pi_1(\mathbb{D}^{(1)}) = 0$.

**Proof.** $\langle Q\rangle_{*} = 1$ is the hyperbola $q^2 - q'^2 = 1$ with the two branches $q = \pm\sqrt{1+q'^2} > 0$ or $< 0$; the branch $q>0$ is parametrised bijectively by $q' = \sinh t$, $q = \cosh t$, and equals $\{\exp(jt)\}$ by the closed form of the exponential. The branch $q<0$ is its negative. The parametrisation $t\mapsto \exp(jt)$ is a group isomorphism onto the first branch because $\exp(jt)\exp(js) = \exp(j(t+s))$, and $\mathbb{R}$ is non-compact and contractible.

**Corollary (the decomposition of the unit group).** Combining the component count with the hyperbolic subgroup,

$$
\mathbb{D}^\times \;\cong\; \mathbb{R}_{>0}\times\mathbb{R}_{>0}\times(\mathbb{Z}/2)^2 \;\cong\; (\mathbb{D}^\times)_0 \times (\mathbb{Z}/2)^2,
$$

with $(\mathbb{D}^\times)_0 \cong \mathbb{R}^2$ the identity component. The unit group is non-compact, has four components, each simply connected, so $\pi_0(\mathbb{D}^\times) = (\mathbb{Z}/2)^2$ and $\pi_1(\mathbb{D}^\times) = 0$.

## One-Parameter Subgroups and the Geometry Slot

**Proposition (the one-parameter subgroups).** Every one-parameter subgroup of $\mathbb{D}^\times$ is of the form

$$
t \longmapsto \exp(tQ), \qquad Q \in \mathbb{D},
$$

and the infinitesimal generator $Q$ is recovered as $\phi'(0)$. Explicitly, for $Q = q + j q'$,

$$
\exp(tQ) = \exp(q t)\bigl(\cosh(q' t) + j\sinh(q' t)\bigr),
$$

so the one-parameter subgroups are the exponentials of the straight lines through the origin of the abelian Lie algebra; as unparametrised subgroups they are indexed by the directions $\mathbb{R}Q$ in $\mathbb{D}$, a real projective line.

**Proof.** A one-parameter subgroup is a continuous homomorphism $\phi : (\mathbb{R},+)\to\mathbb{D}^\times$; being differentiable by continuity, it has an infinitesimal generator $Q = \phi'(0)\in\operatorname{Lie}(\mathbb{D}^\times) = \mathbb{D}$, and the standard Lie-theoretic argument gives $\phi(t) = \exp(tQ)$. Because $\exp$ is injective on $\mathbb{D}$, the image $\exp(\mathbb{R}Q)$ determines the line $\mathbb{R}Q$, while replacing $Q$ by a nonzero scalar multiple reparametrises the same image; hence the homomorphism determines $Q$ uniquely and the subgroup determines the direction. The displayed formula is the closed form applied to $tQ = q t + q' t j$.

**The geometry slot.** The parameter $Q = j$ generates the hyperbolic rotation subgroup

$$
t \longmapsto \exp(jt) = \cosh t + j\sinh t,
$$

the group of **hyperbolic rotations** of the split-complex plane, which preserves the norm: $\langle \exp(jt)Q\rangle_{*} = \langle Q\rangle_{*}$. This is the one-parameter group of the geometry; its action is the linear map $\begin{pmatrix} \cosh t & \sinh t \\ \sinh t & \cosh t \end{pmatrix}$ on coordinates, the group $SO^+(1,1)$, and it is non-compact because the hyperbolic angle is unbounded. The parameters $Q = 1$ and $Q = j$ are independent, and $\{\exp(t)\}$ is the scaling subgroup $Q\mapsto \exp(t) Q$, so every one-parameter subgroup is a combination of a hyperbolic rotation and a scaling. The hyperbolic rotations are developed as the geometry of the algebra in *Hyperbolic Rotations*.

## Summary

The split-complex algebra is the abelian real Lie algebra of dimension $2$: its commutator bracket vanishes, and in the idempotent basis it is the direct sum of the two one-dimensional abelian Lie algebras $\mathbb{R}\Pi_+$ and $\mathbb{R}\Pi_-$. The exponential has the closed forms $\exp(Q_+\Pi_+ + Q_-\Pi_-) = \exp(Q_+)\Pi_+ + \exp(Q_-)\Pi_-$ and $\exp(q+jq') = \exp(q)(\cosh q' + j\sinh q')$, has positive norm $\langle \exp Q\rangle_{*} = \exp(2q) > 0$, is injective, and is a diffeomorphism of $\mathbb{D}$ onto the identity component $(\mathbb{D}^\times)_0 = \{q > \lvert q'\rvert\}$ of the unit group, with an explicit inverse. It is a group isomorphism $(\mathbb{D}, +)\to((\mathbb{D}^\times)_0,\cdot)$.

The group of units is $\mathbb{D}^\times\cong\mathbb{R}^\times\times\mathbb{R}^\times$, a non-compact abelian Lie group of dimension $2$ with four components, given by the four sign choices of the idempotent coordinates; each component is contractible, so $\pi_0(\mathbb{D}^\times) = (\mathbb{Z}/2)^2$ and $\pi_1(\mathbb{D}^\times) = 0$. The polar parametrisation writes every unit as $Q = \rho u$ with modulus $\rho = \sqrt{\lvert \langle Q\rangle_{*}\rvert}$ and direction $u$ of unit modulus, in two regimes according to the sign of the norm. The unit-norm group is $\mathbb{D}^{(1)}\cong\mathbb{Z}/2\times\mathbb{R}$, with non-compact hyperbolic subgroup $\{\exp(jt)\}\cong(\mathbb{R},+)$, the group of hyperbolic rotations of the geometry slot and the group $SO^+(1,1)$; every one-parameter subgroup is an exponential $\exp(tw)$ of a line in the Lie algebra. The comparison with $\mathbb{C}$ isolates the indefinite sign and the four components.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}$ | Split complex algebra, abelian Lie algebra of dimension $2$ |
| $Q = q + jq'$ | General split complex number |
| $[Q,B] = QB - BQ$ | Commutator; identically zero |
| $\langle Q\rangle_{*} = q^2 - q'^2$ | Norm |
| $\Pi_\pm = \tfrac12(1\pm j)$ | Idempotents, basis of the abelian decomposition |
| $Q_\pm = q\pm q'$ | Idempotent coordinates |
| $\exp(Q)$ | Exponential; $= \exp(Q_+)\Pi_+ + \exp(Q_-)\Pi_-$ |
| $\mathbb{D}^\times = \{\langle Q\rangle_{*}\neq 0\}$ | Group of units, $(\mathbb{R}^\times)^2$-shaped |
| $(\mathbb{D}^\times)_0 = \{q>\lvert q'\rvert\}$ | Identity component, image of $\exp$ |
| $\mathbb{D}^{(1)} = \{\langle Q\rangle_{*} = 1\}$ | Unit-norm group $\cong\mathbb{Z}/2\times\mathbb{R}$ |
| $\mathbb{D}^{(1)}_0 = \{\exp(jt)\}$ | Hyperbolic subgroup $\cong(\mathbb{R},+)$ |
| $\rho(Q) = \sqrt{\lvert \langle Q\rangle_{*}\rvert}$ | Modulus |
| $u = Q/\rho(Q)$ | Direction, of unit modulus |
| $\exp(jt) = \cosh t + j\sinh t$ | Hyperbolic rotation |
| $\pi_0, \pi_1$ | Components and fundamental group |

## Further Reading

- John Stillwell, *Naive Lie Theory* (Springer, Undergraduate Texts in Mathematics, 2008), for the Lie theory of low-dimensional abelian and matrix groups, and for $SO(1,1)$.
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations* (Springer, Graduate Texts in Mathematics 222, 2nd ed. 2015), for the exponential map, one-parameter subgroups and the Lie correspondence.
- Wulf Rossmann, *Lie Groups: An Introduction Through Linear Groups* (Oxford University Press, 2002), for the abelian case and the topology of matrix Lie groups.
- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the hyperbolic rotation group of the split complex plane.
- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for the exponential in a finite-dimensional real algebra and the group of units.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the split complex algebra and its unit group.
