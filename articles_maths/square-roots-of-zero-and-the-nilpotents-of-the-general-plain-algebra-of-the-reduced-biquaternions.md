# __Square Roots of Zero and the Nilpotents of the General Plain Algebra of the Reduced Biquaternions__

## Introduction

This article reads the roots of zero and the nilpotents of the multiplication and of the four general products. For the **multiplication** the result is an **absence**: the only element with $T^{2}=0$ is $T=0$, and there is **no nonzero nilpotent**, because the algebra is reduced. The algebra is the direct product $\mathbb{C}\Pi_{1}\oplus\mathbb{C}\Pi_{2}$ of two fields and has no nilpotent elements beyond $0$; its radical is trivial.

The higher products are read **product by product**, because the roots of zero of a product depend on the product and not on the space. The results are:
$$
TW=0\ \text{on}\ T=W \iff T=0,\qquad
T^{\natural}T=0 \iff T\in\mathbb{C}\Pi_{1}\cup\mathbb{C}\Pi_{2},
$$
$$
TT^{*}=0 \iff T\in\mathbb{C}\Pi_{1}\cup\mathbb{C}\Pi_{2},\qquad
T^{\natural}T^{*}=0 \iff T=0 .
$$
The two **bilinear** products split: the general plain bilinear product has no nonzero square-zero element, and the general quaternionic bilinear product has the two idempotent lines. The two **sesquilinear** products split the other way: the general plain sesquilinear product has the two lines, and the general quaternionic sesquilinear product has none. The two lines are the **same** set for every one of the three products that have a nonzero square-zero element, namely the null cone of the reduced norm.

**The results.** The roots of zero of the multiplication are $\{0\}$, and the multiplication has no nonzero nilpotent; the algebra is **reduced**, its nilradical and its Jacobson radical are $\{0\}$, and it is semisimple. The quaternionic bilinear product and the plain sesquilinear product each have the two idempotent lines as their nonzero square-zero set, and each is **nilpotent of index two** on those lines. The quaternionic sesquilinear product has no nonzero square-zero element, and its nilpotents are the two lines with **index three**: $T^{\star2}\neq0$ and $T^{\star3}=0$ for a nonzero element of a line. The plain bilinear product is the multiplication and has none.

**Boundaries.** The four products and their forms and norms are *The Four Products, Their Forms and Their Algebraic Norms*, above this article in this category; the multiplication and its axioms are *Introduction to the General Plain Algebra of the Reduced Biquaternions*; the zero divisors and the two lines are *Zero Divisors of the General Plain Algebra of the Reduced Biquaternions*, above this article; and the idempotents are *Square Roots of One and the Idempotents of the General Plain Algebra of the Reduced Biquaternions*, above this article. The nilpotent glyph of the reduced biquaternion layer, the plain capital of *Conventions in Mathematics*, §*The Nilpotents*, is not used here because there is no nilpotent to name in the multiplication; the products of the biquaternion layer with their two nilpotent families are *Square Roots of Zero and the Nilpotents of the Biquaternion Algebra*.

## The Roots of Zero of the Multiplication

### The Equation and the Single Root

**The equation $T^{2}=0$ has exactly one solution, $T=0$, in the multiplication.**

**Theorem (the roots of zero).** The solutions of $T^{2}=0$ in the multiplication are the single element $T=0$.

*Proof.* In the idempotent coordinates $T=(q_1,q_2)$ the product is componentwise, so $T^{2}=(q_1^{2},q_2^{2})$ (*Introduction to the General Plain Algebra of the Reduced Biquaternions*). The equation $T^{2}=0$ is the pair $q_1^{2}=0$, $q_2^{2}=0$; a complex number of square zero is $0$, so $q_1=q_2=0$ and $T=0$.

**Corollary (the two lines are not roots of zero of the multiplication).** The nonzero elements of the two idempotent lines are zero divisors, $2A\Pi_{1}\cdot\Pi_{2}=0$, but they are not square-zero: $(2A\Pi_{1})^{2}=4A^{2}\Pi_{1}\neq0$ for $A\neq0$.

### The Algebra Is Reduced

**The multiplication has no nonzero nilpotent, the algebra is reduced, and its radical is trivial.**

**Definition.** An element $T$ is **nilpotent** if some power vanishes, $T^{n}=0$ for some $n\geq1$; the **nilradical** is the set of the nilpotent elements, and the algebra is **reduced** if its only nilpotent is $0$.

**Theorem (the algebra is reduced and semisimple).** The multiplication has no nonzero nilpotent; the nilradical is $\{0\}$ and the Jacobson radical is $\{0\}$; the algebra is semisimple, being a direct product of two fields.

