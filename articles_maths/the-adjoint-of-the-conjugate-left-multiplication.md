# __The Adjoint of the Conjugate Left Multiplication__

## Introduction

The sesquilinear product attaches two one-sided operators to an element, the right multiplication $R_{b}(x)=x\star b=xb^{*}$ and the left multiplication $L_{a}(x)=a\star x=ax^{*}$, and the two are not of the same kind: the right multiplication is $R$-linear, while the left multiplication is $\varsigma$-semilinear, because it is the second slot of the product that meets the involution and exports the conjugate of the scalar. The present article studies the adjoint of the conjugate-linear one, and it does so for the sesquilinear pairing $\varphi(x,y)=\tau(xy^{*})$ of *The Sesquilinear Adjoint Operator*. The operator $L_{a}$, for $a\neq0$, is $R$-linear exactly when the base involution $\varsigma$ is trivial, and in the general case it has no adjoint under the linear rule; the adjoint it does have is taken by the twisted rule of the conjugate-linear operators, and it is the sandwich $S_{1,a}$ of *The Sesquilinear Sandwich Operator*, not another one-sided multiplication. The article computes that adjoint, the products the operator forms with its adjoint, the elements for which the operator is self-adjoint, the unitary case, and the two degenerations of the involution.

The subject belongs to the operator theory of the sesqualgebras, and its point is the asymmetry of the two slots. The right multiplication and the left multiplication are the two ways an element acts on the algebra, and the adjoint separates them: the right multiplication is met by the linear rule and is adjoint to another right multiplication, while the left multiplication is met by the twisted rule and is adjoint to a sandwich. The family of the one-sided operators is therefore not stable under the adjoint, and the products $L_{a}^{\dagger}L_{b}$ and $L_{b}L_{a}^{\dagger}$ are the plain one-sided operators, the right and the left regular families of the ordinary product. That is the content of the article.

**The boundaries.** The pairing, the parity obstruction, the twisted rule and the two adjoints are *The Sesquilinear Adjoint Operator*; the sandwich is *The Sesquilinear Sandwich Operator*; the left and right multiplication operators and the plain two-sided operator $T_{p,q}$ are *The Left and Right Multiplication Operators of a Sesqualgebra*; the unitary elements are *Units and the Unitary Elements*; the ternary operator attached to a pair is *The Ternary Product as an Operator* and its adjoint is *The Adjoint of the Ternary Product*; the operators that preserve the product are *The Unitary Operators of a Sesqualgebra*, the later entry of the group. This article stays inside Part I: no distance, no limit, no completeness.

Throughout, $R$ is a commutative ring with $1$ without zero divisors, $\varsigma$ is an involution of $R$, and $A$ is a unital associative $R$-algebra with a $\varsigma$-semilinear involution $*$, so that $A$ is a sesqualgebra in the sense of *Sesqualgebras*; the unit satisfies $1^{*}=1$. The function $\tau:A\to R$ is $R$-linear, central, compatible with the involution, $\tau(ab)=\tau(ba)$ and $\tau(x^{*})=\varsigma(\tau(x))$, and the pairing is $\varphi(x,y)=\tau(xy^{*})$, $R$-linear in its first variable, $\varsigma$-semilinear in its second and perfect. The derived product is $x\star y=xy^{*}$, and the operators are

$$
L_{a}(x)=a\star x=ax^{*}, \qquad R_{b}(x)=x\star b=xb^{*}, \qquad S_{a,b}(x)=ax^{*}b, \qquad T_{p,q}(x)=pxq .
$$

The adjoint of a $\varsigma$-semilinear operator $S$ is the operator $S^{\dagger}$ with $\varphi(Sx,y)=\varsigma\bigl(\varphi(x,S^{\dagger}y)\bigr)$, and the adjoint of an $R$-linear operator $T$ is the operator $T^{\dagger}$ with $\varphi(Tx,y)=\varphi(x,T^{\dagger}y)$; both exist and are unique, as *The Sesquilinear Adjoint Operator* proves.

## The Conjugate Left Multiplication

### The Operator and its Parity

**Definition.** For $a\in A$ the **conjugate left multiplication** by $a$ is the operator

$$
L_{a}:A\longrightarrow A,\qquad L_{a}(x)=a\star x=ax^{*} .
$$

