# __The Reduced Biquaternion Iterated Function Systems__

## Introduction

The reduced biquaternion algebra is the commutative algebra $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$ of basis $1,i,j,ij$, with element $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}=Q_{+}\Pi_++Q_{-}\Pi_-$ in the two central idempotents and with the topological norm $\langle \breve Q\rangle_{\mathrm{ts}*}=|Q_{\blacktriangle}|^{2}+|Q_{\blacktriangledown}|^{2}=\tfrac12(|Q_{+}|^{2}+|Q_{-}|^{2})$. An **iterated function system** of the algebra is a finite family of contractions of the algebra, and the article describes the geometry of those systems.

The algebra forces three simplifications and one structural fact. The simplifications: an affine map of the algebra is a pair of complex affine maps, one on each idempotent coordinate, because the two-sided maps $\breve Q\mapsto P\,\breve Q\,Q+R$ act diagonally and their linear parts are the pair of the two products $pq$ and $p'q'$ of the idempotent coordinates; the operator norm of the left multiplication is the larger of the two moduli, $\lVert L_{\breve Q}\rVert=\max(|Q_{+}|,|Q_{-}|)$, so that the contraction and similarity criteria are read from the two complex multipliers; and the square is invertible in the strongest sense, having four inverse branches generically and no element without a square root. The structural fact: a system of generators acts coordinatewise with the honest single index of the algebra, so the attractor is the matched set of the pairs coded by the same sequence of generators, a graph-like subset of the product of the two coordinate attractors, a picture developed in *The Idempotent Decomposition and the Split Fractal*.

The article owns the affine maps of the algebra, the contraction and similarity criteria, the similarity dimension, the existence and the shape of the attractor, the inverse branches of the square and the symmetries of a system. The operator norm and the multiplication operators are *The Multiplication Operators of the Algebra of the Reduced Biquaternions*; the group of units and the torus are *The Group of Units of the Algebra of the Reduced Biquaternions* and *The Unitary Group of the Reduced Biquaternion Algebra*; the zero-divisor cone that is the branching set of the square is *Zero Divisors of the Algebra of the Reduced Biquaternions*; the attractor structure is *The Idempotent Decomposition and the Split Fractal*; the quadratic map and its fractal are *The Reduced Biquaternion Quadratic Map and Its Julia Sets*; the dimension is *The Hausdorff Dimension of the Reduced Biquaternion Julia Sets*. The companion is *The Biquaternion Iterated Function Systems*.

## Affine Maps of the Algebra

**Proposition (every affine map is a pair of complex affine maps).** An $\mathbb{R}$-affine map of the algebra has the form $\breve Q\mapsto M(\breve Q)+R$ with $M$ real-linear, and if $M$ is one of the two-sided multiplication maps $\breve Q\mapsto P\,\breve Q\,Q$, then in the idempotent coordinates

$$
P\,\breve Q\,Q=\bigl(p\,q\,Q_{+}\bigr)\Pi_++\bigl(p'q'\,Q_{-}\bigr)\Pi_-,
$$

so that $M$ is the pair of the two complex scalars $pq$ and $p'q'$ acting on the two coordinates. Consequently every affine map that is built from the multiplications of the algebra is the pair of two complex affine maps

$$
(Q_{+},Q_{-})\longmapsto\bigl(\alpha Q_{+}+\rho,\;\beta Q_{-}+\sigma\bigr).
$$

**Proof.** The multiplication is componentwise, so $P\,\breve Q\,Q$ has coordinates $p\,q\,Q_{+}$ and $p'q'Q_{-}$ with $p,p'$ the coordinates of $P$ and $q,q'$ those of $Q$; adding the translation gives the displayed pair, with $\alpha=pq$, $\beta=p'q'$, $\rho$ and $\sigma$ the coordinates of $R$.

**Corollary (the collapse of the several kinds of affine map).** In the biquaternion algebra there are three distinct kinds of affine map — the left, the right and the two-sided — and they give three different families of fractals. Here the algebra is commutative, so the left and the right affine maps coincide, the two-sided maps are again pairs of complex affine maps, and there is a single notion of affine iterated function system, with the general linear part the pair $(\alpha,\beta)$.