*Proof.* The multiplication is commutative and associative, and the algebra is the direct product $\mathbb{C}\Pi_{1}\oplus\mathbb{C}\Pi_{2}$ of two fields (*Reduced Biquaternion Space*); in a direct product of fields an element is nilpotent iff both coordinates are nilpotent, and a field has no nonzero nilpotent, so the coordinates vanish and the element is $0$. A commutative algebra that is a direct product of fields is semisimple, and its Jacobson radical is the intersection of the maximal ideals, which is $\mathbb{C}\Pi_{1}\cap\mathbb{C}\Pi_{2}=\{0\}$ (*Zero Divisors of the General Plain Algebra of the Reduced Biquaternions*, §*The Maximal Ideals*).

**Remark (the reduction is the structure).** The absence of nilpotents is not an accident of the coefficients: the algebra is a direct product of two copies of the field $\mathbb{C}$, hence reduced for every coefficient field, and the two squares of a general element are read componentwise. The idempotent coordinates are the reason: squaring is squaring in each coordinate, and $\mathbb{C}$ has no nilpotent.

## The Roots of Zero of the Four Products

### The Tables

**The square-zero set and the nilpotent set of each of the four products are the ones of the table below.**

For a product $\star$ the **square-zero set** is $\{T:T\star T=0\}$ and the **nilpotent set** is the set of elements some left-nested power of which vanishes, $T^{\star n}=0$ with $T^{\star(n+1)}=(T^{\star n})\star T$. The results are:

| product | square-zero set | nilpotent set | nilpotency index |
|---|---|---|---|
| general plain bilinear ($TW$) | $\{0\}$ | $\{0\}$ | none |
| general quaternionic bilinear ($T^{\natural}W$) | $\mathbb{C}\Pi_{1}\cup\mathbb{C}\Pi_{2}$ | $\mathbb{C}\Pi_{1}\cup\mathbb{C}\Pi_{2}$ | $2$ |
| general plain sesquilinear ($TW^{*}$) | $\mathbb{C}\Pi_{1}\cup\mathbb{C}\Pi_{2}$ | $\mathbb{C}\Pi_{1}\cup\mathbb{C}\Pi_{2}$ | $2$ |
| general quaternionic sesquilinear ($T^{\natural}W^{*}$) | $\{0\}$ | $\mathbb{C}\Pi_{1}\cup\mathbb{C}\Pi_{2}$ | $3$ |

**Theorem (the plain bilinear product and the quaternionic sesquilinear product).** The multiplication $TW$ has square-zero set $\{0\}$, and the quaternionic sesquilinear product $T^{\natural}W^{*}$ has square-zero set $\{0\}$ as well.

*Proof.* The multiplication is the theorem of the previous section. For the quaternionic sesquilinear product, the diagonal is
$$
T^{\natural}T^{*}=(|A|^{2}+|B|^{2})-\bigl(A\bar B+B\bar A\bigr)j,
$$
so $T^{\natural}T^{*}=0$ requires $|A|^{2}+|B|^{2}=0$, which forces $A=B=0$; hence $T=0$.

**Theorem (the quaternionic bilinear product and the plain sesquilinear product).** The quaternionic bilinear product $T^{\natural}W$ and the plain sesquilinear product $TW^{*}$ have the same nonzero square-zero set, the two idempotent lines
$$
\bigl\{T\neq0:T^{\natural}T=0\bigr\}=\mathbb{C}^{\times}\Pi_{1}\cup\mathbb{C}^{\times}\Pi_{2}=\bigl\{T\neq0:TT^{*}=0\bigr\}=\mathcal{N},
$$
the null cone of the reduced norm.

*Proof.* $T^{\natural}T=(A^{2}-B^{2})+0\cdot j$, a scalar, so $T^{\natural}T=0$ iff $A^{2}=B^{2}$, which is the null cone $\mathcal{N}$ (*Zero Divisors of the General Plain Algebra of the Reduced Biquaternions*). For the plain sesquilinear product,
$$
TT^{*}=(|A|^{2}-|B|^{2})+\bigl(-A\bar B+B\bar A\bigr)j,
$$
and this vanishes iff $|A|^{2}=|B|^{2}$ and $A\bar B=B\bar A$. The two conditions force $B=\pm A$: writing $A=|A|\exp(i\alpha)$ and $B=|B|\exp(i\beta)$, the first gives $|A|=|B|$ and the second gives $\exp(i(\alpha-\beta))=\pm1$, that is $B=\pm A$, which is the null cone $\mathcal{N}$ again. Conversely $B=A$ gives $|A|^{2}-|A|^{2}=0$ and $-A\bar A+A\bar A=0$, and $B=-A$ gives $-A(-\bar A)+(-A)\bar A=0$, so both lines are square-zero.

### The Two Products Split Differently

