
# __Left and Right Multiplication in a Ring__

## Introduction

The elementary operators on a ring are the two one-sided multiplications: for $a \in A$, the **left multiplication** $L_a(x) = ax$ and the **right multiplication** $R_a(x) = xa$. They are the operators that carry the ring's own product, one factor at a time, and every other operator of this group — the sandwich, the inner automorphism, the conjugation by a unit — is built from them by composition. This article defines them, computes their composition and commutation laws, identifies their kernels and images with the annihilators and the principal ideals of the ring, and shows how the commutator of the elements appears in the commutator of the operators.

The point of the operator reading is the asymmetry between $L$ and $R$: the assignment $a \mapsto L_a$ is a ring homomorphism, since the order of the elements is the order of the composition, whereas $a \mapsto R_a$ reverses the order and is a homomorphism from the opposite ring. The two families commute with one another, and their failure to commute pairwise is exactly the noncommutativity of $A$: $[L_a, L_b] = L_{[a,b]}$ and $[R_a, R_b] = R_{[b,a]}$, so the element-commutator $[a,b] = ab - ba$ resurfaces as the operator commutator. This is the "commutation up to the commutator" of the menu.

The article is purely algebraic and assumes only *Rings* for the object, its ideals and its annihilators, and *Ring and Field Automorphisms* for the unit group and the conjugation. It stays inside Part I: the operators are endomorphisms of the additive group, and no distance, norm or form is used. The two-sided sandwich, the inner automorphism and the adjoint of a one-sided multiplication are the articles that follow in this group and in the later groups of the category. Throughout, $A$ is a ring with $1 \neq 0$, not assumed commutative; $\operatorname{End}(A)$ is the ring of additive endomorphisms of $A$ under composition, and $Z(A)$, $A^\times$ are the centre and the unit group.

## The Two One-Sided Families

### Definition and first properties

**Definition.** For $a \in A$ the **left multiplication** and the **right multiplication** by $a$ are the additive maps

$$
L_a : A \to A, \quad L_a(x) = ax, \qquad\qquad R_a : A \to A, \quad R_a(x) = xa .
$$

Both take values in $A$ and are additive, because addition distributes over the product; they are **unital** in the sense that $L_a(1) = a = R_a(1)$, so the two families are distinguished by nothing at the unit and must be separated by their composition instead.

**Proposition.** For all $a, b \in A$ and all integers $n$,

$$
L_{a+b} = L_a + L_b, \qquad L_{ab} = L_a \circ L_b, \qquad L_{na} = nL_a,
$$

and the same statements hold for $R$ with the order reversed:

$$
R_{a+b} = R_a + R_b, \qquad R_{ab} = R_b \circ R_a, \qquad R_{na} = nR_a .
$$

Hence $a \mapsto L_a$ is a unital ring homomorphism $A \to \operatorname{End}(A)$, the **left regular representation**, while $a \mapsto R_a$ is a unital ring homomorphism $A^{\mathrm{op}} \to \operatorname{End}(A)$, equivalently an anti-homomorphism $A \to \operatorname{End}(A)$.

**Proof.** Additivity in the parameter is the distributive law. For the composition, $L_a(L_b(x)) = a(bx) = (ab)x = L_{ab}(x)$, while $R_a(R_b(x)) = (xb)a = x(ba) = R_{ba}(x)$, which is the reversal. The integer statements follow from the additive ones.

**Corollary.** $L_a = 0 \iff a = 0$, since $L_a(1) = a$; likewise $R_a = 0 \iff a = 0$. Both maps are therefore injective, and $A$ embeds in $\operatorname{End}(A)$ in two ways.

### Composition and the opposite ring

The reversal in $R$ is not a defect of the notation but the essential difference between the two families.

**Proposition.** The left and the right multiplication commute, $L_a \circ R_b = R_b \circ L_a$ for all $a, b$, and their product is the **two-sided multiplication**

$$
L_a R_b = R_b L_a : x \longmapsto a\,x\,b .
$$

**Proof.** $a(xb) = (ax)b$ by associativity.

**Corollary (the elements that compose in the same order).** For all $a, b$,

$$
[L_a, L_b] = L_{[a,b]}, \qquad [R_a, R_b] = R_{[b,a]} = -R_{[a,b]}, \qquad [L_a, R_b] = 0,
$$

where $[a,b] = ab - ba$ and $[L_a, L_b] = L_aL_b - L_bL_a$. Thus $A$ is commutative exactly when the left multiplications commute pairwise, equivalently when the right multiplications do; the failure is measured by the commutator in both families at once.