**Proof.** Left multiplication by $P$ is $p\,q\,Q_{+}$ and $p'q'Q_{-}$ with $q=q'=1$, right multiplication is the same with $p=p'=1$, and the general two-sided map multiplies the two; commutativity makes the three formulas of the same shape.

**Remark (the affine group).** The invertible affine maps of the algebra are the semidirect product of the group of units acting diagonally and the translations, that is the semidirect product of $\mathbb{C}^{\times}\times\mathbb{C}^{\times}$ with $\mathbb{C}\oplus\mathbb{C}$; it is the affine group of the product of two complex lines, an abelian normal subgroup of translations and a diagonal linear part.

## Contractions and the Operator Norm

**Theorem (the operator norm).** For the left multiplication by an element $\breve Q$ on the algebra with the topological norm,

$$
\boxed{\;
\lVert L_{\breve Q}\rVert=\max(|Q_{+}|,|Q_{-}|)
\;},
$$

the maximum of the moduli of the two idempotent coordinates; in terms of the topological norm, $\max(|Q_{+}|,|Q_{-}|)^{2}\leq 2\langle\breve Q\rangle_{\mathrm{ts}*}$, with equality exactly when one of the two moduli vanishes, so that the operator norm is at most $\sqrt{2\langle\breve Q\rangle_{\mathrm{ts}*}}$ and equals $\sqrt{\langle\breve Q\rangle_{\mathrm{ts}*}}$ precisely when the two moduli coincide.

**Proof.** The operator is diagonal with the two entries $Q_{+}$ and $Q_{-}$ in the idempotent basis, and the norm of a diagonal operator for the norm $\tfrac12(|Q_{+}|^{2}+|Q_{-}|^{2})^{1/2}$ is the largest modulus of an entry; the comparison with $\langle\cdot\rangle_{\mathrm{ts}*}$ follows from $\max(|Q_{+}|,|Q_{-}|)^{2}\leq|Q_{+}|^{2}+|Q_{-}|^{2}\leq2\max(|Q_{+}|,|Q_{-}|)^{2}$, with equality in the first inequality exactly when one modulus vanishes and in the second exactly when $|Q_{+}|=|Q_{-}|$.

**Corollary (the contraction criterion).** An affine map with linear part the pair $(\alpha,\beta)$ is a contraction of the algebra exactly when $\max(|\alpha|,|\beta|)<1$; in particular the affine map with linear part the left multiplication by $\breve Q$ is a contraction exactly when both $|Q_{+}|<1$ and $|Q_{-}|<1$, that is exactly when $\breve Q$ lies in the open unit bidisc.

**Proof.** The Lipschitz ratio of the map is the operator norm of its linear part, which is the larger modulus of the two multipliers.

## Similarities and the Similarity Dimension

**Proposition (the similarity criterion).** The linear map with multipliers $(\alpha,\beta)$ is a similarity of the algebra exactly when $|\alpha|=|\beta|$, and then its ratio is $|\alpha|$. In particular the left multiplication by $\breve Q$ is a similarity exactly when $|Q_{+}|=|Q_{-}|$, and then its ratio is $|Q_{+}|$; the elements with $|Q_{+}|=|Q_{-}|$ include the central complex scalars and the purely hyperbolic multiples $t\,j$ with $t$ real.

**Proof.** A real-linear map of a Euclidean space is a similarity exactly when its two singular values coincide; the map is diagonal in the idempotent coordinates with entries $\alpha,\beta$, so its singular values are $|\alpha|$ and $|\beta|$. For the left multiplication by $\breve Q$ the entries are $Q_{+}$ and $Q_{-}$, and for $\breve Q=t\,j$ with $t$ real the coordinates are $Q_{+}=t$ and $Q_{-}=-t$, of equal modulus.

**Theorem (the similarity dimension).** Let the system have $m$ generators, each a similarity of the algebra of ratio $r_{i}<1$ with the same ratio in the two coordinates. Then the attractor is a self-similar set, and under the open set condition its Hausdorff dimension is the unique $s$ with