**The bilinear pair and the sesquilinear pair split in opposite ways: the plain bilinear product has no square-zero element while the quaternionic bilinear product has the lines, and the plain sesquilinear product has the lines while the quaternionic sesquilinear product has none.**

**Remark (the reading of the table).** The table is the exact analogue for the reduced biquaternion layer of the tables of the biquaternion layer, with one difference: over the non-commutative quaternions the two nilpotent families are larger, while here the whole nilpotent set of every non-associative product is the two idempotent lines. The two lines are the null cone of the reduced norm, and the three products that have a nonzero square-zero element have it on the same cone; the distinction is only the **index**, two for the two bilinear-or-plain cases and three for the quaternionic sesquilinear one.

## The Nilpotents

### The Multiplication Has None

**The multiplication has no nonzero nilpotent: its nilpotent set is $\{0\}$.**

*Proof.* An element is nilpotent in the multiplication iff some $T^{n}=0$; in the idempotent coordinates $T^{n}=(q_1^{n},q_2^{n})$, and $q_1^{n}=q_2^{n}=0$ iff $q_1=q_2=0$; so the only nilpotent is $0$. The statement is the one of §*The Algebra Is Reduced*, and it is repeated here because the article reads the nilpotents of all four products.

### The Nilpotents of the Non-Associative Products

**The two products of index two are the quaternionic bilinear product and the plain sesquilinear product, on the two lines; the quaternionic sesquilinear product is of index three on the two lines; and the plain bilinear product has none.**

**Theorem (index two).** For every nonzero element of the null cone,
$$
T\in\mathcal{N}\ \Longrightarrow\ T^{\natural}T=0\quad\text{and}\quad TT^{*}=0,
$$
so the quaternionic bilinear product and the plain sesquilinear product are nilpotent of index two on the cone.

*Proof.* Both square-zero sets are the cone by the theorems above; an element whose square vanishes has every left-nested higher power vanishing as well, so the index is two.

**Theorem (index three of the quaternionic sesquilinear product).** For $T=2A\Pi_{1}$ with $A\neq0$,
$$
T^{\natural}T^{*}\neq0,\qquad (T^{\natural}T^{*})^{\natural}T^{*}=0,
$$
and likewise for $T=2A\Pi_{2}$; the quaternionic sesquilinear product has nilpotency index three on the two lines and no nilpotent outside them.

*Proof.* Write $T=A(1+j)=2A\Pi_{1}$. Then $T^{\natural}=A(1-j)=2A\Pi_{2}$ and $T^{*}=\bar A(1-j)=2\bar A\Pi_{2}$, so
$$
T^{\natural}T^{*}=A(1-j)\bar A(1-j)=|A|^{2}(1-j)^{2}=2|A|^{2}(1-j)\neq0,
$$
a nonzero element of the second idempotent line. The next power is $(T^{\natural}T^{*})^{\natural}T^{*}$: the natural sign of $2|A|^{2}(1-j)$ is $2|A|^{2}(1+j)$, and its product with $T^{*}=\bar A(1-j)$ is $2|A|^{2}\bar A(1+j)(1-j)=2|A|^{2}\bar A(1-j^{2})=0$. So the index is three. Outside the two lines both idempotent coordinates $q_1=A+B$ and $q_2=A-B$ are nonzero, and in the idempotent coordinates the product reads $(x_{1},x_{2})\star(w_{1},w_{2})=(x_{2}\bar w_{2},\,x_{1}\bar w_{1})$, so the left-nested powers obey $x_{n+1}=y_{n}\bar q_2$ and $y_{n+1}=x_{n}\bar q_1$; every coordinate of $T^{\star n}$ is a product of a power of $q_1$ or $q_2$ with a conjugate power, hence nonzero, and no power vanishes.

**Corollary (the nilpotent set of every product is the two lines).** For the three products that have a nonzero nilpotent, the nilpotent set is the null cone $\mathbb{C}\Pi_{1}\cup\mathbb{C}\Pi_{2}$, and the nilpotency index is the one of the table; the multiplication has no nonzero nilpotent.

**Remark (the glyph).** The nilpotents of the reduced biquaternion layer carry, in the convention of *Conventions in Mathematics*, §*The Nilpotents*, the plain capital and **no tilde**; but the only nilpotents here lie on the two idempotent lines and are already named by the idempotents, so this article names none of them and reads them as the cone.

## The Radical

**The radical of the multiplication is trivial: the Jacobson radical is $\{0\}$ and the algebra is semisimple.**

**Theorem (the radical).** The Jacobson radical of the algebra is
$$
\operatorname{rad}\mathbb{B}_{\mathrm{r}}=\{0\},
$$
and the algebra is semisimple and Artinian.