**Proof.** $[L_a,L_b] = L_aL_b - L_bL_a = L_{ab} - L_{ba} = L_{ab-ba}$. For the right family, $[R_a,R_b] = R_{ba} - R_{ab} = R_{ba-ab} = R_{[b,a]} = -R_{[a,b]}$, the negative sign being legitimate because $R$ is additive in the parameter. The cross family commutes by the previous proposition.

**Remark.** The sign in $[R_a,R_b] = -R_{[a,b]}$ is the operator shadow of the reversal: a commutator is antisymmetric in the elements, and the right family reports it with the opposite sign because it reverses the order of every product. Only the combinations $[L_a,L_b]$ and $-[R_a,R_b]$ are equal, and neither is zero unless $[a,b] = 0$.

## Kernels, Images and Ideals

### The annihilators

**Definition.** The **left annihilator** and the **right annihilator** of $a \in A$ are

$$
\ell(a) = \{x \in A : ax = 0\}, \qquad r(a) = \{x \in A : xa = 0\}.
$$

Both are additive subgroups, and $\ell(a)$ is a left ideal while $r(a)$ is a right ideal.

**Proposition.** $\ker L_a = \ell(a)$, $\ker R_a = r(a)$; $\operatorname{im} L_a = Aa$, the left ideal generated by $a$, and $\operatorname{im} R_a = aA$, the right ideal generated by $a$.

**Proof.** $L_a(x) = ax$, so its kernel is $\ell(a)$ by definition; its image is $\{ax : x \in A\} = Aa$, which is a left ideal. The right statements are the mirror image, $\operatorname{im} R_a = \{xa\} = aA$, a right ideal.

**Corollary.** $L_a$ is injective exactly when $a$ is a left non-zero-divisor ($\ell(a) = 0$), and surjective exactly when $Aa = A$, that is, when $a$ has a left inverse. $L_a$ is invertible exactly when $a \in A^\times$, with $L_a^{-1} = L_{a^{-1}}$; likewise $R_a$ is invertible exactly when $a \in A^\times$, with $R_a^{-1} = R_{a^{-1}}$.

**Proof.** For invertibility, if $L_a$ is bijective then $a = L_a(1)$ has a left inverse by surjectivity and is not a zero divisor by injectivity, hence is a unit; conversely $L_aL_{a^{-1}} = L_{aa^{-1}} = L_1 = \mathrm{id}$. The right case is identical.

### The endomorphisms of the regular module

The two families are the two natural actions of $A$ and of its opposite on the additive group $A$, and the $A$-linear maps are exactly one of them.

**Proposition.** An additive map $T : A \to A$ commutes with every $L_a$ exactly when it is a right multiplication:

$$
\{T \in \operatorname{End}(A) : T L_a = L_a T \ \forall a\} = \{R_b : b \in A\} \cong A^{\mathrm{op}} .
$$

Dually, $\{T : T R_a = R_a T \ \forall a\} = \{L_b : b \in A\} \cong A$. The two-sided operators $L_aR_b$ generated by the families form the image of the multiplication map $A \otimes_{\mathbb{Z}} A^{\mathrm{op}} \to \operatorname{End}(A)$, whose surjectivity is the statement that the left and right multiplications are a complete set of operators.

**Proof.** If $T L_a = L_a T$ for all $a$, then $T(a) = T(L_a(1)) = L_a(T(1)) = a\,T(1)$, so $T = R_{T(1)}$. Conversely $R_b L_a = L_a R_b$ as shown. The second statement is the mirror, and the last is the definition of the map $a \otimes b \mapsto L_a R_b$.

**Remark.** This is the double centraliser theorem in its ring-of-multiplication form: the centraliser of one family is the other. It is the reason a two-sided operator requires **two** elements, and it is the algebraic reason the sandwich $x \mapsto axb$ is the general element of the algebra generated by the one-sided multiplications.

## Worked Cases

### A commutative ring

If $A$ is commutative then $L_a = R_a$ for every $a$, the two families coincide, and $a \mapsto L_a$ is an injective ring homomorphism $A \to \operatorname{End}(A)$. Every one-sided multiplication is a two-sided one, $[L_a,L_b] = L_{[a,b]} = 0$, and the two-sided operator reduces to $L_{ab}$. The operators $L_a$ are $A$-linear for the $A$-module structure of $A$, and the map is the regular representation of the commutative ring.

### The matrix ring