$$
\boxed{\;
\sum_{i=1}^{m}r_{i}^{s}=1
\;},
$$

the same equation as for each of the two coordinate systems.

**Proof.** Each generator is a similarity of ratio $r_{i}$ and the family is a self-similar system; the attractor satisfies the fixed point equation of the system, and the classical dimension formula for a self-similar set with the open set condition gives the equation. The two coordinate systems have the same ratios by hypothesis, so their dimensions solve the same equation.

**Remark (the self-affine case).** If the two multipliers of a generator have different moduli, the generator is not a similarity but a self-affine map, the attractor is a graph-directed or self-affine set rather than a self-similar one, and there is no single equation of the displayed form; the coordinates are then stretched by different factors and the dimension is that of a self-affine object. The reduced biquaternion algebra produces both cases, and the similarity case is the one in which the system comes from the units of equal modulus, the diagonal pairs.

## The Attractor

**Theorem (existence).** A finite system of contractions of the algebra has a unique non-empty compact attractor, and the attractor is the limit of the iterates of the Hutchinson operator on the space of compact sets with the Hausdorff metric.

**Proof.** The algebra with the topological norm is a complete metric space, and each contraction is a map of that space with ratio less than one; the Hutchinson operator is a contraction of the space of compact sets with ratio the largest ratio of the generators, hence has a unique fixed point by the contraction principle.

**Corollary (the shape).** The attractor is the set of the matched pairs, the image of the coding space under the pair of the two coding maps, a graph-like subset of the product of the two coordinate attractors, as stated and proved in *The Idempotent Decomposition and the Split Fractal*; for a system with one generator it is the pair of the two fixed points, which is the product of the two one-point attractors, and for the quadratic family the bounded orbit locus is the full product.

**Proof.** The statement is the theorem of the article on the split fractal.

## The Inverses and the Branches of the Square

**Theorem (the branches of the square).** The squaring map $\breve Q\mapsto \breve Q^{2}$ is surjective, and the solutions of $\breve Q^{2}=W$ with $W=w_{1}\Pi_++w_{2}\Pi_-$ are

$$
\boxed{\;
\breve Q=\pm\sqrt{w_{1}}\;\Pi_+\pm\sqrt{w_{2}}\;\Pi_-
\;},
$$

four of them when $w_{1}w_{2}\neq0$, two when exactly one coordinate is zero, and one when $W=0$. The branching set is the zero-divisor cone $\{w_{1}=0\}\cup\{w_{2}=0\}$.

**Proof.** The square is coordinatewise, so $\breve Q^{2}=W$ is the pair of the equations $Q_{+}^{2}=w_{1}$ and $Q_{-}^{2}=w_{2}$; each has two solutions in the complex field, one of them double when the value is zero, and none otherwise; the branching is at the values where a solution is multiple, which is the vanishing of a coordinate.

**Remark (no rootless element).** Every element of the reduced biquaternion algebra has a square root, of which four in the generic case, because the two complex equations are always solvable; the inverse branches of the square are therefore the four complex affine-in-the-radical maps with multipliers $1/(2Q_{+})$ and $1/(2Q_{-})$, and a branch is a similarity exactly when $|w_{1}|=|w_{2}|$. In the companion algebra the corresponding analysis has additional cases, and the branching and rootless phenomena there are among the reasons the fractal theory is harder.

## The Symmetries of a System

**Proposition (the equivariance of a system).** Let $g$ be an involution of the algebra. A system $\{f_{i}\}$ is conjugated by $g$ to the system $\{g\circ f_{i}\circ g\}$, with the same attractor image $g(\mathcal{K})$; if every $f_{i}$ commutes with $g$, then $g$ preserves the attractor. For the affine systems the involutions act on the multipliers by the corresponding sign changes.

**Proof.** The conjugation of a contraction by an isometry of the norm is a contraction with the same ratio, and it conjugates the fixed point equation of the attractor; the commutation case follows.

**Corollary (the standard symmetry).** A system is symmetric under the tessarine sign exactly when its two coordinate systems coincide, because the tessarine sign exchanges the two idempotent coordinates; hence the systems $\{f_{i}\}$ with $f_{i}=(f_{i}^{+},f_{i}^{+})$ in the coordinates are the symmetric ones, and they are exactly the systems whose attractor is invariant under the exchange.

