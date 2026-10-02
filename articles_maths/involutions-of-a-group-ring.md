
# __Involutions of a Group Ring__

## Introduction

The group ring $K[G]$ carries an involution built from two reversals, the inversion $g \mapsto g^{-1}$ of the group and an involution $\sigma$ of the coefficient ring $K$. The map

$$
\Bigl(\sum_g a_g\,g\Bigr)^{*} = \sum_g \sigma(a_g)\,g^{-1}
$$

is anti-multiplicative because the two reversals compensate: the inverse of a product is the product of the inverses in the opposite order, and $\sigma$ is anti-multiplicative. This **standard involution** is the one used throughout the representation theory of a finite group, and it is only the first of a family: any anti-automorphism of $G$ of order two, composed with $\sigma$ on the coefficients, gives an involution of $K[G]$, and the standard one is the case of inversion. When $G$ is abelian, inversion is an automorphism, so the standard involution is an automorphism of $K[G]$ and the distinction between the two kinds of involution disappears.

This article fixes the standard involution, derives the involutions induced by an anti-automorphism of the group, records the compatibility with the coefficients and the passage to a twisted group ring, and computes the symmetric and skew elements. It assumes *Rings* and *Involutive Rings* for the involution of a ring, *Groups* for the group and its anti-automorphisms, and *Group Algebras* for the group ring and its augmentation; the classification of all the involutions of $K[G]$ by a cocycle is stated in the form in which the twisted group ring carries it, and the applications to representation theory are not touched. Throughout, $G$ is a group, $K$ is a commutative ring with $1 \neq 0$ and $\sigma$ is an involution of $K$ (possibly the identity), $K[G]$ is the group ring, and $\varepsilon$ is its augmentation; the general element is $\sum_g a_g g$ with $a_g \in K$ and finite support.

## The Standard Involution

**Definition.** The **standard involution** of $K[G]$ is the map

$$
\Bigl(\sum_g a_g\,g\Bigr)^{*} = \sum_g \sigma(a_g)\,g^{-1},
$$

extended linearly.

**Theorem.** The standard involution is an involution of $K[G]$; it restricts to $\sigma$ on the copy of $K$ inside $K[G]$, and it commutes with the augmentation, $\varepsilon(x^{*}) = \varepsilon(x)$.

**Proof.** Additivity is entrywise, and $1^{*} = 1$ because $1 = 1\cdot e$ and $e^{-1} = e$. For the anti-multiplicativity, let $x = \sum_g a_g g$ and $y = \sum_h b_h h$; then $xy = \sum_{g,h} a_g b_h\,gh$ and

$$
(xy)^{*} = \sum_{g,h}\sigma(a_gb_h)\,(gh)^{-1} = \sum_{g,h}\sigma(b_h)\sigma(a_g)\,h^{-1}g^{-1} = y^{*}x^{*},
$$

using $(gh)^{-1} = h^{-1}g^{-1}$ and $\sigma(a_gb_h) = \sigma(b_h)\sigma(a_g)$; the reindexing of a finite-support sum is legitimate. The square is the identity because $(g^{-1})^{-1} = g$ and $\sigma^2 = \mathrm{id}$, and the restriction to $K$ is $\sigma$ because $g = e$ gives $a_e e \mapsto \sigma(a_e)e$. The augmentation of $x^{*}$ is the sum of the $\sigma(a_g)$ over those $g$ with $g^{-1}$ ranging over the support, which is the sum of the $a_g$ because $\sigma(1) = 1$ and $g \mapsto g^{-1}$ is a bijection of $G$.

**Corollary (the two cases of the group).** The standard involution is an automorphism of $K[G]$ exactly when inversion is an automorphism of $G$, that is, when $G$ is abelian; for a nonabelian $G$ it is a genuine anti-automorphism. In the abelian case $K[G]$ is commutative, and the standard involution is an automorphism of order dividing two whose fixed ring is the subring of the elements with $a_g = \sigma(a_{g^{-1}})$.

**Proof.** The standard involution reverses products, so it is multiplicative exactly when the product is commutative, and the computation $(gh)^{-1} = h^{-1}g^{-1}$ shows that inversion is an automorphism exactly when $gh = hg$ for all $g, h$. The fixed elements are those with $\sigma(a_g) = a_{g^{-1}}$ by comparison of coefficients.

## Involutions from an Anti-Automorphism of the Group

**Definition.** Let $\iota$ be an **anti-automorphism of $G$ of order two**, $\iota(gh) = \iota(h)\iota(g)$ and $\iota^2 = \mathrm{id}$. The involution of $K[G]$ **induced by $\iota$** is

$$
\Bigl(\sum_g a_g\,g\Bigr)^{\iota} = \sum_g \sigma(a_g)\,\iota(g).
$$

**Proposition.** The map $x \mapsto x^{\iota}$ is an involution of $K[G]$, and the standard involution is the case $\iota(g) = g^{-1}$.

