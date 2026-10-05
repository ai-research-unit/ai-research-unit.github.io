
# __Inner Automorphisms of a Ring__

## Introduction

Conjugation by a unit is the one source of automorphisms that every ring, commutative or not, carries internally. For $u \in A^\times$ the **inner automorphism** by $u$ is the map $\operatorname{conj}_u(x) = uxu^{-1}$, and the set of these maps is a group under composition. Read as an operator, $\operatorname{conj}_u$ is the composite $L_u \circ R_{u^{-1}}$ of a left and a right multiplication, and this article studies the inner automorphisms in that operator reading: the factorisation, the composition law, the exact sense in which they form a group, and the point at which commutativity makes them collapse.

The group-theoretic facts — that the inner automorphisms form a normal subgroup of $\operatorname{Aut}(A)$ and that $\operatorname{Inn}(A) \cong A^\times / Z(A)^\times$ — are established in *Ring and Field Automorphisms* and are quoted, not reproved; what is added here is the operator description and the discussion of the failure of commutativity, which is where the noncommutative case differs from the commutative one. The article stays inside Algebra: no length, angle or norm is available to an automorphism, and none is used. The Skolem–Noether theorem, that every automorphism of a central simple algebra is inner, is named as the boundary and deferred to *Automorphisms and Derivations of Algebras*.

Throughout, $A$ is a ring with $1 \neq 0$, not assumed commutative, $A^\times$ is its unit group, $Z(A)$ its centre, and $L_u(x) = ux$, $R_v(x) = xv$ are the one-sided multiplications of *Left and Right Multiplication in a Ring*. The automorphism group is $\operatorname{Aut}(A)$ and the inner automorphism group is $\operatorname{Inn}(A)$, as in *Ring and Field Automorphisms*; the derivations $\operatorname{ad}_a$ and their image $\operatorname{Inn}_{\mathrm{der}}(A)$ are distinct from the automorphism group of this article and are *Derivations of a Ring*.

## The Conjugation Operator

### Definition and first properties

**Definition.** For $u \in A^\times$ the **inner automorphism**, or **conjugation**, by $u$ is

$$
\operatorname{conj}_u : A \to A, \qquad \operatorname{conj}_u(x) = u\,x\,u^{-1}.
$$

In the notation of the one-sided operators it is the composite

$$
\operatorname{conj}_u = L_u \circ R_{u^{-1}} = R_{u^{-1}} \circ L_u,
$$

the two composites agreeing by associativity, and its value at the unit is $\operatorname{conj}_u(1) = 1$.

**Proposition.** For every $u \in A^\times$, $\operatorname{conj}_u$ is a unital ring automorphism of $A$; its inverse is $\operatorname{conj}_{u^{-1}}$, and for all $u, v \in A^\times$

$$
\operatorname{conj}_u \circ \operatorname{conj}_v = \operatorname{conj}_{uv}, \qquad \operatorname{conj}_{u^{-1}} = \operatorname{conj}_u^{-1}.
$$

**Proof.** Additivity is clear; multiplicativity is $\operatorname{conj}_u(xy) = uxyu^{-1} = (uxu^{-1})(uyu^{-1}) = \operatorname{conj}_u(x)\operatorname{conj}_u(y)$, and $\operatorname{conj}_u(1) = uu^{-1} = 1$; bijectivity follows from the inverse formula. The composition law is $(uxu^{-1}) \mapsto v(uxu^{-1})v^{-1} = (vu)x(vu)^{-1}$.

**Proposition (when two conjugations agree).** For $u, v \in A^\times$,

$$
\operatorname{conj}_u = \operatorname{conj}_v \iff uv^{-1} \in Z(A) \iff u = vc \text{ for some } c \in Z(A)^\times .
$$

In particular $\operatorname{conj}_u = \mathrm{id}$ exactly when $u \in Z(A)^\times$.

**Proof.** $\operatorname{conj}_u = \operatorname{conj}_v$ says $uxu^{-1} = vxv^{-1}$ for all $x$, that is, $(v^{-1}u)x = x(v^{-1}u)$ for all $x$, which is $v^{-1}u \in Z(A)$; write $c = v^{-1}u$. The second equivalence is rearrangement. Taking $v = 1$ gives the last statement.

### The composition as an operator

