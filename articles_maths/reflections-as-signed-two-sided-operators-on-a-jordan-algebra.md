# __Reflections as Signed Two-Sided Operators on a Jordan Algebra__

## Introduction

A **reflection** in the algebraic sense is an operator of order two, $r^2 = \mathrm{id}$, $r \ne \mathrm{id}$. On a graded ring the natural operators of order two are the signed two-sided operators of *The Signed Sandwich on a Ring*, the **signed conjugations** $r_u(x) = u\,\alpha(x)\,u^{-1}$; they are operators of order two exactly when the element $u\alpha(u)$ is central, and this is the criterion the present article develops for a Jordan algebra. The signed conjugation is an automorphism of a Jordan algebra, because it is built from an algebra automorphism $\alpha$ and an inner conjugation, both of which preserve the Jordan product; what has to be decided is when it is an **involution**, and the answer is the **correspondence** between the reflections and the elements $u$ whose twisted square $u\alpha(u)$ is central.

The article defines the signed conjugation on a special Jordan algebra $J = A^+$, proves that it is an automorphism of $J$ and that its square is the inner conjugation by the twisted square $u\alpha(u)$, and derives the correspondence: the signed conjugations are classified by the cosets $uZ(A)^\times$, and the reflections are exactly those with central twisted square. It shows that the reflections do **not** form a group — the composite of two of them is the inner conjugation by $u\alpha(v)$, which is generally not a signed conjugation — but that they generate the inner automorphism group, and it records the **degenerate cases**: a signed conjugation with non-central twisted square is an automorphism of infinite order, not a reflection. Two further identifications are made: the reflection by a symmetry $u = u^{-1}$ coincides with the symmetrised signed sandwich $U_u\circ\alpha$ of *The Signed Sandwich on a Jordan Algebra*, and the reflections of the special Jordan algebra are the operators the inner structure group of *The Left and Right Multiplication Operators on a Jordan Algebra* is built from.

The article assumes *The Signed Sandwich on a Jordan Algebra* for the signed sandwich, its symmetrisation $\Sigma^{\alpha}_{a,b} = U_{a,b}\circ\alpha$ and the definition of the diagonal signed sandwich $r_u$; *The Signed Sandwich on a Ring* for the criterion $u\alpha(u)$ central in the ring case; *The Left and Right Multiplication Operators on a Jordan Algebra* for the quadratic representation, the symmetries and the inner structure group; and *Jordan Algebras* for the special algebra $A^+$. Throughout, $A$ is a commutative-or-not associative unital $R$-algebra, $\alpha$ is a grade involution of $A$ (an automorphism with $\alpha^2 = \mathrm{id}$), $J = A^+$ is the special Jordan algebra with the halved product, and $c_u$ denotes the signed conjugation by the unit $u$. No form, norm, distance or geometric reflection occurs: an operator of order two is all that "reflection" means here, and the symmetric-space reading is deferred to Part IV.

## The Signed Conjugation

### Definition and Automorphism Property

**Definition.** For a unit $u \in A^\times$ the **signed conjugation** by $u$ is the operator

$$
c_u : J \longrightarrow J, \qquad c_u(x) = u\,\alpha(x)\,u^{-1} .
$$

It is $R$-linear and bijective with inverse $c_{u^{-1}}$, and it is the diagonal signed sandwich $S^{\alpha}_{u,u^{-1}}$ of *The Signed Sandwich on a Jordan Algebra*.

**Theorem.** For every unit $u$, the signed conjugation $c_u$ is an automorphism of the Jordan algebra $J$.

*Proof.* For $x, y \in J$,
$$
c_u(x\circ y) = u\,\alpha(x\circ y)\,u^{-1} = u\,\bigl(\alpha(x)\circ\alpha(y)\bigr)\,u^{-1} ,
$$
and, since $z\mapsto uzu^{-1}$ is an algebra automorphism of $A$ and therefore preserves the halved product,
$$
u\,\bigl(\alpha(x)\circ\alpha(y)\bigr)\,u^{-1} = \bigl(u\alpha(x)u^{-1}\bigr)\circ\bigl(u\alpha(y)u^{-1}\bigr) = c_u(x)\circ c_u(y) .
$$
Hence $c_u$ preserves the Jordan product; being bijective, it is an automorphism of $J$. $\square$