**Proposition (the operator and its parity).** $L_{a}$ is $\varsigma$-semilinear, $L_{a}(\lambda x)=\varsigma(\lambda)L_{a}(x)$; it satisfies $L_{a}(1)=a$; it vanishes identically if and only if $a=0$; and the assignment $a\mapsto L_{a}$ is $R$-linear,

$$
L_{\lambda a}=\lambda L_{a}, \qquad L_{a+b}=L_{a}+L_{b} .
$$

**Proof.** For the parity, $L_{a}(\lambda x)=a(\lambda x)^{*}=a\,\varsigma(\lambda)\,x^{*}=\varsigma(\lambda)ax^{*}=\varsigma(\lambda)L_{a}(x)$, by the scalar rule of the involution. At the unit, $L_{a}(1)=a1^{*}=a$, so $L_{a}=0$ forces $a=0$, and conversely $a=0$ gives the zero operator. The two linearity laws are the distributivity and the $R$-linearity of the product in its first slot. $\square$

**Remark.** The failure of linearity is the scalar defect of the second slot: for $a\neq0$ the operator $L_{a}$ is $R$-linear if and only if $\varsigma=\mathrm{id}$. The general criterion of *Sesqualgebras* for the sesquilinear product keeps the alternative $(\lambda-\varsigma(\lambda))ax=0$ for all $\lambda$ and $x$; the hypotheses here remove it, because the evaluation at $x=1$ gives $(\varsigma(\lambda)-\lambda)a=0$, and a nonzero value of $\varsigma(\lambda)-\lambda$ would force $a=0$: the ring has no zero divisors, and the algebra is torsion-free, a torsion element of $A$ lying in the radical of the perfect pairing. The right multiplication $R_{b}(x)=xb^{*}$ is $R$-linear in every case, because the variable enters the first slot and the parameter the second; the asymmetry of the two slots of the product is therefore visible in the two operators already, before any adjoint is taken.

**Remark.** The assignment $a\mapsto L_{a}$ is $R$-linear and injective, so the algebra $A$ sits as an $R$-submodule of the $\varsigma$-semilinear operators on $A$; it is not a subalgebra of the endomorphism algebra, because the composite of two conjugate-linear operators is $R$-linear, and the composite of two conjugate left multiplications is the plain two-sided operator $L_{a}L_{b}=T_{a,b^{*}}$, $x\mapsto axb^{*}$. The family of the left multiplications is a copy of $A$ as an $R$-module, and its composites leave the family for the plain two-sided operators.

### The Single-Slot Adjoint that it has not

**Proposition (the parity obstruction, the case of $L_{a}$).** Let $\varsigma\neq\mathrm{id}$ and let $a\neq0$. Then there is no $R$-linear operator $U$ with

$$
\varphi(L_{a}x,y)=\varphi(x,Uy)\qquad\text{for all }x,y\in A .
$$

**Proof.** Suppose there is one, and replace $x$ by $\lambda x$ in the identity. On the left, $\varphi\bigl(L_{a}(\lambda x),y\bigr)=\varphi\bigl(\varsigma(\lambda)L_{a}x,y\bigr)=\varsigma(\lambda)\varphi(L_{a}x,y)$; on the right, $\varphi(\lambda x,Uy)=\lambda\varphi(x,Uy)=\lambda\varphi(L_{a}x,y)$. Hence $\bigl(\varsigma(\lambda)-\lambda\bigr)\varphi(L_{a}x,y)=0$ for every $\lambda$, $x$ and $y$. Choosing $\lambda$ with $\varsigma(\lambda)\neq\lambda$, which is possible because $\varsigma\neq\mathrm{id}$ and which is a non-zero-divisor by the hypothesis on $R$, gives $\varphi(L_{a}x,y)=0$ for all $x$ and $y$; since $a\neq0$ the operator $L_{a}$ does not vanish, and the perfection of the pairing supplies $y$ with $\varphi(L_{a}x,y)\neq0$ for some $x$, a contradiction. $\square$

