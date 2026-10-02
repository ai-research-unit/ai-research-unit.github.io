
# __The Signed Sandwich on a Topological Vector Space__

## Introduction

On a topological vector space carrying a continuous multiplication each pair of elements produces a **sandwich**, the operator $x \mapsto axb$ with the two factors fixed, and an order-two automorphism of the algebra — a **grade involution** — produces its **signed** variant $x \mapsto a\alpha(x)b$. The signed sandwich is the composite of the unsigned one with the grade involution, so the two families are reparametrisations of one another; the sandwich maps compose by the rule $(a, b)(r, s) = (ar, sb)$, the signed ones by the twisted rule, the invertible ones form the group of two-sided operators with the inner automorphisms among them, and on a homogeneous element the signed sandwich is the unsigned one multiplied by the parity sign. Read on the operator algebra of a topological vector space, the inner sandwiches are the inner automorphisms by the invertible operators, and their involutive members are the reflections developed in the companion article.

This article develops the two sandwiches on a topological vector space with a continuous multiplication, their continuity, their composition laws, their relation, their homogeneity signs and their invertibility. The one-sided case is *The Signed Left Multiplication on a Topological Vector Space*, the reflections the inner sandwiches realise are *Reflections as Signed Two-Sided Operators on a Topological Vector Space*, and the adjoints with respect to the pairing of the category are *The Signed Adjoint Sandwich on a Topological Vector Space*. The one-sided multiplications and the composition laws are *The Left and Right Multiplication Operators on a Topological Vector Space*; the abstract algebra version is *The Signed Sandwich on an Algebra* in the next category of this Part; the trace pairing used by the adjoint articles is *The Adjoint of the Left Multiplication on a Topological Vector Space*. No form and no involution on the elements is used here.

Throughout, $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$, $E$ is an associative topological algebra over $\mathbb{K}$ with a jointly continuous multiplication and a unit $1$, $\mathcal{L}(E)$ is its operator algebra, and $\alpha$ is a **grade involution**: a continuous algebra automorphism of $E$ with $\alpha^{2} = \mathrm{id}$. A concrete instance is $\alpha(x) = TxT$ for an involutive operator $T \in \mathcal{L}(E)$ with $T^{2} = \mathrm{id}$, and on the operator algebra $\mathcal{L}(F)$ of a topological vector space the instance is $\alpha(A) = TAT$ for an involutive $T \in \mathcal{L}(F)$. An element is **homogeneous** when it lies in an eigenspace of $\alpha$, and its **sign** is $\varepsilon_{x} = +1$ on the fixed part and $-1$ on the negated part.

## The Two Sandwiches

**Definition.** For $a, b \in E$ the **unsigned sandwich** and the **signed sandwich** are the operators on $E$

$$
\Phi_{a,b}(x) = axb, \qquad \Theta^{\alpha}_{a,b}(x) = a\,\alpha(x)\,b .
$$

**Proposition (the sandwiches are continuous operators).** For all $a, b$ the maps $\Phi_{a,b}$ and $\Theta^{\alpha}_{a,b}$ lie in $\mathcal{L}(E)$; the unsigned sandwich is the composite $L_{a}R_{b}$ of the one-sided multiplications, the signed sandwich is $L_{a}R_{b}\alpha$, and the parametrisations $E \times E \to \mathcal{L}(E)$, $(a, b) \mapsto \Phi_{a,b}$ and $(a, b) \mapsto \Theta^{\alpha}_{a,b}$, are continuous for the topology of bounded convergence.

**Proof.** Continuity is the joint continuity of the multiplication and the continuity of $\alpha$; the identifications are $L_{a}R_{b}(x) = a(xb) = axb$ and $L_{a}R_{b}\alpha(x) = a\alpha(x)b$. For the parametrisation, a basic neighbourhood of $0$ is $N(B, V)$ with $B$ bounded; $a x b \in V$ for all $x \in B$ holds uniformly when $a$ and $b$ are small, by the joint continuity of the multiplication on the bounded set $B$.