In $A = M_n(k)$ with matrix units $E_{ij}$, the left multiplication $L_{E_{ij}}$ has $L_{E_{ij}}(E_{kl}) = E_{ij}E_{kl} = \delta_{jk}E_{il}$, so it moves the $i$-th row onto the $j$-th row and kills the matrix units that miss $j$. The right multiplication $R_{E_{ij}}(E_{kl}) = E_{kl}E_{ij} = \delta_{li}E_{kj}$ moves the $j$-th column onto the $i$-th column. Already for $n = 2$ and the matrices $E_{12}, E_{21}$,

$$
[L_{E_{12}}, L_{E_{21}}] = L_{E_{12}E_{21} - E_{21}E_{12}} = L_{E_{11} - E_{22}},
$$

which is nonzero, so the left multiplications of the matrix ring do not commute; the commutator register records $[E_{12}, E_{21}] = E_{11} - E_{22}$, an element of trace $0$ and not a scalar.

### The polynomial ring

In $A = R[x]$ over a commutative ring $R$, the left multiplication $L_x$ is the operator of multiplication by $x$, and $L_{x^n}$ is multiplication by $x^n$. The operators $L_{x^n}$, $n \geq 0$, form a commutative family generating the image of $R[x]$ in $\operatorname{End}_R(R[x])$; the map $a \mapsto L_a$ is here the injective regular representation of a commutative ring, and no commutator is nonzero.

## Summary

For $a$ in the ring $A$ the one-sided multiplications are $L_a(x) = ax$ and $R_a(x) = xa$. They are additive, take the unit to $a$, and compose as $L_{ab} = L_aL_b$ and $R_{ab} = R_bR_a$: the left family is a unital ring homomorphism $A \to \operatorname{End}(A)$, the **left regular representation**, while the right family is one from the opposite ring and an anti-homomorphism from $A$. The two families commute, $L_aR_b = R_bL_a = (x \mapsto axb)$, and their pairwise commutators are the element commutator: $[L_a,L_b] = L_{[a,b]}$, $[R_a,R_b] = R_{[b,a]} = -R_{[a,b]}$, and $[L_a,R_b] = 0$. Thus the ring is commutative exactly when either family is commutative.

The kernel of $L_a$ is the left annihilator $\ell(a)$ and its image is the left ideal $Aa$; the kernel of $R_a$ is the right annihilator $r(a)$ and its image is the right ideal $aA$. Each is invertible exactly when $a$ is a unit, with inverse $L_{a^{-1}}$ or $R_{a^{-1}}$. The centraliser of one family is the other, so the two-sided operators $L_aR_b$ are the general operators generated by the one-sided ones, and the sandwich of the next article is the member of this generated ring built from a single element. The matrix and polynomial cases exhibit the two extremes: the matrix ring has non-commuting one-sided operators and the commutator register is nonzero, while the commutative polynomial ring has commuting ones.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A$ | Ring with $1 \neq 0$, not assumed commutative |
| $L_a(x) = ax$ | Left multiplication by $a$ |
| $R_a(x) = xa$ | Right multiplication by $a$ |
| $L_{ab} = L_aL_b$, $R_{ab} = R_bR_a$ | Composition laws; $L$ is a homomorphism, $R$ an anti-homomorphism |
| $L_aR_b = R_bL_a$ | The two families commute; the two-sided operator $x \mapsto axb$ |
| $[a,b] = ab - ba$ | Commutator in the ring |
| $[L_a,L_b] = L_{[a,b]}$, $[R_a,R_b] = -R_{[a,b]}$ | Commutation up to the commutator |
| $\ell(a)$, $r(a)$ | Left and right annihilators; kernels of $L_a$ and $R_a$ |
| $Aa$, $aA$ | Left and right ideals generated by $a$; images of $L_a$ and $R_a$ |
| $\{L_a\}' = \{R_b\}$ | The centraliser of one family is the other |
| $A^{\mathrm{op}}$ | Opposite ring; $a \mapsto R_a$ is a representation of it |
| $A^\times$ | Unit group; $L_a$ invertible iff $a \in A^\times$ |

## Further Reading

- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced Mathematics 50 (Cambridge University Press, 1995), for the one-sided multiplications and the regular representations.
- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for the left and right regular representations, the annihilators and the ideals they generate.
- Tsi-Yuen Lam, *A First Course in Noncommutative Rings*, Graduate Texts in Mathematics 131 (Springer, 2nd ed. 2001), for the opposite ring and the embedding of a ring in its endomorphism ring.
- Nathan Jacobson, *Structure of Rings*, American Mathematical Society Colloquium Publications 37 (1956), for the double centraliser theorem and the operators generated by the regular representations.