**Remark (why the ring has no zero divisors).** The proof cancels $\varsigma(\lambda)-\lambda$, and that step is not idle: over $R=\mathbb{Q}[\varepsilon]/(\varepsilon^{2})$ with $\varsigma(\varepsilon)=-\varepsilon$, $A=M_{2}(R)$ with $X^{*}=\varsigma(X)^{T}$ and $\tau$ the trace, the pairing is perfect and $L_{a}$ for $a=\varepsilon E_{11}$ has the $R$-linear adjoint $U(Y)=-\varepsilon Y^{T}E_{11}$ beside its twisted adjoint $S_{1,a}$: for every $\lambda$ the difference $\varsigma(\lambda)-\lambda$ annihilates the image of $L_{a}$, so the argument has nothing to cancel. The same hypothesis is used in the criterion for $R$-linearity, which evaluates at the unit: there a zero divisor of $R$ lets $(\varsigma(\lambda)-\lambda)a$ vanish although $\varsigma(\lambda)\neq\lambda$ and $a\neq0$.

**Remark.** The witness of the failure is the unit: $\varphi(L_{a}1,1)=\tau(a)$, and the defect $\bigl(\varsigma(\lambda)-\lambda\bigr)\tau(a)$ is the obstruction in its smallest form. The single-slot adjoint that the operator does not have is the one the right multiplication does have, and the reason is the parity: a conjugate-linear operator exports the scalar $\varsigma(\lambda)$ and a linear rule imports the scalar $\lambda$, so the two can agree only if the two scalars are the same.

## The Twisted Adjoint

### The Adjoint of the Operator

**Theorem (the adjoint of the conjugate left multiplication).** For every $a\in A$ the operator $L_{a}$ has the adjoint

$$
L_{a}^{\dagger}=S_{1,a},\qquad L_{a}^{\dagger}(y)=y^{*}a .
$$

The adjoint is $\varsigma$-semilinear, it is a sandwich and not a one-sided multiplication, and it is a left multiplication $L_{a}$ again exactly when $a$ is central.

**Proof.** The defining identity is $\varphi(L_{a}x,y)=\varsigma\bigl(\varphi(x,L_{a}^{\dagger}y)\bigr)$, and for the candidate $L_{a}^{\dagger}(y)=y^{*}a$ the right-hand side is $\varsigma\bigl(\tau(x(y^{*}a)^{*})\bigr)=\varsigma\bigl(\tau(xa^{*}y)\bigr)=\tau\bigl((xa^{*}y)^{*}\bigr)=\tau(y^{*}ax^{*})=\tau(ax^{*}y^{*})$, using the anti-multiplicativity of $*$ and the compatibility of $\tau$; the cyclicity of $\tau$ turns the last expression into $\tau(ax^{*}y^{*})=\varphi(L_{a}x,y)$, which is the identity. The operator is $\varsigma$-semilinear by its definition, and the sandwich $S_{1,a}$ is a left multiplication $L_{c}$ only if $y^{*}a=cy^{*}$ for all $y$, that is only if $a=c$ is central. $\square$

**Corollary (the order of the operation).** $L_{a}^{\dagger\dagger}=L_{a}$; the adjoint operation is an order-two map on the union of the left regular family with the sandwiches $S_{1,a}$.

**Proof.** The adjoint is an involution on the $\varsigma$-semilinear operators, as the general theory records, and $S_{1,a}^{\dagger}=S_{a,1}=L_{a}$, since $S_{a,1}(y)=ay^{*}=L_{a}(y)$; the two families $\{L_{a}\}$ and $\{S_{1,a}\}$ are therefore exchanged, and exchanged back. $\square$

**Remark.** The adjoint of the conjugate left multiplication is not one-sided, and that is a genuine loss of the family: the right multiplication is adjoint to another right multiplication, $R_{b}^{\dagger}=R_{b^{*}}$, while the left multiplication does not stay in it. The two slots are met differently by the adjoint, exactly as they are met differently by the product.

### The Two Adjoints Coincide

**Theorem (the left and the right adjoint).** For every $a$ the left adjoint ${}^{\dagger}L_{a}$ of $L_{a}$ for the transposed pairing is the right adjoint,

$$
{}^{\dagger}L_{a}=L_{a}^{\dagger}=S_{1,a} .
$$

**Proof.** The two adjoints are the adjoint taken against $\varphi$ and against $\varphi^{T}$, and for the sesqui-symmetric pairing $\varphi^{T}=\varsigma\circ\varphi$ makes them agree, as *The Sesquilinear Adjoint Operator* proves. $\square$

**Remark.** The coincidence is the reason a single symbol $\dagger$ serves. It is not a general fact about pairings: for a pairing that is not sesqui-symmetric the two adjoints differ, and the difference is the sesquilinear analogue of the defect that separates the adjoint from the left adjoint of the bilinear case.