**Proposition (composition laws).** For all $a, b, r, s \in E$,

$$
\Phi_{a,b}\Phi_{r,s} = \Phi_{ar,sb}, \qquad \Theta^{\alpha}_{a,b}\Theta^{\alpha}_{r,s} = \Theta^{\alpha}_{a\alpha(r),\alpha(s)b} .
$$

**Proof.** $\Phi_{a,b}\Phi_{r,s}(x) = a(rxs)b = (ar)x(sb) = \Phi_{ar,sb}(x)$. For the signed case, $\Theta^{\alpha}_{a,b}\Theta^{\alpha}_{r,s}(x) = a\alpha(r\alpha(x)s)b = a\alpha(s)\alpha(\alpha(x))\alpha(r)b = a\alpha(s)x\alpha(r)b$, using the multiplicativity of $\alpha$ and $\alpha^{2} = \mathrm{id}$, so the composite is the signed sandwich with the pair $(a\alpha(r), \alpha(s)b)$. This is the twisted form of the unsigned rule $(a, b)(r, s) = (ar, sb)$, and it reduces to it when $\alpha = \mathrm{id}$.

**Proposition (the signed sandwich is the unsigned one composed with $\alpha$).** For all $a, b$,

$$
\Theta^{\alpha}_{a,b} = \Phi_{a,b} \circ \alpha = \alpha \circ \Phi_{\alpha(a),\alpha(b)}, \qquad
\Phi_{a,b} = \alpha \circ \Theta^{\alpha}_{\alpha(a),\alpha(b)} = \Theta^{\alpha}_{\alpha(a),\alpha(b)} \circ \alpha .
$$

**Proof.** $\Phi_{a,b}(\alpha(x)) = a\alpha(x)b = \Theta^{\alpha}_{a,b}(x)$, which is the first identity; $(\alpha \circ \Phi_{\alpha(a),\alpha(b)})(x) = \alpha(\alpha(a)x\alpha(b)) = a\alpha(x)b$ by the multiplicativity of $\alpha$, which is the second. Replacing $a, b$ by $\alpha(a), \alpha(b)$ in the first identity and composing with $\alpha$ gives the last, since $\alpha^{2} = \mathrm{id}$.

**Corollary (the sign on homogeneous elements).** If $x$ is homogeneous then

$$
\Theta^{\alpha}_{a,b}(x) = \varepsilon_{x}\,\Phi_{a,b}(x) ,
$$

so the signed sandwich differs from the unsigned one by the parity sign of the element acted on; in particular the two agree on the fixed part of $\alpha$ and are opposite on the negated part.

**Proof.** $\alpha(x) = \varepsilon_{x}x$ for homogeneous $x$, so $a\alpha(x)b = \varepsilon_{x}axb$.

## Invertibility and the Inner Sandwiches

**Proposition (invertibility).** The sandwich $\Phi_{a,b}$ is invertible in $\mathcal{L}(E)$ if and only if $a$ and $b$ are invertible in $E$, and then $\Phi_{a,b}^{-1} = \Phi_{b^{-1},a^{-1}}$; the signed sandwich $\Theta^{\alpha}_{a,b}$ is invertible if and only if $a$ and $b$ are invertible.

**Proof.** If $a, b$ are invertible then $\Phi_{b^{-1},a^{-1}}\Phi_{a,b} = \Phi_{b^{-1}a,ba^{-1}} = \Phi_{1,1} = \mathrm{id}$ and likewise on the other side. Conversely assume $\Phi_{a,b}$ invertible. It is surjective, so for $y \in E$ there is $z$ with $y = azb = (az)b$, and $R_{b}$ is surjective; and it is injective, so $xb = 0$ forces $\Phi_{a,b}(x) = 0$ and hence $x = 0$, and $R_{b}$ is injective. Thus $R_{b}$ is bijective, and then $b$ is a unit: choosing $c$ with $cb = 1$ gives $R_{b}(bc - 1) = bcb - b = 0$, so $bc = 1$ by injectivity. With $b$ a unit, surjectivity of $\Phi_{a,b}$ gives $L_{a}$ surjective, and injectivity of $\Phi_{a,b}$ gives $L_{a}$ injective because $\{xb\} = E$; hence $L_{a}$ is bijective and $a$ is a unit by the same argument. The signed case follows from $\Theta^{\alpha}_{a,b} = \Phi_{a,b}\alpha$ and the invertibility of $\alpha$.

