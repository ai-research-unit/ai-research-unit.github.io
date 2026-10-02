# __Two-Sided Operators with the Signed Product__

## Introduction

The two-sided operators of *The Sandwich on a Clifford Algebra* multiply the argument on the left and on the right. A second family is obtained by twisting the argument itself by the grading: the **signed product** attaches the grade involution to the middle factor, and the operator is

$$
T^{\alpha}_{a,b}(y) = a\,\alpha(y)\,b .
$$

It is the ordinary sandwich of the twisted argument, $T^{\alpha}_{a,b} = T_{a,b}\circ\alpha$, and its geometry is different: where the ordinary sandwich returns the negative of a reflection for an odd parameter, the signed product returns the reflection itself, so the reflections of the quadratic space are carried by the signed family.

Two structural facts organise the article. First, the signed family is closed under composition but with a twisted law, $T^{\alpha}_{a,b}T^{\alpha}_{c,d} = T^{\alpha}_{a\alpha(c),\,\alpha(d)b}$, in which the automorphism enters the parameters; equivalently the composite of two signed operators corresponds to conjugating the middle group element by $\alpha$. Second, the family contains no identity – the identity map is not a signed operator – so it is a **coset** of the group of ordinary two-sided operators rather than a group. The signed family and the ordinary family generate a group together, and the signed operators are exactly the elements of the coset through $\alpha$; this is the precise sense in which "signed" is a position in a group and not a second multiplication.

The ordinary family and its composition are *The Sandwich on a Clifford Algebra*; the operators twisted by the grading and the sign rule of the graded commutator are *The Graded Multiplication Operators*; the signed inner conjugation $\mathrm{Ad}^{\alpha}_x(y) = \alpha(x)yx^{-1}$, whose left factor and not whose argument carries the sign, is *Two-Sided Operators on a Clifford Algebra with Signed Inner Conjugation*; the groups and the reflection formula are *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*. Those are cited. This article owns the family $T^{\alpha}_{a,b}$, its composition law, its coset structure and the reflections it realises; the sandwich specialisation $b = a^{-1}$ is *The Sandwich with the Signed Product*. The base is a field $F$ of characteristic not $2$, $q$ is non-degenerate, $\alpha$ is the grade involution and $\varepsilon_v = -1$ for a vector $v$.

## The Signed Product

**Definition.** For $a, b \in \mathrm{Cl}(V,q)$ the **signed two-sided operator** is the $F$-linear map

$$
T^{\alpha}_{a,b} : \mathrm{Cl}(V,q) \longrightarrow \mathrm{Cl}(V,q), \qquad T^{\alpha}_{a,b}(y) = a\,\alpha(y)\,b .
$$

It is the sandwich by the pair $(a,b)$ composed with the grade involution on the right.

**Proposition (the relation to the ordinary family).** $T^{\alpha}_{a,b} = T_{a,b}\circ\alpha = \alpha\circ T_{\alpha(a),\alpha(b)}$, and $T^{\alpha}_{1,1} = \alpha$. The map $T_{a,b}\mapsto T_{a,b}\alpha$ is a bijection from the ordinary two-sided operators onto the signed ones, with inverse $S\mapsto S\circ\alpha$.

**Proof.** $T^{\alpha}_{a,b}(y) = a\alpha(y)b = T_{a,b}(\alpha(y))$, and conjugating an ordinary sandwich by the automorphism $\alpha$ gives $\alpha T_{a,b}\alpha = T_{\alpha(a),\alpha(b)}$, so that $T_{a,b}\alpha = \alpha T_{\alpha(a),\alpha(b)}$.

**Proposition (linearity and the value at the unit).** $T^{\alpha}_{a,b}$ is $F$-linear; $T^{\alpha}_{a,b}(1) = ab$; and $T^{\alpha}_{a,b} = 0$ exactly when $a = 0$ or $b = 0$.

**Proof.** The unit is even, so $\alpha(1) = 1$; linearity and the vanishing are those of the two-sided product.

**Proposition (the composition laws).** For all $a,b,c,d$

$$
T^{\alpha}_{a,b}\circ T^{\alpha}_{c,d} = T_{a\,\alpha(c),\ \alpha(d)\,b},
\qquad
T^{\alpha}_{a,b}\circ T_{c,d} = T^{\alpha}_{a\,\alpha(c),\ \alpha(d)\,b},
\qquad
T_{a,b}\circ T^{\alpha}_{c,d} = T^{\alpha}_{a c,\ d b}.
$$