## The Products with an Adjoint

### The Right and the Left Regular Families

The composite of a conjugate-linear operator with its adjoint is linear, so the products of $L$ and $L^{\dagger}$ are $R$-linear operators, and they are plain one-sided operators of the ordinary product.

**Theorem (the products).** For all $a,b\in A$,

$$
L_{a}^{\dagger}L_{b}=R_{a^{*}b}, \qquad L_{b}L_{a}^{\dagger}=T_{ba^{*},1} .
$$

**Proof.** For the first, $(L_{a}^{\dagger}L_{b})(x)=L_{a}^{\dagger}(bx^{*})=(bx^{*})^{*}a=xb^{*}a$, and the right multiplication with parameter $a^{*}b$ is $R_{a^{*}b}(x)=x(a^{*}b)^{*}=xb^{*}a$. For the second, $(L_{b}L_{a}^{\dagger})(x)=L_{b}(x^{*}a)=b(x^{*}a)^{*}=ba^{*}x=T_{ba^{*},1}(x)$. $\square$

**Remark.** The products are the plain one-sided operators: the derived product does not appear, because the two conjugate-linear factors contribute the star that cancels. The first product is a right multiplication and the second a plain left multiplication, so the composite of the adjoint pair fills the two one-sided families that the derived product itself does not produce from the pairs; the contrast with the conjugate left multiplication, which is derived and not plain, is the whole content of the two displays.

### The Square of the Operator

**Theorem (the two squares).** For every $a\in A$,

$$
L_{a}^{\dagger}L_{a}=R_{a^{*}a}, \qquad L_{a}L_{a}^{\dagger}=T_{aa^{*},1} .
$$

Both squares are self-adjoint, and both are the identity when $a$ is unitary.

**Proof.** The two identities are the theorem above at $b=a$. For the self-adjointness, $R_{c}^{\dagger}=R_{c^{*}}$, so $R_{a^{*}a}^{\dagger}=R_{(a^{*}a)^{*}}=R_{a^{*}a}$; and $T_{p,q}^{\dagger}=T_{p^{*},q^{*}}$, so $T_{aa^{*},1}^{\dagger}=T_{(aa^{*})^{*},1}=T_{aa^{*},1}$, since $aa^{*}$ is Hermitian. If $aa^{*}=a^{*}a=1$ then $R_{a^{*}a}=R_{1}=\mathrm{id}$ and $T_{aa^{*},1}=T_{1,1}=\mathrm{id}$. $\square$

**Remark.** The two squares are different operators, a right multiplication by $a^{*}a$ and a plain left multiplication by $aa^{*}$, and the difference is the noncommutativity of $A$; both parameters are Hermitian, which is why both squares are self-adjoint, and the two squares are the identity exactly for the unitary elements.

**Corollary (the unitary case).** Let $a$ be unitary. Then $L_{a}$ is invertible, $L_{a}^{\dagger}=L_{a}^{-1}$, and $L_{a}$ satisfies the conjugate-linear analogue of the unitary condition $T^{\dagger}=T^{-1}$. The invertible conjugate-linear operators of this kind are the antiunitary operators of *The Unitary Operators of a Sesqualgebra*, the later entry of the group, and the conjugate left multiplications by the unitary elements are the antiunitary operators that the algebra itself supplies.

**Proof.** $L_{a}^{\dagger}L_{a}=L_{a}L_{a}^{\dagger}=\mathrm{id}$ makes $L_{a}$ invertible with inverse $L_{a}^{\dagger}$. The operator is conjugate-linear by its parity, and its adjoint is its inverse, which is the antiunitary condition of *The Unitary Operators of a Sesqualgebra*. $\square$

## The Self-Adjoint Elements

### The Criterion

**Theorem (which left multiplications are self-adjoint).** For $a\in A$ the operator $L_{a}$ is self-adjoint if and only if $a$ is central,

$$
L_{a}^{\dagger}=L_{a}\quad\Longleftrightarrow\quad a\in Z(A) .
$$

**Proof.** By the adjoint theorem $L_{a}^{\dagger}=S_{1,a}$, and $S_{1,a}=L_{a}$ means $y^{*}a=ay^{*}$ for every $y$. As $y$ runs over $A$ the elements $y^{*}$ run over $A$, so the condition is that $a$ commute with every element, that is $a$ central. $\square$