**Corollary.** The map $u \mapsto c_u$ is a homomorphism from $A^\times$ to the automorphism group of $J$ (with the composition law computed below); its kernel is the group of units fixed by the automorphism, that is, the units $u$ with $uzu^{-1} = \alpha(z)$ for all $z$, which is $Z(A)^\times$ when $\alpha = \mathrm{id}$.

### The Square and the Twisted Square

**Definition.** For $u \in A^\times$ the **twisted square** is the element

$$
N(u) = u\,\alpha(u) \in A^\times .
$$

It is a unit, because $\alpha(u)$ is a unit, and it satisfies $\alpha(N(u)) = N(u)$ when $u$ is even or when $u^{-1} = \alpha(u)$; in general $N(u)$ need not be fixed by $\alpha$.

**Proposition.** The twisted square is multiplicative up to conjugation:
$$
N(uv) = u\,N(v)\,\alpha(u) ,
$$
and $N(uv) = N(u)N(v)$ whenever $N(v)$ is central.

*Proof.* $N(uv) = uv\,\alpha(uv) = uv\,\alpha(v)\,\alpha(u) = u\,N(v)\,\alpha(u)$; if $N(v)$ is central it commutes with $\alpha(u)$ and the product is $u\alpha(u)N(v) = N(u)N(v)$. $\square$

**Theorem (the square of a signed conjugation).** For every unit $u$,

$$
c_u^2 = \operatorname{conj}_{N(u)} , \qquad c_u^2(x) = u\alpha(u)\,x\,(u\alpha(u))^{-1} .
$$

*Proof.* Compose: $c_u(c_u(x)) = u\,\alpha(u\alpha(x)u^{-1})\,u^{-1} = u\alpha(u)\,\alpha(\alpha(x))\,\alpha(u)^{-1}u^{-1} = N(u)\,x\,N(u)^{-1}$. $\square$

**Corollary.** The square of a signed conjugation is an **inner conjugation** of $J$, by the twisted square $N(u)$.

## Reflections

### Definition

**Definition.** A **reflection** of the graded Jordan algebra $J = A^+$ is a signed conjugation $c_u$ of order two, $c_u^2 = \mathrm{id}$, $c_u \ne \mathrm{id}$.

**Theorem (the criterion).** A signed conjugation $c_u$ is a reflection exactly when the twisted square $N(u) = u\alpha(u)$ is central in $A$; it is then the inner automorphism $\operatorname{conj}_{N(u)}$ of order two, and the reflection satisfies $c_u^2 = \mathrm{id}$.

*Proof.* By the square theorem, $c_u^2 = \operatorname{conj}_{N(u)}$, and an inner conjugation is the identity exactly when the conjugating element is central. $\square$

**Corollary (parity).** If $u$ is fixed by $\alpha$ then $N(u) = u^2$; if $u$ is negated by $\alpha$ then $N(u) = -u^2$; in both cases $N(u)$ is central exactly when $u^2$ is central, so a unit with $u^2$ central gives a reflection whatever its parity. In particular every symmetry of $J$, a unit $u$ with $u \circ u = 1$ in the special product, has $N(u) = u\alpha(u)$ with $\alpha(u) = u^{-1}$ when $u$ is even, whence $N(u) = 1$; and if $u$ is odd then $N(u) = -1$; in either case the reflection condition holds.

### The Relation to the Signed Sandwich

**Proposition.** If the unit $u$ satisfies $u^{-1} = u$, then the reflection $c_u$ is the symmetrised signed sandwich

$$
c_u = U_u\circ\alpha = \Sigma^{\alpha}_{u,u} ,
$$

where $U_u$ is the quadratic representation and $\Sigma^{\alpha}_{u,u}$ is the symmetrised signed sandwich of *The Signed Sandwich on a Jordan Algebra*.

*Proof.* $U_u(\alpha(x)) = u\alpha(x)u$ for the special quadratic representation, and $u = u^{-1}$ turns this into $u\alpha(x)u^{-1} = c_u(x)$. On the other hand $\Sigma^{\alpha}_{u,u} = U_u\circ\alpha$ by definition, so $c_u = U_u\circ\alpha$. $\square$

**Corollary.** The reflections by the symmetries of $J$ are exactly the symmetrised signed sandwiches $\Sigma^{\alpha}_{u,u}$ with $u$ a unit and $u^{-1} = u$; these operators lie in the multiplication algebra and are self-adjoint for the trace form of *The Left and Right Multiplication Operators on a Jordan Algebra*, whereas the general reflection $c_u$ with $u \ne u^{-1}$ is an operator on the module $J$ and need not lie in $\operatorname{Mult}(J)$.