So the composite of **two** signed operators is an **ordinary** two-sided operator: the two grade involutions, one from each factor, cancel against each other, and the automorphism survives only through the conjugated parameters. The composite of a signed and an ordinary operator, in either order, is signed. In the ordinary family the law has no automorphism at all, so the signed law is the ordinary law conjugated by $\alpha$, and the cancellation of the two involutions is what makes the double product ordinary again.

**Proof.** $T^{\alpha}_{a,b}\bigl(T^{\alpha}_{c,d}(y)\bigr) = a\,\alpha\bigl(c\,\alpha(y)\,d\bigr)b = a\,\alpha(c)\,\alpha^{2}(y)\,\alpha(d)\,b = a\alpha(c)\,y\,\alpha(d)\,b$, which is the ordinary sandwich with parameters $(a\alpha(c), \alpha(d)b)$ because the middle factor is now $y$ and not $\alpha(y)$. The other two identities are the same computation with one of the two factors untwisted; for the third, $T_{a,b}\bigl(T^{\alpha}_{c,d}(y)\bigr) = a\bigl(c\alpha(y)d\bigr)b = ac\,\alpha(y)\,db$.

**Corollary (the parity of the number of factors).** A composite of signed operators is ordinary when the number of factors is even and signed when it is odd:

$$
\underbrace{T^{\alpha}\circ\cdots\circ T^{\alpha}}_{k} \in
\begin{cases}
\mathcal{T}, & k \text{ even}, \\[2pt]
\mathcal{T}^{\alpha}, & k \text{ odd},
\end{cases}
$$

where $\mathcal{T}$ is the group of invertible ordinary two-sided operators and $\mathcal{T}^{\alpha}$ the signed family. In particular the identity is a composite of two signed operators – $T^{\alpha}_{a,b}\circ T^{\alpha}_{\alpha(a^{-1}),\alpha(b^{-1})} = \mathrm{id}$ – without being one.

**Proof.** Apply the first law repeatedly; the automorphism $\alpha$ occurs once in each signed factor and cancels in pairs.

## The Coset Structure

**Proposition (invertibility).** The signed operator $T^{\alpha}_{a,b}$ is a bijection if and only if $a$ and $b$ are units; its inverse is then the signed operator $T^{\alpha}_{\alpha(a^{-1}),\,\alpha(b^{-1})} = \alpha\,T_{a^{-1},b^{-1}}$.

**Proof.** The first part is the invertibility of the ordinary sandwich, since $\alpha$ is a bijection. For the inverse, the composition law gives $T^{\alpha}_{a,b}\circ T^{\alpha}_{\alpha(a^{-1}),\alpha(b^{-1})} = T_{a\alpha(\alpha(a^{-1})),\,\alpha(\alpha(b^{-1}))b} = T_{a a^{-1},\,b^{-1}b} = T_{1,1} = \mathrm{id}$.

**Proposition (the indeterminacy).** For units, $T^{\alpha}_{a,b} = T^{\alpha}_{a',b'}$ if and only if there is a central unit $c$ with $a' = ac$ and $b' = c^{-1}b$; the kernel of the parametrisation is the diagonal of the central units, exactly as for the ordinary family.

**Proof.** Since $\alpha$ is surjective, $a\alpha(y)b = a'\alpha(y)b'$ for all $y$ says $T_{a,b} = T_{a',b'}$, and the indeterminacy of the ordinary family is the statement quoted.

**Theorem (a coset and not a group).** Let $\mathcal{T}$ be the group of invertible ordinary two-sided operators and let $\mathcal{T}^{\alpha} = \{T^{\alpha}_{a,b} : a, b \in \mathrm{Cl}(V,q)^{\times}\}$. Then

$$
\mathcal{T}^{\alpha} = \mathcal{T}\alpha = \{\,g\alpha : g \in \mathcal{T}\,\},
$$

a coset of $\mathcal{T}$ in the group $\mathcal{T}\langle\alpha\rangle$ generated by $\mathcal{T}$ and the grade involution. Every element of $\mathcal{T}^{\alpha}$ is invertible as a linear map and its inverse lies again in $\mathcal{T}^{\alpha}$; the product of two elements of $\mathcal{T}^{\alpha}$ lies in $\mathcal{T}$, and the product of an element of $\mathcal{T}^{\alpha}$ with an element of $\mathcal{T}$, in either order, lies in $\mathcal{T}^{\alpha}$; but the identity map does not lie in $\mathcal{T}^{\alpha}$: a signed operator that were the identity would satisfy $a\alpha(y)b = y$ for every $y$, hence $ab = 1$ and $a\alpha(y)a^{-1} = y$ for all $y$, forcing $\alpha(y) = y$. Consequently $\mathcal{T}^{\alpha}$ is a **torsor** under $\mathcal{T}$ and not a group, and the family must never be called a group.