**Definition.** The **inner sandwich** of an invertible $a$ is $\Phi_{a,a^{-1}}$, also written $\mathrm{Ad}_{a}$; the **signed inner sandwich** is $\Theta^{\alpha}_{a,a^{-1}} = \mathrm{Ad}_{a} \circ \alpha$.

**Proposition (the inner sandwiches are automorphisms).** For invertible $a$ the inner sandwich $\mathrm{Ad}_{a}$ is the inner automorphism of $E$ determined by $a$, and the signed inner sandwich is an automorphism of $E$; the group $\{\mathrm{Ad}_{a} : a \in E^{\times}\}$ is isomorphic to $E^{\times}/Z(E)^{\times}$, and its order-two automorphisms are the $\mathrm{Ad}_{a}$ with $a^{2}$ central.

**Proof.** $\mathrm{Ad}_{a}(xy) = axya^{-1} = (axa^{-1})(aya^{-1})$, so $\mathrm{Ad}_{a}$ is an automorphism with inverse $\mathrm{Ad}_{a^{-1}}$; the kernel of $a \mapsto \mathrm{Ad}_{a}$ is the centre $Z(E)$; $\mathrm{Ad}_{a}^{2} = \mathrm{Ad}_{a^{2}}$, which is the identity exactly when $a^{2}$ is central, and this is the criterion computed in the abstract algebra sibling.

**Proposition (involutive inner sandwiches and reflections).** An inner sandwich $\mathrm{Ad}_{a}$ is an involution, $\mathrm{Ad}_{a}^{2} = \mathrm{id}$, exactly when $a^{2}$ is central; the signed inner sandwich of an involutive $a$ with $a^{2} = 1$ is $\Theta^{\alpha}_{a,a} = \mathrm{Ad}_{a} \circ \alpha$, and when $\alpha = \mathrm{Ad}_{a}$ it is the identity. On the operator algebra $\mathcal{L}(F)$ these are the inner automorphisms by the invertible operators and the reflections read as signed two-sided operators.

**Proof.** The first statement is the order-two criterion above; the second is $\Theta^{\alpha}_{a,a^{-1}} = \Theta^{\alpha}_{a,a}$ for $a^{2} = 1$, and $\mathrm{Ad}_{a}\alpha = \mathrm{Ad}_{a}\mathrm{Ad}_{a} = \mathrm{id}$ when $\alpha = \mathrm{Ad}_{a}$. The operator-algebra reading is the instance $E = \mathcal{L}(F)$.

## Examples

**Example (the matrix algebra).** On $E = M_{n}(\mathbb{K})$ the unsigned sandwich $\Phi_{A,B}(X) = AXB$ has matrix $A \otimes B^{\mathsf{T}}$ acting on the matrix space; the inner sandwich $\mathrm{Ad}_{A}$ is conjugation by $A$, and the reflections are the conjugations by involutions, as in the finite-dimensional linear case.

**Example (the operator algebra with a grading).** Let $F = F_{0} \oplus F_{1}$ be a topological vector space graded by a continuous involutive operator $T$, so that $\mathcal{L}(F)$ is graded and $\alpha(A) = TAT$ is its grade involution. Then $\Phi_{A,B}$ is the unsigned double multiplication and $\Theta^{\alpha}_{A,B}(X) = ATXTB$ is the signed one; on a homogeneous $X$ of parity $\varepsilon_{X}$ it is $\varepsilon_{X}AXB$, in agreement with the sign corollary.