**Remark.** The criterion is the element-level statement of the asymmetry: a conjugate left multiplication is self-adjoint exactly when the element does not see the order, and otherwise its adjoint is a sandwich. On a commutative algebra every conjugate left multiplication is self-adjoint, and on a noncommutative one only the scalars are.

### The Worked Cases

**The complex matrices.** Let $A=M_{n}(\mathbb{C})$ with the conjugate transpose, $\varsigma$ the conjugation, $\tau$ the trace and $\varphi(X,Y)=\operatorname{tr}(XY^{*})$. The conjugate left multiplication is $L_{A}(X)=AX^{*}$, and

$$
L_{A}^{\dagger}(Y)=Y^{*}A, \qquad L_{A}^{\dagger}L_{B}=R_{A^{*}B}, \qquad L_{B}L_{A}^{\dagger}=T_{BA^{*},1} .
$$

The criterion reads $L_{A}^{\dagger}=L_{A}$ if and only if $A=\lambda 1$ is a scalar matrix, and a unitary $U$ gives the antiunitary $L_{U}(X)=UX^{*}$ with $L_{U}^{\dagger}=L_{U}^{-1}$. For $n=2$ and $A=E_{12}$ the adjoint is $L_{A}^{\dagger}(Y)=Y^{*}E_{12}$, which sends $Y=E_{11}$ to $E_{11}E_{12}=E_{12}$ and $Y=E_{12}$ to $E_{21}E_{12}=E_{22}$, while $L_{A}$ sends $E_{11}$ to $0$ and $E_{12}$ to $E_{11}$; the two operators differ, and the element $E_{12}$ is not central.

**The field.** Let $A=\mathbb{C}$ with $\varsigma$ the conjugation, $\tau$ the identity and $\varphi(x,y)=x\overline{y}$. The conjugate left multiplication is $L_{c}(x)=c\overline{x}$, its adjoint is $L_{c}^{\dagger}(y)=\overline{y}c=c\overline{y}=L_{c}(y)$, and every conjugate left multiplication is self-adjoint, the algebra being commutative. The assignment $c\mapsto L_{c}$ is an $R$-linear isomorphism of the field onto the conjugate-linear operators of the space, and the antiunitary operators of the field are exactly the multiplications by the complex numbers $c$ with $c\overline{c}=1$.

**The quaternions.** Let $A=\mathbb{H}$ over $R=\mathbb{R}$ with the quaternion conjugation and $\tau$ the real part, so that $\varsigma=\mathrm{id}$ and the twisted rule is the linear rule. The right multiplication is $R_{b}^{\dagger}=R_{b^{*}}$ and the left multiplication is $L_{a}^{\dagger}=S_{1,a}(y)=y^{*}a$, which is one-sided again only for real $a$, the central elements of the division algebra $\mathbb{H}$. The unitary elements are those with $qq^{*}=1$, and the conjugate left multiplication by such an element is antiunitary; since $\mathbb{H}$ is a division algebra, $L_{a}$ is injective for $a\neq0$.

## The Degenerations

### The Trivial Base Involution

When $\varsigma=\mathrm{id}$ the operator $L_{a}$ is $R$-linear, and the proposition of the parity obstruction says nothing: the scalar the operator exports and the scalar the linear rule imports are the same. The single-slot adjoint therefore exists, it is the same operator as the twisted adjoint, and the two adjoints of the general theory merge into one. The price is the involution of the algebra: $\varsigma=\mathrm{id}$ requires $(xy)^{*}=y^{*}x^{*}$ with $(\lambda x)^{*}=\lambda x^{*}$, that is an $R$-linear anti-automorphism of $A$, so the conjugate transpose of the matrix algebra, which is conjugate-linear over $\mathbb{C}$, is excluded and the transpose is the admissible involution. This is the bilinear case $\varsigma=\mathrm{id}$ of *Sesqualgebras*, where the derived product $x\star y=xy^{*}$ is $R$-bilinear, and there the statements of the article reduce to those of *The Adjoint in an Involutive Algebra* for the pairing read with $\sigma=*$.

### The Trivial Algebra Involution