The factorisation $\operatorname{conj}_u = L_u R_{u^{-1}}$ separates the two one-sided pieces, and it explains both the multiplicative law and the collapse on central units: $L$ is a homomorphism and $R$ is an anti-homomorphism, and the two reversals cancel.

**Proposition.** For all $u, v \in A^\times$,

$$
L_u L_v = L_{uv}, \qquad R_u R_v = R_{vu}, \qquad L_u R_v = R_v L_u, \qquad \operatorname{conj}_{uv} = L_{uv} R_{(uv)^{-1}} .
$$

**Proof.** The first two are the composition laws of the one-sided families with $\theta = \mathrm{id}$ and $\alpha = \mathrm{id}$; the third is associativity, $u(xv) = (ux)v$. The last is $(uv)^{-1} = v^{-1}u^{-1}$, so $R_{(uv)^{-1}} = R_{u^{-1}}R_{v^{-1}}$ by the anti-multiplicativity of $R$, and $L_{uv}R_{u^{-1}}R_{v^{-1}} = L_uL_vR_{v^{-1}}R_{u^{-1}} = L_u(L_vR_{v^{-1}})R_{u^{-1}} = L_uR_{u^{-1}}L_vR_{v^{-1}}$, which is $\operatorname{conj}_u\operatorname{conj}_v$ by the commutation of the two families.

**Remark.** The two one-sided factors alone are not automorphisms: $L_u$ is not multiplicative unless $A$ is commutative, and $R_{u^{-1}}$ is anti-multiplicative; only their product is an automorphism. This is the operator form of the fact that an automorphism of a noncommutative ring must undo the order of a product, which a left multiplication alone cannot do.

## The Inner Automorphism Group

### Definition and the isomorphism

**Definition.** The **inner automorphism group** is

$$
\operatorname{Inn}(A) = \{\operatorname{conj}_u : u \in A^\times\},
$$

a subgroup of $\operatorname{Aut}(A)$, and the **outer automorphism group** is the quotient $\operatorname{Out}(A) = \operatorname{Aut}(A)/\operatorname{Inn}(A)$.

**Theorem.** The assignment $u \mapsto \operatorname{conj}_u$ is a group homomorphism $A^\times \to \operatorname{Aut}(A)$ with kernel $Z(A)^\times$, and it induces an isomorphism

$$
A^\times / Z(A)^\times \;\cong\; \operatorname{Inn}(A), \qquad \operatorname{Inn}(A) \trianglelefteq \operatorname{Aut}(A).
$$

**Proof.** The homomorphism and the kernel are the two propositions above; the first isomorphism theorem gives the isomorphism. For normality, if $\varphi \in \operatorname{Aut}(A)$ then $\varphi \operatorname{conj}_u \varphi^{-1} = \operatorname{conj}_{\varphi(u)}$, because $\varphi(uxu^{-1}) = \varphi(u)\varphi(x)\varphi(u)^{-1}$.

**Corollary.** $\operatorname{Inn}(A)$ is trivial exactly when every unit is central; for a commutative ring $Z(A)^\times = A^\times$, so $\operatorname{Inn}(A) = 1$ and $\operatorname{Aut}(A) = \operatorname{Out}(A)$.

### The failure of commutativity

In a commutative ring the inner automorphism group is trivial and carries no information. In a noncommutative ring it can be large and, in contrast with the commutative case, it can be nonabelian.

**Proposition.** $\operatorname{Inn}(A)$ is abelian exactly when $A^\times / Z(A)^\times$ is abelian; equivalently, exactly when every commutator of units is central. In a commutative ring this holds vacuously.

**Proof.** $\operatorname{Inn}(A)$ is isomorphic to $A^\times/Z(A)^\times$ by the theorem, and a group is abelian exactly when the commutator subgroup is trivial, that is, when every commutator $uvu^{-1}v^{-1}$ lies in the centre.

**Example.** In $A = M_n(k)$ over a field $k$ and $n \geq 2$, the unit group is $GL_n(k)$ and the centre is the scalars $k^\times I$, so

$$
\operatorname{Inn}(M_n(k)) \cong GL_n(k)/k^\times I = PGL_n(k),
$$