**Proof.** The set is $\mathcal{T}\alpha$ by the first proposition. A coset $gH$ of a subgroup satisfies $gH\cdot gH = gHg^{-1}H = H$ and $gH\cdot H = gH = H\cdot gH$; here $H = \mathcal{T}$, $g = \alpha$, and $\alpha\mathcal{T}\alpha = \mathcal{T}$ because conjugating an ordinary sandwich by the automorphism $\alpha$ gives the ordinary sandwich $T_{\alpha(a),\alpha(b)}$. A coset contains the identity exactly when it is the subgroup itself, which here would require $\alpha \in \mathcal{T}$, that is $\alpha(y) = ayb$ for all $y$; at $y = 1$ this gives $ab = 1$, and then $\alpha(y) = aya^{-1}$ with $a$ central, which is the identity and not $\alpha$.

**Remark (the group generated together).** The group $\mathcal{T}\langle\alpha\rangle$ is the subgroup of $\mathrm{GL}_F(\mathrm{Cl})$ generated by the ordinary two-sided operators and the parity operator $\Gamma$. The signed family is its nontrivial coset, and every element is a product of an ordinary operator with $\Gamma$; this is the operator form of the statement that the signed family is a twist of the ordinary one by the grading, made in *The Graded Multiplication Operators*.

## The Reflections

**Theorem (the reflections).** Let $u \in V$ with $q(u) \neq 0$. Then the signed sandwich by $(u, u^{-1})$ is the reflection in the hyperplane $u^{\perp}$:

$$
T^{\alpha}_{u,\,u^{-1}}(v) = u\,\alpha(v)\,u^{-1} = -u\,v\,u^{-1} = \rho_u(v), \qquad v \in V .
$$

**Proof.** A vector is odd, so $\alpha(v) = -v$ and the operator is $-u\,v\,u^{-1}$. Since $u^{-1} = u\,q(u)^{-1}$ and $uvu = 2B(u,v)u - q(u)v$,

$$
-u\,v\,u^{-1} = -\bigl(2B(u,v)u - q(u)v\bigr)q(u)^{-1} = v - 2B(v,u)q(u)^{-1}u = \rho_u(v),
$$

using $B(u,v) = B(v,u)$.

**Corollary (Cartan–Dieudonné).** Every signed sandwich whose parameters are in the Clifford group acts on $V$ as an orthogonal transformation, and the odd ones generate the reflections; a product of signed sandwiches by vectors $u_1, \ldots, u_k$ acts on $V$ as $\rho_{u_1}\cdots\rho_{u_k}$, an orthogonal transformation that is a rotation when $k$ is even and a reflection-times-rotation when $k$ is odd.

**Proof.** Each factor acts as a reflection by the theorem; the composite of the restrictions is the restriction of the composite, and the parity of the number of reflections decides the determinant.

**Remark (why the sign is there).** The ordinary sandwich by a vector $u$ gives $-\rho_u$, the negative of the reflection, as *The Sandwich on a Clifford Algebra* records. The signed product inserts exactly the sign that repairs this, and it does so at the cost of losing the identity; this is the trade described in *The Graded Multiplication Operators* and the reason the signed and the ordinary families are used for different purposes.

## Worked Cases

### A Reflection in $\mathrm{Cl}_{0,3}(\mathbb{R})$

With $e_j^{2} = -1$ let $u = e_1$, so $u^{-1} = -e_1$ and $\alpha(e_j) = -e_j$. Then $T^{\alpha}_{e_1,-e_1}(v) = e_1\alpha(v)(-e_1) = e_1v e_1$, and

$$
T^{\alpha}_{e_1,-e_1}(e_1) = e_1^{3} = -e_1, \qquad T^{\alpha}_{e_1,-e_1}(e_2) = e_1e_2e_1 = -e_1^{2}e_2 = e_2, \qquad T^{\alpha}_{e_1,-e_1}(e_3) = e_3 ,
$$