**Proof.** The same computation as for the standard involution, with $\iota(gh) = \iota(h)\iota(g)$ in place of $(gh)^{-1} = h^{-1}g^{-1}$, gives anti-multiplicativity; the order-two condition is $\iota^2 = \mathrm{id}$; additivity, the unit and the coefficient restriction are as before. Inversion is the anti-automorphism $g \mapsto g^{-1}$, which has order two and is an automorphism exactly when $G$ is abelian.

**Proposition (twisting by a cocycle).** Let $\iota$ be an anti-automorphism of $G$ of order two and let $u : G \to K^{\times}$ be a map with

$$
u_e = 1, \qquad u_{gh} = u_h\,u_g, \qquad u_g\,u_{\iota(g)} = 1 \quad \text{for all } g, h \in G .
$$

Then

$$
\Bigl(\sum_g a_g\,g\Bigr)^{*} = \sum_g \sigma(a_g)\,u_g\,\iota(g)
$$

is an involution of $K[G]$ restricting to $\sigma$ on the coefficients; the involution induced by $\iota$ is the case $u = 1$, and the standard involution is the case $u = 1$ and $\iota(g) = g^{-1}$.

**Proof.** Additivity and $1^{*} = 1$ are immediate, the restriction to $K$ is $\sigma$, and $\sigma^2 = \mathrm{id}$ with $\iota^2 = \mathrm{id}$ and $u_g u_{\iota(g)} = 1$ give $(x^{*})^{*} = x$. For the anti-multiplicativity, it suffices to check the products of group elements: $(g h)^{*} = \sigma(1)u_{gh}\iota(gh) = u_{gh}\iota(h)\iota(g)$, while $h^{*}g^{*} = u_h\iota(h)\,u_g\iota(g) = u_hu_g\,\iota(h)\iota(g)$, and the two agree by $u_{gh} = u_hu_g$ (the coefficients $u_g$ are central scalars). The case $u = 1$ is the involution induced by $\iota$.

**Remark.** The map $u$ is a **cocycle**, an anti-homomorphism of $G$ into the units of $K$ that is inverted by $\iota$; when $K^{\times}$ is abelian it is a homomorphism and its class in $H^1(G;K^{\times})$ is an invariant of the involution. That every involution of $K[G]$ that restricts to $\sigma$ on the coefficients arises from a pair $(\iota, u)$ as above is the classification theorem of Hertweck; it is quoted here, not used, and the family above is the part the article works with.

## The Twisted Group Ring

Let $\alpha : G \times G \to K^{\times}$ be a two-cocycle in the sense of group cohomology, and let $K^{\alpha}[G]$ be the **twisted group ring** with basis $\bar g$ and product

$$
\bar g\,\bar h = \alpha(g,h)\,\overline{gh}, \qquad \alpha(g,h)\alpha(gh,k) = \alpha(h,k)\alpha(g,hk).
$$

**Proposition.** The assignment $\bar g^{*} = \overline{g^{-1}}$ extends to an involution of $K^{\alpha}[G]$ with coefficient involution $\sigma$ if and only if

$$
\alpha(g,h) = \alpha(h^{-1},g^{-1}) \qquad \text{for all } g, h \in G .
$$

**Proof.** By linearity it suffices to check the products of basis elements. On the one hand $(\bar g\bar h)^{*} = \alpha(g,h)\,\overline{gh}^{*} = \alpha(g,h)\overline{(gh)^{-1}}$. On the other hand $\bar h^{*}\bar g^{*} = \overline{h^{-1}}\,\overline{g^{-1}} = \alpha(h^{-1},g^{-1})\overline{h^{-1}g^{-1}} = \alpha(h^{-1},g^{-1})\overline{(gh)^{-1}}$. The two agree for all $g, h$ exactly under the stated identity. The square is the identity because $\overline{g^{-1}}^{*} = \bar g$ and $\sigma^2 = \mathrm{id}$, and additivity and the unit are immediate.

**Corollary.** For the untwisted group ring, where $\alpha = 1$, the condition is automatic and the standard involution exists for every $G$; the twist obstructs the involution exactly by the difference between $\alpha(g,h)$ and $\alpha(h^{-1},g^{-1})$, and the obstruction vanishes when $\alpha$ is symmetric in this sense. The twisted group ring is the algebra of a projective representation of $G$ of cocycle $\alpha$, and the involution it carries is the one that makes that algebra involutive.

**Example (the rational group algebra of the quaternion group).** For $G = Q_8 = \{\pm 1, \pm i, \pm j, \pm k\}$ and $K = \mathbb{Q}$ with $\sigma = \mathrm{id}$, the standard involution sends $g$ to $g^{-1}$, which is $-g$ for the six elements $\pm i, \pm j, \pm k$ and fixes $\pm 1$. The group algebra decomposes as

$$
\mathbb{Q}[Q_8] \cong \mathbb{Q}^4 \times \mathbb{H}(\mathbb{Q}),
$$