The other degeneration is $*=\mathrm{id}$, and it is not independent: the identity is an anti-automorphism only on a commutative algebra, so $*=\mathrm{id}$ forces $A$ commutative, and then the scalar rule $(\lambda x)^{*}=\varsigma(\lambda)x^{*}$ reads $\lambda x=\varsigma(\lambda)x$, that is $\varsigma=\mathrm{id}$ as well. In that case the derived product is the ordinary product, $L_{a}(x)=ax$ is the plain left multiplication, the sandwich $S_{1,a}(y)=ya$ is the plain right multiplication, and

$$
L_{a}^{\dagger}=R_{a},\qquad \varphi(ax,y)=\tau(axy)=\tau(xay)=\varphi(x,ay) ,
$$

so every left multiplication is self-adjoint, in agreement with the criterion, every element being central. The two degenerations therefore meet, and the article collapses to the classical statement that the left and the right multiplication by an element of a commutative algebra are adjoint.

## Summary

The conjugate left multiplication $L_{a}(x)=a\star x=ax^{*}$ is the one-sided operator that the sesquilinear product attaches to the first slot, and it is $\varsigma$-semilinear while the right multiplication is $R$-linear. For $\varsigma\neq\mathrm{id}$ it has no adjoint under the linear rule, the obstruction being the parity mismatch $\varsigma(\lambda)-\lambda$ tested at the unit through $\tau(a)$; the adjoint it does have is taken by the twisted rule and is the sandwich $L_{a}^{\dagger}=S_{1,a}$, $y\mapsto y^{*}a$, so that the family of the one-sided operators is not stable under the adjoint. The composite of the operator with its adjoint is linear and plainly one-sided: $L_{a}^{\dagger}L_{b}=R_{a^{*}b}$ is a right multiplication and $L_{b}L_{a}^{\dagger}=T_{ba^{*},1}$ a plain left multiplication, the derived product disappearing in the composition. The two squares $L_{a}^{\dagger}L_{a}=R_{a^{*}a}$ and $L_{a}L_{a}^{\dagger}=T_{aa^{*},1}$ are self-adjoint and are the identity exactly for the unitary elements, where $L_{a}$ is an antiunitary operator. The operator is self-adjoint if and only if the element is central; on a commutative algebra every one is; and in the two degenerations of the involution the article becomes the classical adjointness of the left and the right multiplication.

## Summary of Notation

| symbol | meaning |
|---|---|
| $L_{a}(x)=ax^{*}$ | the conjugate left multiplication by $a$, $\varsigma$-semilinear |
| $R_{b}(x)=xb^{*}$ | the right multiplication by $b$, $R$-linear |
| $S_{a,b}(x)=ax^{*}b$ | the sandwich of the pair $(a,b)$ |
| $T_{p,q}(x)=pxq$ | the plain two-sided operator |
| $L_{a}^{\dagger}=S_{1,a}$ | the adjoint of the conjugate left multiplication, $y\mapsto y^{*}a$ |
| $L_{a}^{\dagger\dagger}=L_{a}$ | the adjoint operation is of order two |
| $L_{a}^{\dagger}L_{b}=R_{a^{*}b}$ | the right regular family from the adjoint pair |
| $L_{b}L_{a}^{\dagger}=T_{ba^{*},1}$ | the plain left regular family from the adjoint pair |
| $L_{a}^{\dagger}L_{a}=R_{a^{*}a}$, $L_{a}L_{a}^{\dagger}=T_{aa^{*},1}$ | the two self-adjoint squares |
| $L_{a}^{\dagger}=L_{a}\iff a\in Z(A)$ | the criterion of self-adjointness |
| $a$ unitary $\Rightarrow$ $L_{a}$ antiunitary | the unitary case |

## Further Reading

- Sterling K. Berberian, *Baer $\ast$-Rings* (Springer, 1972), for the adjoint operation in a ring with an involution, the module of the conjugate-linear operators and the trace pairing against which the adjoint is taken, which is the algebraic setting of the whole article.
- Nathan Jacobson, *Lectures in Abstract Algebra, Volume II: Linear Algebra* (Van Nostrand, 1953), for the adjoint of a linear operator against a trace form and the classical duality of the left and the right multiplication, the degeneration of the last section.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume I* (Academic Press, 1983), for the conjugate-linear operators, the two adjoints that a conjugate-linear operator requires and the unitary and antiunitary operators, treated there with the analysis the present article leaves to Part III.
- Sterling K. Berberian, *Lectures in Functional Analysis and Operator Theory* (Springer, 1974), for the classical adjoint of an operator on a space with an inner product, the model after which the pairing of this article is patterned.