*Proof.* The radical of a commutative ring is the intersection of its maximal ideals; the maximal ideals are the two idempotent lines (*Zero Divisors of the General Plain Algebra of the Reduced Biquaternions*), and their intersection is $\{0\}$ because they meet only at the origin. The algebra is a direct product of two fields, hence Artinian and semisimple.

**Remark (reduced against radical).** The absence of nilpotents and the triviality of the radical are the same fact here, because the algebra is commutative and a direct product of fields; both are read from the two coordinates, and both contrast with the biquaternion layer, whose algebra is simple with nilpotent elements and a nontrivial theory of nilpotents.

## Summary

The roots of zero of the multiplication are the single element $T=0$; the multiplication has **no nonzero nilpotent**, the algebra is **reduced**, its nilradical and its Jacobson radical are $\{0\}$, and it is semisimple, being the direct product $\mathbb{C}\Pi_{1}\oplus\mathbb{C}\Pi_{2}$ of two fields. Read product by product, the four general products give:

| product | square-zero set | nilpotent set | index |
|---|---|---|---|
| general plain bilinear ($TW$) | $\{0\}$ | $\{0\}$ | none |
| general quaternionic bilinear ($T^{\natural}W$) | the two lines | the two lines | $2$ |
| general plain sesquilinear ($TW^{*}$) | the two lines | the two lines | $2$ |
| general quaternionic sesquilinear ($T^{\natural}W^{*}$) | $\{0\}$ | the two lines | $3$ |

The two **bilinear** products split in opposite ways — the plain one has no nonzero square-zero element, $T^{\natural}T=A^{2}-B^{2}$ being a scalar vanishing only on the cone, and the quaternionic one has the cone — and the two **sesquilinear** products split the other way — the plain one has the cone, $TT^{*}=(|A|^{2}-|B|^{2})+(-A\bar B+B\bar A)j$ vanishing only at $B=\pm A$, and the quaternionic one has none, since $T^{\natural}T^{*}$ has scalar part $|A|^{2}+|B|^{2}$. Every nonzero nilpotent of every product lies on the null cone $\mathbb{C}\Pi_{1}\cup\mathbb{C}\Pi_{2}$, at index two for the quaternionic bilinear and the plain sesquilinear products and at index three for the quaternionic sesquilinear product.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $T^{2}=0$ | the root-of-zero equation of the multiplication, with the single solution $T=0$ |
| $T^{\natural}T=A^{2}-B^{2}$ | the diagonal of the quaternionic bilinear product, vanishing on the two lines |
| $TT^{*}=(\lvert A\rvert^{2}-\lvert B\rvert^{2})+(-A\bar B+B\bar A)j$ | the diagonal of the plain sesquilinear product, vanishing on the two lines |
| $T^{\natural}T^{*}=(\lvert A\rvert^{2}+\lvert B\rvert^{2})-(A\bar B+B\bar A)j$ | the diagonal of the quaternionic sesquilinear product, vanishing only at $0$ |
| $\mathbb{C}\Pi_{1}\cup\mathbb{C}\Pi_{2}$ | the nilpotent set of every product that has one, the null cone |
| index $2$, index $3$ | the nilpotency index of the non-associative products |
| $\operatorname{rad}\mathbb{B}_{\mathrm{r}}=\{0\}$ | the trivial radical, the semisimplicity |

## Further Reading

- *The Four Products, Their Forms and Their Algebraic Norms* (`articles_maths/the-four-products-their-forms-and-their-algebraic-norms-of-the-reduced-biquaternions.md`), above this article in this category, for the four products and their diagonals.
- *Introduction to the General Plain Algebra of the Reduced Biquaternions* (`articles_maths/introduction-to-the-general-plain-algebra-of-the-reduced-biquaternions.md`), above this article, for the algebra, its product and its structure as a direct product of two fields.
- *Zero Divisors of the General Plain Algebra of the Reduced Biquaternions* (`articles_maths/zero-divisors-of-the-general-plain-algebra-of-the-reduced-biquaternions.md`), above this article, for the null cone and the maximal ideals.
- *Square Roots of One and the Idempotents of the General Plain Algebra of the Reduced Biquaternions* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-general-plain-algebra-of-the-reduced-biquaternions.md`), above this article, for the idempotents and the projections.
- *Conventions in Mathematics* (`articles_maths/conventions-in-mathematics.md`), §*The Nilpotents*, for the glyph of the nilpotent of the layer.
- *Square Roots of Zero and the Nilpotents of the Biquaternion Algebra* (`articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-biquaternion-algebra.md`), the non-commutative counterpart, for the two nilpotent families of the larger algebra.
- *Dual-Numbers Zero Divisors* (`articles_maths/dual-numbers-zero-divisors.md`), for the companion with nonzero square-zero elements, the dual numbers, whose imaginary line is square-zero.