which is nonabelian for $n \geq 2$. Concretely, for the units $U = \left(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\right)$ and $V = \left(\begin{smallmatrix}1&0\\1&1\end{smallmatrix}\right)$ in $GL_2(\mathbb{Q})$, the two inner automorphisms $\operatorname{conj}_U$ and $\operatorname{conj}_V$ do not commute, because the matrix $UVU^{-1}V^{-1}$ is not scalar: a direct computation gives $UVU^{-1}V^{-1} = \left(\begin{smallmatrix}3&-1\\1&0\end{smallmatrix}\right)$, whose trace is $3$ and which is not of the form $\lambda I$. Hence $\operatorname{Inn}(M_2(\mathbb{Q}))$ is nonabelian, and the inner automorphisms of a noncommutative ring are a genuinely nonabelian group.

**Example (division rings).** If $D$ is a division ring with centre $F$, then $\operatorname{Inn}(D) \cong D^\times/F^\times$, and $\operatorname{Aut}(D)$ contains it. For $D = \mathbb{H}$ the centre is $\mathbb{R}$, so $\operatorname{Inn}(\mathbb{H}) \cong \mathbb{H}^\times/\mathbb{R}^\times$, a group whose structure belongs to the algebra layer; the inner automorphisms of $\mathbb{H}$ are the maps $Q \mapsto UQU^{-1}$ by a quaternion $U \neq 0$.

## Inner Automorphisms and the Other Operators

### Comparison with the automorphisms and the derivations

The inner automorphisms sit inside the two operator structures of this category, and the comparison separates them.

| Operator | Definition | Made from | Group or Lie ring |
|---|---|---|---|
| left multiplication | $L_a(x) = ax$ | one element | not multiplicative |
| right multiplication | $R_a(x) = xa$ | one element | anti-multiplicative |
| inner automorphism | $\operatorname{conj}_u(x) = uxu^{-1}$ | a unit | $\operatorname{Inn}(A) \cong A^\times/Z(A)^\times$ |
| inner derivation | $\operatorname{ad}_a(x) = ax - xa$ | an element | $\operatorname{Inn}_{\mathrm{der}}(A) \cong A/Z(A)$ |

**Remark.** The table is the operator ladder of the ring in miniature: the two one-sided multiplications are the raw material, their pairing on a unit gives an automorphism, and their commutator gives a derivation. The two inner structures are different in kind — one is a group, the other a Lie ring — and they are related by the fact that both measure the failure of an element to be central: $\operatorname{conj}_u = \mathrm{id}$ iff $u$ is central, and $\operatorname{ad}_a = 0$ iff $a$ is central.

**Proposition.** For $u \in A^\times$ and $a \in A$,

$$
[\operatorname{conj}_u, \operatorname{ad}_a] = \operatorname{ad}_{\operatorname{conj}_u(a) - a}.
$$

**Proof.** An inner automorphism acts on the derivation $\operatorname{ad}_a$ by $D \mapsto \operatorname{conj}_u D \operatorname{conj}_u^{-1}$; in the operator picture this is $\operatorname{conj}_u\operatorname{ad}_a\operatorname{conj}_{u^{-1}}$, and computing on $x$ gives $u(au^{-1}xu - u^{-1}xua)u^{-1} = uau^{-1}x - x\,uau^{-1} = \operatorname{ad}_{uau^{-1}}(x)$. So $\operatorname{conj}_u\operatorname{ad}_a\operatorname{conj}_u^{-1} = \operatorname{ad}_{\operatorname{conj}_u(a)}$, and writing the commutator as the difference of this and $\operatorname{ad}_a$ gives the stated form.

### The boundary at the central simple algebras

**Theorem (Skolem–Noether, quoted).** If $A$ is a finite-dimensional central simple algebra over a field $F$, then every $F$-algebra automorphism of $A$ is inner: $\operatorname{Aut}_F(A) = \operatorname{Inn}(A)$ and $\operatorname{Out}(A) = 1$.

**Remark.** This is the sharpest calibration of the inner automorphism group: it says that for the central simple algebras the outer automorphism group vanishes and the whole automorphism group is accounted for by conjugation. Its statement and proof belong to *Automorphisms and Derivations of Algebras*, in the category *Bilinear Algebras*, where the Skolem–Noether theorem is established; it is quoted here only to mark the boundary of the ring-level theory. For a general ring the outer automorphisms can be large, and the quotients of the number-system algebras are computed in that article.

## Examples