so on the basis the values are $(-e_1, e_2, e_3)$: the reflection $\rho_{e_1}$, since $\rho_{e_1}(e_1) = -e_1$ when $q(e_1) = -1$ and $\rho_{e_1}$ fixes $e_2, e_3$. The ordinary sandwich by $(e_1, -e_1)$ would have returned $(e_1, -e_2, -e_3) = -\rho_{e_1}$.

### A Rotation

In the same algebra let $x = e_1e_2$, an even unit. Then $T^{\alpha}_{x,x^{-1}}(v) = x\alpha(v)x^{-1} = xvx^{-1}$ for every vector $v$, which is the half-turn $\mathrm{Ad}_x$ of the plane: $(-e_1, -e_2, e_3)$. On the even part the signed and the ordinary sandwiches coincide, since $\alpha$ is the identity there.

### No Identity

In any Clifford algebra the map $\alpha$ is the signed operator $T^{\alpha}_{1,1}$, and it is not the identity. Composing it with itself returns the identity, which is therefore a product of two signed operators without being one; this is the smallest witness that the signed family is a torsor and not a group.

## Summary

The **signed two-sided operator** $T^{\alpha}_{a,b}(y) = a\alpha(y)b$ is the ordinary sandwich composed with the grade involution on the right, $T^{\alpha}_{a,b} = T_{a,b}\alpha$, and $T^{\alpha}_{1,1} = \alpha$. Its composition with another signed operator is an **ordinary** sandwich, $T^{\alpha}_{a,b}T^{\alpha}_{c,d} = T_{a\alpha(c),\alpha(d)b}$, the two grade involutions cancelling; its composition with an ordinary operator, in either order, is signed, $T^{\alpha}_{a,b}T_{c,d} = T^{\alpha}_{a\alpha(c),\alpha(d)b}$ and $T_{a,b}T^{\alpha}_{c,d} = T^{\alpha}_{ac,db}$. It is invertible exactly for units, with inverse $T^{\alpha}_{\alpha(a^{-1}),\alpha(b^{-1})}$, and the kernel of the parametrisation is the central units as before; and $T^{\alpha}_{a,b}(1) = ab$. The family is the **coset** $\mathcal{T}\alpha$ of the group of invertible ordinary two-sided operators: it contains inverses, its products with the group lie in the coset, its products with itself lie in the group, and it contains no identity. It is therefore a torsor, not a group, and a composite of an even number of signed operators is ordinary. Its geometry is the point of the construction: for a vector $u$ with $q(u)\neq0$ the signed sandwich by $(u,u^{-1})$ is exactly the reflection $\rho_u$, where the ordinary sandwich gave $-\rho_u$; so the signed family carries the reflections of the quadratic space and, through products, the orthogonal group. The sandwich specialisation, the versor action and the groups are *The Sandwich with the Signed Product* and *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\alpha$, $\varepsilon_v = -1$ for vectors | Grade involution and its sign |
| $T^{\alpha}_{a,b}(y) = a\,\alpha(y)\,b$ | Signed two-sided operator |
| $T^{\alpha}_{a,b} = T_{a,b}\circ\alpha$ | Relation to the ordinary sandwich |
| $T^{\alpha}_{a,b}T^{\alpha}_{c,d} = T_{a\alpha(c),\alpha(d)b}$ | Two signed give an ordinary operator |
| $\mathcal{T}$, $\mathcal{T}^{\alpha} = \mathcal{T}\alpha$ | Ordinary group; the signed coset, a torsor |
| $T^{\alpha}_{a,b}T_{c,d} = T^{\alpha}_{a\alpha(c),\alpha(d)b}$ | Signed with ordinary gives a signed operator |
| $(ac, c^{-1}b)$, $c \in Z^{\times}$ | Indeterminacy of the parametrisation |
| $T^{\alpha}_{u,u^{-1}} = \rho_u$ | Reflection by a vector |
| $\rho_u(v) = v - 2B(v,u)q(u)^{-1}u$ | Reflection in $u^{\perp}$ |

## Further Reading

- Claude Chevalley, *The Algebraic Theory of Spinors and Clifford Algebras*, Collected Works vol. 2 (Springer, 1997), for the signed conjugation and the reflections.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the reflection formula and the two conjugation actions on the vectors.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced Mathematics 50 (Cambridge University Press, 1995), for the two-sided operators and the grade involution.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for the reflection formula in the low-dimensional algebras.
- Nathan Jacobson, *Lectures in Abstract Algebra II: Linear Algebra* (Van Nostrand, 1953), for the orthogonal group generated by the reflections.
