# __Reduced Biquaternion Automorphisms and Derivations__

## Introduction

The reduced biquaternion algebra is the commutative four-real-dimensional algebra

$$
\mathbb{B}_{\mathrm{r}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\oplus\mathbb{C},
$$

of basis $1,i,j,ij$ with $i^{2}=-1$, $j^{2}=+1$ and $ji=ij$, whose two complementary central idempotents are $\Pi_{\pm}=\tfrac12(1\pm j)$. An element is $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ with $Q_{\blacktriangle}=q_{\blacktriangle}+iq'_{\blacktriangle}$ and $Q_{\blacktriangledown}=q_{\blacktriangledown}+iq'_{\blacktriangledown}$ complex, and it is the pair $(Q_{+},Q_{-})=(Q_{\blacktriangle}+Q_{\blacktriangledown},Q_{\blacktriangle}-Q_{\blacktriangledown})$ of its idempotent coordinates, $\breve Q=Q_{+}\Pi_++Q_{-}\Pi_-$. An automorphism of the algebra is a bijective linear map preserving the multiplication and the unit; a derivation is a linear map satisfying the Leibniz rule $D(\breve Q_{1}\breve Q_{2})=D(\breve Q_{1})\breve Q_{2}+\breve Q_{1}D(\breve Q_{2})$. Both are structural invariants of the multiplication, and both are decided by one fact: the algebra is a direct product of two copies of the complex field, and it is not simple.

The biquaternion algebra exhibits the opposite behaviour, and the contrast organises the article. There the algebra is simple, so every derivation is inner and the automorphisms over $\mathbb{C}$ are the inner ones, a group of complex dimension three; the reduced biquaternion algebra has no nonzero derivation at all, and its automorphism group is finite of order eight. The reduction is the whole content: an automorphism must permute the two primitive idempotents, and then acts on each complex factor by an $\mathbb{R}$-algebra automorphism, of which there are two; a derivation annihilates the idempotents, and then acts on each factor by an $\mathbb{R}$-derivation of $\mathbb{C}$, of which there are none.

The article owns the structure of the automorphism group, its generators in the algebra's own vocabulary, its finite order, the inner automorphisms, and the vanishing of the derivations. The multiplication and the idempotents are *Reduced Biquaternion Space*; the bar, the tessarine sign, the star and the flat are *The Two Involutions and the Group of Involutions*; the ideals, the radical and the failure of simplicity are *Ideals and Peirce Decomposition of the Algebra of the Reduced Biquaternions*; the zero divisors that the automorphisms permute are *Zero Divisors of the Algebra of the Reduced Biquaternions*; the group of units is *The Group of Units of the Algebra of the Reduced Biquaternions*. The biquaternion counterpart, where the algebra is simple and the derivations are inner, is *Biquaternion Automorphisms and Derivations*.

## The Idempotents and the Factor Structure

**Proposition (the idempotents).** The idempotents of $\mathbb{B}_{\mathrm{r}}$ are exactly $0$, $\Pi_+$, $\Pi_-$ and $1$, and the only primitive ones are $\Pi_+$ and $\Pi_-$.

**Proof.** In the isomorphism $\mathbb{B}_{\mathrm{r}}\cong\mathbb{C}\oplus\mathbb{C}$ a pair $(Q_{+},Q_{-})$ satisfies $(Q_{+},Q_{-})^{2}=(Q_{+},Q_{-})$ exactly when each coordinate is $0$ or $1$, giving the four listed elements; a primitive idempotent is a nonzero idempotent that is not the sum of two nonzero orthogonal idempotents, which excludes $1$ and leaves $\Pi_+$ and $\Pi_-$. Equivalently $Q_{+}^{2}=Q_{+}$ and $Q_{-}^{2}=Q_{-}$ in the field $\mathbb{C}$ have only the roots $0$ and $1$.

**Proposition (the algebra is the direct product of its factors).** The map $\varphi(\breve Q)=(Q_{\blacktriangle}+Q_{\blacktriangledown},Q_{\blacktriangle}-Q_{\blacktriangledown})$ is an isomorphism $\mathbb{B}_{\mathrm{r}}\to\mathbb{C}\oplus\mathbb{C}$ of $\mathbb{R}$-algebras and of $\mathbb{C}$-algebras, the product being componentwise.

**Proof.** $\varphi$ is $\mathbb{C}$-linear and bijective, and $\varphi(\breve Q_{1}\breve Q_{2})=((Q_{1\blacktriangle}+Q_{1\blacktriangledown})(Q_{2\blacktriangle}+Q_{2\blacktriangledown}),(Q_{1\blacktriangle}-Q_{1\blacktriangledown})(Q_{2\blacktriangle}-Q_{2\blacktriangledown}))=\varphi(\breve Q_{1})\varphi(\breve Q_{2})$ by the multiplication rule $\breve Q_{1}\breve Q_{2}=(Q_{1\blacktriangle}Q_{2\blacktriangle}+Q_{1\blacktriangledown}Q_{2\blacktriangledown})+(Q_{1\blacktriangle}Q_{2\blacktriangledown}+Q_{1\blacktriangledown}Q_{2\blacktriangle})j$.

**Corollary (the factors).** Every element is uniquely $Q_{+}\Pi_++Q_{-}\Pi_-$, the two lines $\mathbb{C}\Pi_+$ and $\mathbb{C}\Pi_-$ are the two minimal two-sided ideals, they annihilate each other, and the algebra is semisimple but not simple.

## Automorphisms over $\mathbb{R}$

**Proposition (the permutation of the factors).** Let $\alpha$ be an automorphism of $\mathbb{B}_{\mathrm{r}}$ over $\mathbb{R}$. Then $\{\alpha(\Pi_+),\alpha(\Pi_-)\}=\{\Pi_+,\Pi_-\}$.

**Proof.** $\alpha$ carries idempotents to idempotents and preserves the unit and the product, so $\alpha(\Pi_+)$ and $\alpha(\Pi_-)$ are nonzero orthogonal idempotents with sum $1$; by the proposition on idempotents each is primitive, and the two primitive idempotents are $\Pi_+$ and $\Pi_-$.

**Theorem (the automorphism group over $\mathbb{R}$).** Every automorphism over $\mathbb{R}$ is of one of the two forms

$$
Q_{+}\Pi_++Q_{-}\Pi_-\longmapsto f(Q_{+})\Pi_++g(Q_{-})\Pi_-, \qquad Q_{+}\Pi_++Q_{-}\Pi_-\longmapsto f(Q_{-})\Pi_++g(Q_{+})\Pi_-,
$$

where each of $f$ and $g$ is the identity or the complex conjugation. Hence the automorphism group over $\mathbb{R}$ has exactly eight elements; it is the semidirect product $(\mathbb{Z}/2)^{2}\rtimes(\mathbb{Z}/2)$ and is isomorphic to the dihedral group of order eight.

**Proof.** By the proposition $\alpha$ either fixes the two factors or exchanges them. If it fixes them, then it restricts to an $\mathbb{R}$-algebra automorphism of each copy of $\mathbb{C}$, and the $\mathbb{R}$-algebra automorphisms of $\mathbb{C}$ are the identity and the conjugation, because an automorphism fixes $\mathbb{R}$ pointwise and sends $i$ to a root of $-1$, that is to $\pm i$; this gives four maps. If it exchanges them, then it is the exchange composed with an automorphism fixing the factors, giving four more. The eight are distinct on the basis and they are automorphisms, since conjugation is one and the exchange $Q_{+}\Pi_++Q_{-}\Pi_-\mapsto Q_{-}\Pi_++Q_{+}\Pi_-$ preserves the componentwise product. The conjugation on the first factor commutes with that on the second, and the exchange conjugates the first into the second, which is the presentation of the dihedral group; the group is non-abelian because the two do not commute.

**Corollary (the generators in the algebra).** The group is generated by the three involutions

$$
\tau: Q_{+}\Pi_++Q_{-}\Pi_-\longmapsto\bar Q_{+}\,\Pi_++Q_{-}\Pi_-, \qquad
{}_{\mathrm{ts}}: Q_{+}\Pi_++Q_{-}\Pi_-\longmapsto Q_{-}\Pi_++Q_{+}\Pi_-, \qquad
\bar{\cdot}: Q_{+}\Pi_++Q_{-}\Pi_-\longmapsto\bar Q_{+}\,\Pi_++\bar Q_{-}\,\Pi_-,
$$

the **idempotent conjugation**, the **tessarine sign** and the **coefficient conjugation**, which in the basis $1,i,j,ij$ act as

$$
\tau: i\longmapsto -ij,\; j\longmapsto j,\; ij\longmapsto -i, \qquad
{}_{\mathrm{ts}}: i\longmapsto i,\; j\longmapsto -j,\; ij\longmapsto -ij,
$$

and $\bar{\cdot}:i\mapsto-i$, $j\mapsto j$, $ij\mapsto-ij$. The tessarine sign is the exchange of the two factors and the coefficient conjugation is the conjugation on both factors at once; their composite is the star ${}^{*}=\bar{\cdot}\circ{}_{\mathrm{ts}}$.

**Proof.** Reading $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ gives $Q_{+}=Q_{\blacktriangle}+Q_{\blacktriangledown}$ and $Q_{-}=Q_{\blacktriangle}-Q_{\blacktriangledown}$, so conjugating $Q_{+}$ alone sends $Q_{\blacktriangle}$ to $\bar Q_{\blacktriangle}$ and $Q_{\blacktriangledown}$ to $Q_{\blacktriangledown}$, that is $i\mapsto-ij$ on the basis, while conjugating both sends $Q_{\blacktriangle}$ and $Q_{\blacktriangledown}$ to their conjugates, that is $i\mapsto-i$; the exchange sends $Q_{\blacktriangledown}$ to $-Q_{\blacktriangledown}$, that is $j\mapsto-j$. Direct substitution into the relations $i^{2}=-1$, $j^{2}=1$, $ji=ij$ verifies that each map preserves them.

**Proposition (the group of involutions inside).** The three conjugations $\bar{\cdot}$, ${}_{\mathrm{ts}}$ and ${}^{*}$ are automorphisms, they generate the subgroup $\{1,\bar{\cdot},{}_{\mathrm{ts}},{}^{*}\}\cong(\mathbb{Z}/2)^{2}$ of the automorphism group, and the flat ${}^{\flat}=-{}^{*}$ is not an automorphism.

**Proof.** The coefficient conjugation is an automorphism because $\overline{\breve Q_{1}\breve Q_{2}}=\bar{\breve Q_{1}}\bar{\breve Q_{2}}$ in $\mathbb{C}\oplus\mathbb{C}$, and the tessarine sign is the exchange, which is an automorphism; their composite is one too, and the four maps are distinct and commute. The flat is the negative of the star, so it is not unital: ${}^{\flat}(1)=-1$.

## Automorphisms over $\mathbb{C}$

**Theorem (the automorphism group over $\mathbb{C}$).** An automorphism of $\mathbb{B}_{\mathrm{r}}$ that is $\mathbb{C}$-linear is either the identity or the tessarine sign; the automorphism group over $\mathbb{C}$ has order two and is generated by the exchange of the two factors.

**Proof.** A $\mathbb{C}$-linear automorphism is in particular $\mathbb{R}$-linear, so it is one of the eight maps of the theorem above; a map of that list is $\mathbb{C}$-linear exactly when the maps $f$ and $g$ are the identity, because the conjugations are antiholomorphic, that is $f(\lambda z)\neq\lambda f(z)$ for $\lambda\in\mathbb{C}$ non-real. The exchange is $\mathbb{C}$-linear because $\lambda$ is central.

**Remark (why the order drops).** Over $\mathbb{R}$ the field $\mathbb{C}$ has two automorphisms, and each of the two factors contributes one; over $\mathbb{C}$ the field $\mathbb{C}$ has only the identity, so the two factorwise choices vanish and only the exchange of the two factors survives. The same mechanism appears in the biquaternion algebra, where the complex-linear automorphisms are the inner ones and are far from trivial, because there the algebra is simple and every automorphism is inner.

## Inner Automorphisms and Derivations

**Proposition (the inner automorphisms are trivial).** The algebra is commutative, so for every unit $P$ the conjugation $\breve Q\mapsto P \breve Q P^{-1}$ is the identity; every inner automorphism is the identity, and all eight automorphisms of the theorem above are outer.

**Proof.** $P \breve Q=\breve Q P$ for every $\breve Q$ because the algebra is commutative, so $P \breve Q P^{-1}=\breve Q$.

**Theorem (the derivations vanish).** Every $\mathbb{R}$-derivation of $\mathbb{B}_{\mathrm{r}}$ is zero, and every $\mathbb{C}$-derivation is zero: the derivation space is $\{0\}$ over both fields.

**Proof.** Let $D$ be an $\mathbb{R}$-derivation. From the Leibniz rule $D(1)=D(1\cdot1)=2D(1)$, so $D(1)=0$, and from $\Pi_\pm=\Pi_\pm^{2}$ one has $D(\Pi_\pm)=2\Pi_\pm D(\Pi_\pm)$, so $D(\Pi_\pm)=0$; then $D$ is determined on the direct product by its restrictions to the two factors, which are $\mathbb{R}$-derivations $\mathbb{C}\to\mathbb{C}$. A derivation of a field vanishes on its prime field, and $\mathbb{C}$ is algebraic over $\mathbb{R}$, so for $z\in\mathbb{C}$ with minimal polynomial $p$ one has $0=D(p(z))=p'(z)D(z)$ with $p'(z)\neq0$, whence $D(z)=0$. The two restrictions are therefore zero and $D=0$. The complex case is the same computation read over $\mathbb{C}$.

**Corollary (no exponential of a derivation, no adjoint action).** The Lie algebra of the automorphism group of $\mathbb{B}_{\mathrm{r}}$ is zero, so the automorphism group is a discrete group of order eight with no continuous part; the adjoint map $\mathrm{ad}$ of the algebra into its own endomorphisms is identically zero, the algebra being commutative and therefore abelian as a Lie algebra.

**Remark (the contrast with the biquaternion algebra).** For the biquaternion algebra the derivations are the inner ones and the derivation space has complex dimension three, which is the Lie algebra of the automorphism group; here the derivation space is zero and the automorphism group is finite. The difference is exactly the difference between a simple algebra and a direct product: the derivation space of $\mathbb{C}\Pi_+\oplus\mathbb{C}\Pi_-$ is the direct sum of the derivation spaces of the factors, and each factor is a field.

## Worked Examples

**The eight automorphisms on the basis.** In the ordered basis $(1,i,j,ij)$ the eight maps have the following matrices over $\mathbb{R}$, where a factor $\pm1$ on a basis vector is read off the rules $i\mapsto\pm i$, $j\mapsto\pm j$, $ij\mapsto\pm ij$ with the two signs tied by the product:

| automorphism | $1$ | $i$ | $j$ | $ij$ |
|---|---|---|---|---|
| identity | $1$ | $i$ | $j$ | $ij$ |
| $\bar{\cdot}$ (conjugate both factors) | $1$ | $-i$ | $j$ | $-ij$ |
| ${}_{\mathrm{ts}}$ (exchange the factors) | $1$ | $i$ | $-j$ | $-ij$ |
| ${}^{*}=\bar{\cdot}\circ{}_{\mathrm{ts}}$ | $1$ | $-i$ | $-j$ | $ij$ |
| $\tau$ (conjugate the first factor) | $1$ | $-ij$ | $j$ | $-i$ |
| $\tau\circ{}_{\mathrm{ts}}$ | $1$ | $-ij$ | $-j$ | $i$ |
| $\tau\circ\bar{\cdot}$ (conjugate the second factor) | $1$ | $ij$ | $j$ | $i$ |
| $\tau\circ\bar{\cdot}\circ{}_{\mathrm{ts}}$ | $1$ | $ij$ | $-j$ | $-i$ |

**The two non-commuting involutions.** The product $\tau\circ{}_{\mathrm{ts}}$ sends $Q_{+}\Pi_++Q_{-}\Pi_-$ to $\bar Q_{-}\Pi_++Q_{+}\Pi_-$, and its square is the conjugation $\bar{\cdot}$ on both coordinates; hence $\tau\circ{}_{\mathrm{ts}}$ has order four while $\tau$ and ${}_{\mathrm{ts}}$ have order two, and the relations are those of the dihedral group. In the basis, $\tau\circ{}_{\mathrm{ts}}$ sends $i$ to $-ij$ and $ij$ to $i$, so on the ordered pair $(i,ij)$ it is the quarter turn $x\,i+y\,ij\mapsto y\,i-x\,ij$.

**Verification.** The eight listed maps were checked to be multiplicative by recomputation on random elements of the algebra, and the subgroup they generate was computed and found to have order eight, non-abelian with two elements of order four; the linear system expressing the Leibniz rule for a derivation on the four basis elements, sixteen unknowns against the sixty-four equations, was solved exactly and found to have rank sixteen, so its solution space is $\{0\}$.

## Summary

The reduced biquaternion algebra is the direct product $\mathbb{C}\Pi_+\oplus\mathbb{C}\Pi_-$ of two complex fields, so its four idempotents are $0,\Pi_+,\Pi_-,1$ and an automorphism must permute the two primitive ones. Over $\mathbb{R}$ an automorphism is the identity or the conjugation on each factor together with a possible exchange of the two, giving a group of order eight isomorphic to the dihedral group and generated by the idempotent conjugation $\tau$, the tessarine sign ${}_{\mathrm{ts}}$ (the exchange) and the coefficient conjugation $\bar{\cdot}$; over $\mathbb{C}$ the factorwise conjugations are not linear and only the identity and the exchange survive, a group of order two. The three conjugations $\bar{\cdot}$, ${}_{\mathrm{ts}}$, ${}^{*}$ form a Klein four subgroup of the automorphism group, while the flat is not an automorphism because it is not unital. The algebra is commutative, so every inner automorphism is the identity and all automorphisms are outer; and every derivation is zero, over $\mathbb{R}$ and over $\mathbb{C}$, because a derivation annihilates the idempotents and acts on each complex factor by a derivation of a field, where an algebraic extension admits none. The contrast with the biquaternion algebra, whose automorphisms over $\mathbb{C}$ are the inner ones and whose derivations are inner and three-dimensional, is the contrast between a direct product and a simple algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Pi_{\pm}=\tfrac12(1\pm j)$ | the two primitive idempotents, the coordinates of the direct product |
| $\breve Q=Q_{+}\Pi_++Q_{-}\Pi_-$ | an element in idempotent coordinates, $Q_{+}=Q_{\blacktriangle}+Q_{\blacktriangledown}$, $Q_{-}=Q_{\blacktriangle}-Q_{\blacktriangledown}$ |
| $\bar{\cdot}$ | the coefficient conjugation, the conjugation of both factors |
| ${}_{\mathrm{ts}}$ | the tessarine sign, the exchange $Q_{+}\leftrightarrow Q_{-}$ of the two factors, $Q_{\blacktriangledown}\mapsto-Q_{\blacktriangledown}$ |
| ${}^{*}=\bar{\cdot}\circ{}_{\mathrm{ts}}$ | the star, the conjugation of both coordinates |
| $\tau$ | the idempotent conjugation $Q_{+}\Pi_++Q_{-}\Pi_-\mapsto\bar Q_{+}\Pi_++Q_{-}\Pi_-$, $i\mapsto-ij$ |
| $\operatorname{Aut}_{\mathbb{R}}(\mathbb{B}_{\mathrm{r}})$ | the automorphism group over $\mathbb{R}$, dihedral of order eight |
| $\operatorname{Aut}_{\mathbb{C}}(\mathbb{B}_{\mathrm{r}})$ | the automorphism group over $\mathbb{C}$, of order two, generated by ${}_{\mathrm{ts}}$ |
| $\operatorname{Der}(\mathbb{B}_{\mathrm{r}})$ | the derivation space, $\{0\}$ over $\mathbb{R}$ and over $\mathbb{C}$ |
| $D(\breve Q_{1}\breve Q_{2})=D(\breve Q_{1})\breve Q_{2}+\breve Q_{1}D(\breve Q_{2})$ | the Leibniz rule defining a derivation |

## Further Reading

- [Reduced Biquaternion Space](reduced-biquaternion-space.html), above this article in this category, for the multiplication, the idempotents and the isomorphism $\mathbb{B}_{\mathrm{r}}\cong\mathbb{C}\oplus\mathbb{C}$.
- [The Two Involutions and the Group of Involutions](the-two-involutions-and-the-group-of-involutions-of-the-reduced-biquaternions.html), above this article, for the bar, the tessarine sign, the star and the flat.
- [Ideals and Peirce Decomposition of the Algebra of the Reduced Biquaternions](ideals-and-peirce-decomposition-of-the-general-plain-algebra-of-the-reduced-biquaternions.html), below this article, for the minimal two-sided ideals that an automorphism permutes.
- [The Group of Units of the Algebra of the Reduced Biquaternions](the-group-of-units-of-the-general-plain-algebra-of-the-reduced-biquaternions.html), below this article, for the units whose inner automorphisms are all trivial.
- [Biquaternion Automorphisms and Derivations](biquaternion-automorphisms-and-derivations.html), for the companion in which the algebra is simple, the automorphisms over $\mathbb{C}$ are inner and the derivations are inner and three-dimensional.
- [Split-Biquaternion Automorphisms and Derivations](split-biquaternion-automorphisms-and-derivations.html), for the split-complex companion.