with four one-dimensional factors and the quaternion algebra; under this decomposition the standard involution is the identity on the four copies of $\mathbb{Q}$ and the quaternion conjugation on $\mathbb{H}(\mathbb{Q})$, so its fixed part is $4+1 = 5$-dimensional, spanned by the four coordinate units together with the real line of the quaternion factor, and its skew part is the $3$-dimensional space of pure quaternions.

## Compatibility with the Coefficients

**Proposition.** An involution of $K[G]$ that restricts to the involution $\sigma$ of $K$ is determined by its values on the group elements: the ring is generated as a $K$-module by $G$, so the involution is fixed by $\sigma$ and by the images of the group elements. The involutions of the previous section are exactly those of the form $g^{*} = u_g\iota(g)$; that these exhaust the involutions restricting to $\sigma$ is Hertweck's theorem, quoted rather than proved here.

**Proof.** The generation statement is the definition of the group ring; the form of the involutions of the previous section is its construction, and the exhaustiveness is the deferred classification.

**Corollary (elements fixed by the standard involution).** For the standard involution the fixed elements are $\{x : a_g = \sigma(a_{g^{-1}})\ \text{for all}\ g\}$ and the skew elements are $\{x : a_g = -\sigma(a_{g^{-1}})\}$; both are additive subgroups, and they are the eigenspaces when $2$ is invertible in $K$. For a finite group the symmetric part is a $K^\sigma$-module of rank at least the number of conjugacy classes of $G$ that are stable under inversion.

**Proof.** The fixed-element condition is the comparison of coefficients in $x^{*} = x$; the eigenspace statement is the additive decomposition of *Involutive Rings*. The rank statement follows because a stable conjugacy class sum is fixed under $\sigma = \mathrm{id}$ and the class sums are linearly independent.

## Summary

The group ring $K[G]$ carries the **standard involution** $(\sum a_g g)^{*} = \sum \sigma(a_g)g^{-1}$, anti-multiplicative because the inversion of $G$ and the involution $\sigma$ of $K$ reverse in tandem, with $1^{*} = 1$ and $\varepsilon(x^{*}) = \varepsilon(x)$. It restricts to $\sigma$ on the coefficients, it is an automorphism exactly when $G$ is abelian, and its fixed elements are those with $a_g = \sigma(a_{g^{-1}})$. More generally an anti-automorphism $\iota$ of $G$ of order two gives the involution $(\sum a_g g)^{\iota} = \sum \sigma(a_g)\iota(g)$, and the standard involution is the case of inversion; every involution of $K[G]$ fixing the coefficients is of the form $g^{*} = u_g\iota(g)$ with $u$ a cocycle, the invariant of the involution being the class of $u$ in $H^2(G;K^{\times})$.

On a twisted group ring $K^{\alpha}[G]$, with $\bar g\bar h = \alpha(g,h)\overline{gh}$, the assignment $\bar g^{*} = \overline{g^{-1}}$ extends to an involution if and only if $\alpha(g,h) = \alpha(h^{-1},g^{-1})$, a condition automatic for the untwisted ring. The symmetric and skew elements are the eigenspaces of the standard involution, and for a finite group the symmetric part contains the inversion-stable class sums.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $G$, $K$, $\sigma$ | Group, commutative coefficient ring, involution of $K$ |
| $K[G]$ | Group ring; $\varepsilon$ its augmentation |
| $x^{*} = \sum \sigma(a_g)g^{-1}$ | Standard involution, from inversion |
| $x^{\iota} = \sum \sigma(a_g)\iota(g)$ | Involution induced by an anti-automorphism $\iota$ of order two |
| $g^{*} = u_g\iota(g)$ | General involution fixing the coefficients; $u$ a cocycle |
| $\alpha$, $K^{\alpha}[G]$ | Two-cocycle and twisted group ring; $\bar g\bar h = \alpha(g,h)\overline{gh}$ |
| $\alpha(g,h) = \alpha(h^{-1},g^{-1})$ | Existence of the involution on the twisted group ring |
| $a_g = \sigma(a_{g^{-1}})$ | Fixed elements of the standard involution |
| $\mathbb{Q}[Q_8] \cong \mathbb{Q}^4 \times \mathbb{H}(\mathbb{Q})$ | Example; conjugation on the quaternion factor |

## Further Reading

- Charles W. Curtis and Irving Reiner, *Representation Theory of Finite Groups and Associative Algebras* (Wiley, 1962), for group algebras, the augmentation and the standard involution.
- Gregory Karpilovsky, *The Jacobson Radical of Group Algebras* (North-Holland, 1987), for involutions of group rings and their fixed subrings.
- Martin Hertweck, "Involutions of group rings", *Proceedings of the American Mathematical Society* **134** (2006), for the classification of the involutions of $K[G]$ by an anti-automorphism and a cocycle.
- Donald S. Passman, *The Algebraic Structure of Group Rings* (Wiley, 1977), for the structure of group rings over a commutative ring and for twisted group rings.