| Ring $A$ | $Z(A)$ | $\operatorname{Inn}(A)$ | Nonabelian? |
|---|---|---|---|
| commutative $R$ | $R$ | $1$ | no |
| $\mathbb{H}$ | $\mathbb{R}$ | $\mathbb{H}^\times/\mathbb{R}^\times$ | yes |
| $M_n(k)$, $n \geq 2$ | $k\,I$ | $PGL_n(k)$ | yes for $n \geq 2$ |
| $A \times B$ | $Z(A) \times Z(B)$ | $\operatorname{Inn}(A) \times \operatorname{Inn}(B)$ | if a factor is |
| $k[G]$ for a nonabelian $G$ | depends on $k[G]$ | at least the image of $G$ | generally |

**Proposition.** $\operatorname{Inn}(A \times B) \cong \operatorname{Inn}(A) \times \operatorname{Inn}(B)$ and $Z(A \times B) = Z(A) \times Z(B)$.

**Proof.** A unit of $A \times B$ is a pair of units, and conjugation acts componentwise; the centre is the product of the centres.

## Summary

For a unit $u$ of the ring $A$, the inner automorphism $\operatorname{conj}_u(x) = uxu^{-1}$ is the composite $L_u R_{u^{-1}}$ of a left and a right multiplication; it is a unital automorphism with inverse $\operatorname{conj}_{u^{-1}}$, and $\operatorname{conj}_u\operatorname{conj}_v = \operatorname{conj}_{uv}$. Two conjugations agree exactly when the ratio of their units is central, so $\operatorname{conj}_u = \mathrm{id}$ exactly when $u$ is a central unit, and $u \mapsto \operatorname{conj}_u$ induces $\operatorname{Inn}(A) \cong A^\times/Z(A)^\times$, a normal subgroup of $\operatorname{Aut}(A)$ with $\operatorname{Out}(A) = \operatorname{Aut}(A)/\operatorname{Inn}(A)$ as quotient.

The one-sided factors are not automorphisms — $L_u$ is not multiplicative unless $A$ is commutative, and $R_{u^{-1}}$ is anti-multiplicative — and only their pairing is; this is the operator form of the reversal that a noncommutative automorphism must perform. In the commutative case every unit is central, $\operatorname{Inn}(A) = 1$ and $\operatorname{Aut}(A) = \operatorname{Out}(A)$; in the noncommutative case $\operatorname{Inn}(A)$ can be nonabelian, as $PGL_n(k)$ and $\mathbb{H}^\times/\mathbb{R}^\times$ show. The inner automorphism group and the Lie ring of inner derivations are the two inner structures of the ring, a group and a Lie ring respectively, and both measure the failure of an element to be central. The outer automorphisms vanish for a central simple algebra by the Skolem–Noether theorem, whose proof is in the algebra category.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A$ | Ring with $1 \neq 0$, not assumed commutative |
| $A^\times$, $Z(A)$ | Unit group and centre of $A$ |
| $\operatorname{conj}_u(x) = uxu^{-1}$ | Inner automorphism by a unit $u$ |
| $L_u$, $R_{u^{-1}}$ | Left and right multiplications; $\operatorname{conj}_u = L_uR_{u^{-1}}$ |
| $\operatorname{conj}_u = \operatorname{conj}_v \iff uv^{-1} \in Z(A)$ | Agreement of two conjugations |
| $\operatorname{Inn}(A) \cong A^\times/Z(A)^\times$ | Inner automorphism group |
| $\operatorname{Out}(A) = \operatorname{Aut}(A)/\operatorname{Inn}(A)$ | Outer automorphism group |
| $\operatorname{ad}_a(x) = ax - xa$ | Inner derivation, distinct from the automorphisms |
| $\operatorname{Inn}_{\mathrm{der}}(A) \cong A/Z(A)$ | Lie ring of inner derivations |

## Further Reading

- Israel Nathan Herstein, *Noncommutative Rings* (Mathematical Association of America, 1968), for inner automorphisms, their group structure and the failure of commutativity.
- Nathan Jacobson, *Structure of Rings*, American Mathematical Society Colloquium Publications 37 (1956), for conjugation by units, the inner automorphism group and its relation to the unit group.
- Paul M. Cohn, *Skew Fields: Theory of General Division Rings* (Cambridge University Press, 1995), for the automorphism group of a division ring and the inner automorphisms of a noncommutative field.
- Tsi-Yuen Lam, *A First Course in Noncommutative Rings*, Graduate Texts in Mathematics 131 (Springer, 2nd ed. 2001), for $PGL_n$ as the inner automorphism group of a matrix ring and the Skolem–Noether theorem.