## The Correspondence

### Classifying the Signed Conjugations

**Theorem.** For units $u, v$,
$$
c_u = c_v \iff u^{-1}v \in Z(A)^\times .
$$

*Proof.* Suppose $c_u = c_v$, so $u\alpha(x)u^{-1} = v\alpha(x)v^{-1}$ for all $x$. Applying this with $x = \alpha^{-1}(z)$, which runs through all $z$ as $x$ does, gives $uzu^{-1} = vzv^{-1}$ for all $z$, that is $u^{-1}v$ commutes with every $z$, so $u^{-1}v$ is central. Conversely if $u^{-1}v$ is central then it commutes with $\alpha(x)$, and $u\alpha(x)u^{-1} = v\alpha(x)v^{-1}$ follows from $v = u(u^{-1}v)$ with $u^{-1}v$ central. $\square$

**Corollary.** The correspondence $u \mapsto c_u$ factors through the quotient $A^\times/Z(A)^\times$, and it is injective there; the signed conjugations are in bijection with the **cosets** of the units modulo the central units of $A$.

### The Reflections Among the Signed Conjugations

**Definition.** Let
$$
G = \{u \in A^\times : N(u) = u\alpha(u) \in Z(A)\}
$$
be the set of units with central twisted square, the **reflection group** of the graded algebra.

**Theorem.** $G$ is a subgroup of $A^\times$ containing $Z(A)^\times$, and the reflections are the images $c_u$ of the elements $u \in G$; the reflections are in bijection with the cosets $uZ(A)^\times$ with $u \in G$.

*Proof.* If $u, v \in G$ then $N(v)$ is central, so $N(uv) = N(u)N(v)$ by the multiplicativity up to conjugation, and it is central; thus $uv \in G$. The inverse: $N(u^{-1}) = u^{-1}\alpha(u^{-1}) = (u\alpha(u))^{-1}$? This is $u^{-1}\alpha(u)^{-1} = (u\alpha(u))^{-1} = N(u)^{-1}$ only if $\alpha(u)$ and $u$ commute, which is not automatic; instead $N(u^{-1}) = u^{-1}\alpha(u^{-1}) = u^{-1}\alpha(u)^{-1}$, and its conjugate by $u$ is $u\,u^{-1}\alpha(u)^{-1}\,u^{-1} = \alpha(u)^{-1}u^{-1} = N(u)^{-1}$, so $N(u^{-1})$ is conjugate to $N(u)^{-1}$ and is therefore central exactly when $N(u)$ is; hence $u^{-1} \in G$. The classification is the previous theorem restricted to $G$. $\square$

**Remark (the reflections do not form a group).** The composite of two reflections is
$$
c_u\,c_v = \operatorname{conj}_{u\alpha(v)} ,
$$
because $c_u(c_v(x)) = u\alpha(v)\,x\,\alpha(v)^{-1}u^{-1}$. This inner conjugation is generally not of the form $c_w$: it is a signed conjugation only when $u\alpha(v) = w\alpha(w)w^{-1}$ for some unit $w$, which is not automatic. The reflections therefore generate the inner automorphism group of $J$ without forming a subgroup of it, and the group they generate is the **inner automorphism group** of the graded Jordan algebra.

*Proof.* The computation is the one displayed; the failure of closure is shown by the degenerate example below, where $c_uc_v$ has non-central conjugating element $u\alpha(v)$. $\square$

## Degenerate Cases

### Non-Central Twisted Square

**Proposition.** If $N(u) = u\alpha(u)$ is not central, the signed conjugation $c_u$ is not a reflection: $c_u^2 = \operatorname{conj}_{N(u)} \ne \mathrm{id}$, and $c_u$ is an inner automorphism of infinite order whenever no power of $N(u)$ is central.

*Proof.* $c_u^2 = \operatorname{conj}_{N(u)}$ by the square theorem, and a non-central element does not conjugate to the identity. For the order: $c_u^{2m} = \operatorname{conj}_{N(u)^m}$, which is the identity exactly when $N(u)^m$ is central; if no positive power is central, $c_u$ has infinite order. $\square$