**Proof.** The tessarine sign sends the pair $(f_{i}^{+},f_{i}^{-})$ to $(f_{i}^{-},f_{i}^{+})$, so the system is preserved exactly when the two coordinate systems agree; the attractor of a system commuting with an involution is preserved by it.

## Summary

An affine map of the reduced biquaternion algebra is the pair of two complex affine maps, and there is a single notion of affine system because the left, the right and the two-sided multiplications coincide on the diagonal model. The operator norm of the left multiplication is the largest of the two moduli of the idempotent coordinates, so the contraction criterion is $\max(|\alpha|,|\beta|)<1$ and the similarity criterion is $|\alpha|=|\beta|$, the ratio being the common modulus; for a self-similar system with equal ratios in the two coordinates the similarity dimension solves the classical equation $\sum_{i}r_{i}^{s}=1$, the same equation as in each coordinate. The attractor exists by the contraction principle and is the matched set of the pairs coded by the same sequence of generators, a graph-like subset of the product of the two coordinate attractors, of the dimension of one coordinate attractor when the two systems have the same ratios. The square is surjective with four branches generically, none of the elements is rootless, and the branching set is the zero-divisor cone; a branch is a similarity exactly when the two coordinate values have equal modulus. The involutions conjugate a system to another system and preserve the attractor of a symmetric one, and the exchange of the two coordinates is the standard symmetry of a system whose two coordinate systems coincide.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}=Q_{+}\Pi_++Q_{-}\Pi_-$ | the element and its coordinates |
| $\langle \breve Q\rangle_{\mathrm{ts}*}=\tfrac12(\lvert Q_{+}\rvert^{2}+\lvert Q_{-}\rvert^{2})$ | the topological norm of the algebra |
| $P\,\breve Q\,Q=(p\,q\,Q_{+})\Pi_++(p'q'Q_{-})\Pi_-$ | the diagonal two-sided multiplication |
| $\lVert L_{\breve Q}\rVert=\max(\lvert Q_{+}\rvert,\lvert Q_{-}\rvert)$ | the operator norm |
| $\max(\lvert\alpha\rvert,\lvert\beta\rvert)<1$ | the contraction criterion |
| $\lvert\alpha\rvert=\lvert\beta\rvert$ | the similarity criterion, ratio the common modulus |
| $\sum_{i}r_{i}^{s}=1$ | the similarity dimension equation |
| $\mathcal{K}=\bigcup_{i}f_{i}(\mathcal{K})$ | the attractor equation |
| $\breve Q=\pm\sqrt{w_{1}}\Pi_+\pm\sqrt{w_{2}}\Pi_-$ | the branches of the square |
| $\{Q_{+}=0\}\cup\{Q_{-}=0\}$ | the zero-divisor cone, the branching set |

## Further Reading

- [The Multiplication Operators of the Algebra of the Reduced Biquaternions](the-multiplication-operators-of-the-general-plain-algebra-of-the-reduced-biquaternions.html), above this article, for the operators and their norms.
- [Zero Divisors of the Algebra of the Reduced Biquaternions](zero-divisors-of-the-general-plain-algebra-of-the-reduced-biquaternions.html), above this article, for the branching cone.
- [The Idempotent Decomposition and the Split Fractal](the-idempotent-decomposition-and-the-reduced-biquaternion-split-fractal.html), above this article, for the attractor as the matched set of the coding space.
- [The Reduced Biquaternion Quadratic Map and Its Julia Sets](the-reduced-biquaternion-quadratic-map-and-its-julia-sets.html), above this article, for the quadratic family.
- [The Hausdorff Dimension of the Reduced Biquaternion Julia Sets](the-hausdorff-dimension-of-the-reduced-biquaternion-julia-sets.html), below this article, for the dimension of the attractors of the quadratic family.
- [The Biquaternion Iterated Function Systems](the-biquaternion-iterated-function-systems.html), for the companion in which the left and the right affine systems differ.