**Example (the commutative case).** On $E = C(K)$ with the pointwise product and $\alpha = \mathrm{id}$ the sandwich $\Phi_{f,g}(h) = fgh$ is the multiplication operator by the product $fg$, so the unsigned sandwiches are the multiplication operators; with a nontrivial $\alpha$ the signed sandwich is $fgh \circ \alpha$, and the sign on a homogeneous element is the parity of that element.

## Summary

On a topological algebra $E$ with a jointly continuous multiplication each pair $a, b$ defines the unsigned sandwich $\Phi_{a,b}(x) = axb$ and, with a continuous order-two algebra automorphism $\alpha$, the signed sandwich $\Theta^{\alpha}_{a,b}(x) = a\alpha(x)b$; both are continuous operators, and $\Theta^{\alpha}_{a,b} = \Phi_{a,b}\alpha = \alpha\Phi_{\alpha(a),\alpha(b)}$, so the two families are reparametrisations. They compose by $\Phi_{a,b}\Phi_{r,s} = \Phi_{ar,sb}$ and $\Theta^{\alpha}_{a,b}\Theta^{\alpha}_{r,s} = \Theta^{\alpha}_{a\alpha(r),\alpha(s)b}$, the twisted form of the unsigned rule $(a, b)(r, s) = (ar, sb)$, and on a homogeneous element the signed sandwich is the unsigned one multiplied by the parity sign. The sandwiches are invertible exactly when their two factors are, with $\Phi_{a,b}^{-1} = \Phi_{b^{-1},a^{-1}}$; the inner sandwiches $\Phi_{a,a^{-1}}$ are the inner automorphisms of $E$, the signed inner sandwiches are the composites of an inner automorphism with the grade involution, and an inner sandwich is an involution exactly when the square of its parameter is central. On the operator algebra $\mathcal{L}(F)$ with a grading these are the double multiplications, the inner automorphisms by invertible operators and the reflections; the one-sided signed operator, the reflections and the pairing-based adjoints are the three companion articles.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $E$ | Topological algebra with jointly continuous multiplication |
| $\alpha$ | Grade involution, continuous algebra automorphism with $\alpha^{2} = \mathrm{id}$ |
| $\Phi_{a,b}(x) = axb$ | Unsigned sandwich |
| $\Theta^{\alpha}_{a,b}(x) = a\alpha(x)b$ | Signed sandwich |
| $\Phi_{a,b}\Phi_{r,s} = \Phi_{ar,sb}$ | Unsigned composition law |
| $\Theta^{\alpha}_{a,b}\Theta^{\alpha}_{r,s} = \Theta^{\alpha}_{a\alpha(r),\alpha(s)b}$ | Signed composition law |
| $\varepsilon_{x}$ | Sign of a homogeneous element |
| $\mathrm{Ad}_{a} = \Phi_{a,a^{-1}}$ | Inner automorphism |
| $\Theta^{\alpha}_{a,a^{-1}} = \mathrm{Ad}_{a}\alpha$ | Signed inner sandwich |
| $E^{\times}$, $Z(E)$ | Invertible elements and centre |

## Further Reading

- Nicolas Bourbaki, *Topological Vector Spaces, Chapters 1–5* (Springer, 1987), for the topological algebras, the multiplications and the inner automorphisms.
- Helmut H. Schaefer and Manfred P. Wolff, *Topological Vector Spaces* (Springer, second edition, 1999), for the algebra of operators and the two-sided multiplications.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras I* (Academic Press, 1983), for the inner automorphisms of an operator algebra and the two-sided operators.
- Charles E. Rickart, *General Theory of Banach Algebras* (Van Nostrand, 1960), for the multiplications, the inner automorphisms and the centrality criteria.
- John B. Conway, *A Course in Functional Analysis* (Springer, second edition, 1990), for the two-sided multiplication operators and their continuity.