**Example (the unipotent unit).** Let $A = M_2(k)$ with $\alpha = \mathrm{id}$ and $u = I+E_{12}$, a unipotent unit with $u^{-1} = I-E_{12}$. Then $N(u) = u^2 = I+2E_{12}$, which is not central in characteristic not two, and $N(u)^m = I+2mE_{12}$ is non-central for every $m \ne 0$; hence $c_u = \operatorname{conj}_u$ is an inner automorphism of $J$ of infinite order, not a reflection. The failure is exactly the non-centrality of $u\alpha(u)$.

**Example (a graded degenerate unit).** Let $A = M_2(k)$, $\alpha(X) = JXJ^{-1}$ with $J = \operatorname{diag}(1,-1)$, and $u = \bigl(\begin{smallmatrix}2&1\\0&1\end{smallmatrix}\bigr)$. Then $\alpha(u) = \bigl(\begin{smallmatrix}2&-1\\0&1\end{smallmatrix}\bigr)$ and $N(u) = u\alpha(u) = \bigl(\begin{smallmatrix}4&-1\\0&1\end{smallmatrix}\bigr)$, which is not central; the signed conjugation $c_u$ has square $\operatorname{conj}_{N(u)} \ne \mathrm{id}$ and is not a reflection.

### The Trivial Grade Involution

**Example.** If $\alpha = \mathrm{id}$, then $c_u = \operatorname{conj}_u$ is the ordinary inner conjugation and $N(u) = u^2$; the reflection criterion is $u^2$ central, and the reflection group is $\{u : u^2 \in Z(A)\}$. This is the case of *The Signed Sandwich on a Ring* with the trivial grade involution, and it shows that the correspondence between reflections and elements acting by an involution reduces there to the classical statement that an inner conjugation is an involution exactly when its conjugating element squares to a central element.

## Summary

For a special graded Jordan algebra $J = A^+$ with grade involution $\alpha$, the **signed conjugation** $c_u(x) = u\alpha(x)u^{-1}$ is an automorphism of $J$ for every unit $u$; its square is the inner conjugation by the **twisted square** $N(u) = u\alpha(u)$. The signed conjugation is a **reflection**, an operator of order two, exactly when $N(u)$ is central. The signed conjugations are classified by the cosets $uZ(A)^\times$, and the reflections by the cosets with $u$ in the reflection group $G = \{u : N(u) \in Z(A)\}$. The reflections do not form a group: $c_uc_v = \operatorname{conj}_{u\alpha(v)}$, and this is a signed conjugation only rarely; they generate the inner automorphism group. The degenerate case is a unit with non-central twisted square, where $c_u$ is an inner automorphism of infinite order; the unipotent unit $I+E_{12}$ of $M_2(k)$ with $\alpha = \mathrm{id}$ is the model. When $u^{-1} = u$ the reflection is the symmetrised signed sandwich $\Sigma^{\alpha}_{u,u} = U_u\circ\alpha$, and for the symmetries of $J$ this identification holds. No form, norm or geometric reading is used.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A$ | Associative unital $R$-algebra |
| $J = A^+$ | Special Jordan algebra, halved product |
| $\alpha$ | Grade involution, automorphism with $\alpha^2 = \mathrm{id}$ |
| $c_u(x) = u\alpha(x)u^{-1}$ | Signed conjugation by a unit $u$ |
| $N(u) = u\alpha(u)$ | Twisted square |
| $c_u^2 = \operatorname{conj}_{N(u)}$ | Square of a signed conjugation |
| $c_u$ reflection | $N(u)$ central |
| $c_uc_v = \operatorname{conj}_{u\alpha(v)}$ | Composite of two reflections |
| $G = \{u : N(u)\in Z(A)\}$ | Reflection group |
| $c_u = c_v \iff u^{-1}v \in Z(A)^\times$ | Classification of signed conjugations |
| $\Sigma^{\alpha}_{a,b} = U_{a,b}\circ\alpha$ | Symmetrised signed sandwich (Article 7) |
| $c_u = U_u\circ\alpha$ when $u = u^{-1}$ | Reflection as a symmetrised sandwich |

## Further Reading

- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, 1968), for the inner automorphism group, the structure group and the quadratic representation of a Jordan algebra.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the special Jordan algebra, the structure group and the order-two automorphisms.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society Colloquium Publications 44, 1998), for the grade involution, the two-sided operators built from it and the reflections they realise.
- Ottmar Loos, *Symmetric Spaces I: General Theory* (Benjamin, 1969), for the correspondence between order-two automorphisms and the elements that realise them, in the algebraic setting.
- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for the automorphism group of a nonassociative algebra and the inner automorphisms.
