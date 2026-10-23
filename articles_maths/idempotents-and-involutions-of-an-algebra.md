# __Idempotents and Involutions of an Algebra__

## Introduction

An **idempotent** is an element $e$ with $e^2=e$, and an **involution** is an anti-automorphism $\sigma$ with $\sigma^2=\mathrm{id}$. The two notions meet because an involution carries an idempotent to an idempotent: from $e^2=e$ one gets $\sigma(e)^2=\sigma(e)$. The set of idempotents therefore carries an order-two permutation $e\mapsto e^*=\sigma(e)$, and the present article is a reading of the idempotents of an involutive algebra through that permutation.

Three relations between $e$ and $e^*$ are distinguished by the theory, and they are the subject of the article. The first is the fixed-point relation $e^*=e$, which defines the **Hermitian idempotents**. The second is the exchange relation $e^*=1-e$, which makes $e$ and $e^*$ complementary idempotents and turns $2e-1$ into a skew root of the identity. The third is the vanishing of the Hermitian square, $e^*e=0$, which makes $e$ a **left isotropic idempotent**, and makes every nonzero such $e$ a zero divisor; the two-sided form $e^*e=ee^*=0$ is, when $2$ is invertible, the condition that $e+e^*$ be an idempotent, and it includes the exchange relation as the complete case $e+e^*=1$.

The article is purely algebraic and form-free. The Peirce decomposition $A=eAe\oplus eAf\oplus fAe\oplus fAf$ is that of *Unital Algebras*, §*Idempotents and the Peirce Decomposition*; the involutions themselves, the symmetric and skew elements and the opposite algebra are *Involutive Algebras*; the Peirce analysis of a Hermitian idempotent and the orthogonality of the corners belong to *Hermitian Idempotents and the Peirce Decomposition*; the primitive idempotents and the minimal left ideals are *Primitive Idempotents and Minimal Left Ideals*; and the roots of the identity are *Roots of the Identity, Split Algebras and Nontrivial Idempotents*. No positivity, norm or form is used: the positive definite case, in which $e^*e=0$ forces $e=0$, is a theorem of Part II and is named only as a contrast.

Throughout, $F$ is a field, $A$ is a unital associative $F$-algebra with $1\neq0$, and $\sigma$ is an $F$-linear involution of $A$; we write $a^*=\sigma(a)$. The idempotent is $e$, and $f=1-e$ is its complement. The characteristic is arbitrary unless a statement says otherwise. Two restrictions are marked: the halving of an idempotent into a skew root requires $2$ invertible, and the positive definite case excludes the exchange relation. The semilinear involutions of *Involutive Algebras* are not used.

## Idempotents and the Involution

### Definitions

**Definition.** An element $e\in A$ is an **idempotent** when $e^2=e$. It is **trivial** when $e=0$ or $e=1$, and **nontrivial** otherwise. Two idempotents $e,f$ are **orthogonal** when $ef=fe=0$; they are **complementary** when in addition $e+f=1$. A family $e_1,\dots,e_r$ is **orthogonal** when $e_ie_j=0$ for $i\neq j$, and **complete** when $\sum_i e_i=1$.

For an idempotent $e$, the element $f=1-e$ is again idempotent, and $ef=fe=0$, $e+f=1$: every idempotent has a unique complement, and the pair $e,f$ is a complete orthogonal family of two elements.

**Definition.** An **involution** of $A$ is an $F$-linear map $\sigma:A\to A$ with

$$
\sigma(ab)=\sigma(b)\sigma(a), \qquad \sigma(1)=1, \qquad \sigma^2=\mathrm{id}.
$$

It is an anti-automorphism of order two; the definition and the first properties are those of *Involutive Algebras*. We write $a^*=\sigma(a)$, and $A^+=\{a:a^*=a\}$ for the symmetric elements.

### The involution acts on the idempotents

**Proposition.** Let $e\in A$ be idempotent and $f=1-e$.

**(a)** $e^*$ is idempotent, and $(e^*)^*=e$.

**(b)** $(1-e)^*=1-e^*$; in particular the complement of $e^*$ is $f^*$, and $e+f=1$ gives $e^*+f^*=1$.

**(c)** If $e$ and $f$ are orthogonal, then $e^*$ and $f^*$ are orthogonal; if $e_1,\dots,e_r$ is a complete orthogonal family, then so is $e_1^*,\dots,e_r^*$.

**(d)** $e$ is primitive exactly when $e^*$ is primitive.

**(e)** $e$ is central exactly when $e^*$ is central.

*Proof.* (a) $(e^*)^2=e^*e^*=(ee)^*=(e^2)^*=e^*$, and $\sigma^2=\mathrm{id}$. (b) $\sigma(1-e)=\sigma(1)-\sigma(e)=1-e^*$, and $\sigma$ is additive. (c) From $ef=0$ one gets $e^*f^*=(fe)^*=0$ and $f^*e^*=(ef)^*=0$; completeness is (b). (d) If $e=e_1+e_2$ with $e_1,e_2$ nonzero orthogonal idempotents, then $e^*=e_1^*+e_2^*$ is a decomposition of the same kind, since $\sigma$ is injective and (c) applies; the converse is the same statement for $\sigma^{-1}=\sigma$. (e) $\sigma$ maps the centre onto itself by *Involutive Algebras*, §*Elementary Properties*, and the inverse image of the centre is the centre.

**Corollary.** The involution is a permutation of order two of the set $\operatorname{Idem}(A)$ of idempotents, preserving orthogonality, completeness and primitivity. Its fixed set is the set of **Hermitian idempotents**,

$$
\boxed{\;\operatorname{Idem}(A)^\sigma=\{e\in\operatorname{Idem}(A):e^*=e\}\;}.
$$

The trivial idempotents $0,1$ are always fixed, since $\sigma(0)=0$ and $\sigma(1)=1$.

### The Klein four action

Beside the involution there is the **complement map**

$$
\tau:\operatorname{Idem}(A)\longrightarrow\operatorname{Idem}(A), \qquad \tau(e)=1-e .
$$

It is a bijection of order two, and it commutes with $\sigma$:

$$
\sigma\tau(e)=\sigma(1-e)=1-e^*=\tau\sigma(e).
$$

The two maps therefore generate an action of the Klein four-group $V_4=\{1,\sigma,\tau,\sigma\tau\}$ on the idempotents. The orbit of $e$ is contained in the set

$$
\{e,\ e^*,\ 1-e,\ 1-e^*\},
$$

and the four elements need not be distinct. The composite $\sigma\tau=\tau\sigma$ is the **conjugate complement** $e\mapsto1-e^*$.

The fixed sets of the three nonidentity elements are the three distinguished classes of the article:

$$
\operatorname{Idem}(A)^\sigma=\{e:e^*=e\}, \qquad
\operatorname{Idem}(A)^{\sigma\tau}=\{e:e^*=1-e\}, \qquad
\operatorname{Idem}(A)^\tau=\varnothing .
$$

The complement map has no fixed idempotent: $e=1-e$ gives $2e=1$, and multiplying by $e$ gives $2e^2=e$, hence $e=0$ and $1=0$, which is excluded. A Hermitian idempotent has orbit $\{e,1-e\}$ under $V_4$, and so does an idempotent satisfying $e^*=1-e$; a generic idempotent has an orbit of four elements.

**Remark.** The third distinguished relation of the article, $e^*e=0$, is not a fixed-point condition of this action. It is an orthogonality condition between $e$ and $e^*$, and the involution exchanges its left and its right forms; it is treated in §*Isotropic Idempotents*.

## Hermitian Idempotents

### Definition and the Peirce decomposition

**Definition.** An idempotent $e$ is **Hermitian**, or **self-adjoint**, when $e^*=e$.

The Hermitian idempotents are the fixed points of the involution on $\operatorname{Idem}(A)$. They are the algebra-level analogues of the orthogonal projections of a Hilbert space; the positive definite form that makes the analogy exact is Part II, and the form-free Peirce theory is developed here.

**Proposition.** Let $e$ be a Hermitian idempotent and $f=1-e$. Then $f$ is Hermitian, and the four Peirce corners satisfy

$$
\boxed{\;(eAe)^*=eAe, \qquad (fAf)^*=fAf, \qquad (eAf)^*=fAe, \qquad (fAe)^*=eAf\;} .
$$

In particular the Peirce decomposition is stable under the involution, the two diagonal corners are $*$-subalgebras with identities $e$ and $f$, and the involution exchanges the two off-diagonal corners.

*Proof.* For $x\in eAe$, $x=exe$, so $x^*=e^*x^*e^*=ex^*e\in eAe$; the computation for $fAf$ is the same. For $x\in eAf$, $x=exf$, so $x^*=f^*x^*e^*=fx^*e\in fAe$, and the reverse inclusion follows by applying the involution again. The diagonal corner $eAe$ is closed under multiplication and contains $e$, and $(eae)^*=ea^*e$ lies in it; the same for $fAf$.

**Remark.** The diagonal corner $eAe$ is a $*$-algebra with identity $e$, not with identity $1_A$: its unit is $e$, and the inclusion $eAe\hookrightarrow A$ is a $*$-homomorphism but not a unital one unless $e=1$. The symmetric elements of the corner are $eAe\cap A^+$, and the skew elements are $eAe\cap A^-$, where $A^-=\{a:a^*=-a\}$.

### Examples

**Example (matrix algebras).** Let $A=M_n(F)$ with the transpose involution $X^*=X^{\mathsf T}$, or with the conjugate transpose when $F=\mathbb{C}$. The Hermitian idempotents are the symmetric, respectively Hermitian, idempotents. The matrix unit $E_{11}$ is Hermitian, and its Peirce corners are

$$
E_{11}AE_{11}=FE_{11}, \qquad E_{11}AE_{22}=FE_{12}, \qquad E_{22}AE_{11}=FE_{21}, \qquad E_{22}AE_{22}=M_{n-1}(F),
$$

with the two mixed corners exchanged by the involution. For the conjugate transpose, $E_{11}$ is the orthogonal projection onto the first coordinate line, and the mixed corners are the two off-diagonal matrix blocks.

**Example (the split algebra).** Let $A=F\times F$ with the exchange involution $(a,b)^*=(b,a)$. The idempotents are $(1,0),(0,1),0,1$; the nontrivial ones are exchanged by the involution and are not Hermitian. The only Hermitian idempotents are $0$ and $1$. This is the smallest algebra in which the involution moves a nontrivial idempotent, and it is the model of the complementary case below.

**Example (a Hermitian idempotent with a noncommutative corner).** In $M_3(F)$ with the transpose, let $e=E_{11}+E_{22}$. Then $e$ is Hermitian, $eAe\cong M_2(F)$, $fAf\cong F$, and the mixed corners are the two columns and rows outside the block, exchanged by the transpose. The corner $eAe$ is noncommutative, so the Hermitian idempotent does not force the diagonal corner to be commutative.

## Complementary Idempotents

### Definition and equivalent forms

**Definition.** An idempotent $e$ is **complementary** when $e^*=1-e$. Equivalently, $e$ and $e^*$ are complementary idempotents, $e+e^*=1$.

The name records the relation, not a new operation: the complement of $e$ is $1-e$, and the condition says that the involution carries $e$ to its complement. The complementary idempotents are the fixed points of the conjugate complement $\sigma\tau$, and they are the algebra-level form of a **skew** structure: the element $2e-1$ is skew.

**Proposition.** Let $e$ be an idempotent and $f=1-e$. The following are equivalent.

**(a)** $e^*=1-e$.

**(b)** $e+e^*=1$.

**(c)** $e$ and $e^*$ are complementary: $ee^*=e^*e=0$ and $e+e^*=1$.

**(d)** $ee^*=e^*e=0$ and $e+e^*=1$. In particular both Hermitian squares vanish.

**(e)** If $2$ is invertible in $F$, the element $u=2e-1$ is a skew root of the identity, $u^*=-u$ and $u^2=1$.

*Proof.* (a)$\Leftrightarrow$(b) is the definition of the complement. (a)$\Rightarrow$(c): $e^*=1-e$ gives $ee^*=e(1-e)=0$ and $e^*e=(1-e)e=0$; the sum is $1$. (c)$\Rightarrow$(a): $e^*=1-e$ because $e+e^*=1$. (d) is the same as (c). For (e), $u^*=2e^*-1=2(1-e)-1=1-2e=-u$, and $u^2=4e^2-4e+1=1$; the computation uses $2\neq0$ only to recover $e=(1+u)/2$ in the converse, which is stated next.

**Proposition (the converse).** Suppose $2$ is invertible in $F$. If $u\in A$ satisfies $u^*=-u$ and $u^2=1$, then

$$
\boxed{\;e=\frac{1+u}{2}\;}
$$

is an idempotent with $e^*=1-e$, and the two constructions are inverse. Hence, when $2$ is invertible, the complementary idempotents are in bijection with the skew roots of the identity.

*Proof.* $e^2=(1+2u+u^2)/4=(2+2u)/4=e$, and $e^*=(1+u^*)/2=(1-u)/2=1-e$. Conversely, if $e^*=1-e$, then $(1+(2e-1))/2=e$; and if $u^*=-u$, $u^2=1$, then $2e-1=u$. The two maps are inverse.

**Remark (characteristic two).** When $2=0$, the element $u=2e-1$ is $-1$ for every idempotent, so the map $e\mapsto u$ is constant and has no inverse. The relation $e^*=1-e$ becomes $e^*=1+e$, and it still defines a class of idempotents, but it is no longer the same class as the skew roots of $1$: every idempotent gives the constant $u=-1=1$, while the skew roots of $1$ can be numerous in a non-reduced algebra. The halving correspondence and its collapse are the subject of *Roots of the Identity, Split Algebras and Nontrivial Idempotents*; the present article records the relation without using the halving.

### Examples

**Example (the symplectic matrix algebra).** Let $A=M_2(F)$ with the symplectic involution

$$
X^*=JX^{\mathsf T}J^{-1}, \qquad J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
$$

For $e=E_{11}$ one has $e^*=E_{22}=1-e$, so $e$ is complementary. The image of $e$ is the first coordinate line, the image of $e^*$ is the second, and the involution exchanges the two; the element $2e-1=\operatorname{diag}(1,-1)$ is skew and squares to $1$. The same algebra with the transpose involution has $E_{11}^*=E_{11}$, so the two involutions put the same idempotent in different classes.

**Example (the split algebra).** In $A=F\times F$ with the exchange involution, $e=(1,0)$ satisfies $e^*=(0,1)=1-e$. The element $2e-1=(1,-1)$ is skew and squares to $(1,1)=1$. This is the commutative model of the complementary case.

**Example (the positive definite case is empty).** If $A$ carries a positive definite Hermitian form and $e^*$ is the adjoint of $e$, then $e^*e=0$ forces $e=0$. A complementary idempotent would give $e^*e=(1-e)e=0$, hence $e=0$; then $e^*=1-e=1$, while $e^*=0^*=0$, so $1=0$, impossible. Thus a positive definite involutive algebra has no complementary idempotent. The statement belongs to the form theory of Part II; the algebra-level computation $e^*e=(1-e)e=0$ is already visible here.

## Isotropic Idempotents

### Definition and first properties

**Definition.** An idempotent $e$ is **left isotropic** when $e^*e=0$, and **right isotropic** when $ee^*=0$. It is **two-sided isotropic**, or simply **isotropic**, when both products vanish.

The terminology is that of a Hermitian form: $e^*e$ is the Hermitian square of $e$, and its vanishing is the algebraic form of isotropy. The two-sided condition is the one that is stable under the involution and that produces a decomposition; the one-sided conditions are genuinely one-sided, as the examples below show.

**Proposition.** Let $e$ be a nonzero idempotent with $e^*e=0$, and let $f=1-e$.

**(a)** $e^*$ is a nonzero idempotent and $e$ is a left zero divisor: $e^*e=0$ with $e^*\neq0$.

**(b)** $e^*=e^*f$, so $e^*$ lies in the left ideal $Af$; equivalently $e^*e=0$ says that $e^*$ is supported on the complement of $e$.

**(c)** $e$ is not Hermitian.

**(d)** $(e+e^*)^2=e+e^*+ee^*$; hence $e+e^*$ is idempotent exactly when $ee^*=0$ as well.

**(e)** If $2$ is invertible, $e+e^*$ is idempotent exactly when $e$ is two-sided isotropic. In that case $g=e+e^*$ is a Hermitian idempotent, $e$ and $e^*$ are orthogonal idempotents with sum $g$, and $e^*=g-e$.

*Proof.* (a) $e^*$ is idempotent by the proposition of §*The involution acts on the idempotents*, and $\sigma$ is injective, so $e^*\neq0$. (b) $e^*=e^*(e+f)=e^*e+e^*f=e^*f$. (c) If $e^*=e$, then $0=e^*e=e^2=e$, contrary to $e\neq0$. (d) Expand. (e) If $e+e^*$ is idempotent, then $ee^*+e^*e=0$. Multiplying this equation on the left by $e^*$ gives $e^*ee^*+e^*e=0$, and on the right by $e^*$ gives $e^*e+ee^*=0$; subtracting gives $e^*e=ee^*$, and then $2e^*e=0$, hence $e^*e=0$ and $ee^*=0$. The converse is (d). The last assertions follow from $e^*e=ee^*=0$ and $e+e^*=g$, and $g^*=e^*+e=g$.

**Corollary.** The two-sided isotropic idempotents are exactly the idempotents $e$ for which $e+e^*$ is an idempotent, when $2$ is invertible. The sum $g=e+e^*$ is then Hermitian, and $e$ and $e^*$ are complementary idempotents of the corner $gAg$.

*Proof.* The equivalence is (e) of the proposition. The corner $gAg$ has identity $g$. Since $e^*e=ee^*=0$, $eg=e(e+e^*)=e$ and $ge=(e+e^*)e=e$, so $e\in gAg$; the same computation gives $e^*\in gAg$. The two are orthogonal and sum to $g$.

**Remark.** The relation $e^*e=0$ does not imply $ee^*=0$. The next examples exhibit the difference, and the difference is the reason the article distinguishes the one-sided and the two-sided conditions.

### Examples

**Example (the hyperbolic matrix algebra).** Let $A=M_2(F)$ with the involution

$$
X^*=DX^{\mathsf T}D^{-1}, \qquad D=\operatorname{diag}(1,-1),
$$

and let

$$
e=\begin{pmatrix}1&0\\1&0\end{pmatrix}, \qquad e^2=e .
$$

Then

$$
e^*=\begin{pmatrix}1&-1\\0&0\end{pmatrix}, \qquad
e^*e=\begin{pmatrix}0&0\\0&0\end{pmatrix}, \qquad
ee^*=\begin{pmatrix}1&-1\\1&-1\end{pmatrix}\neq0 .
$$

So $e$ is left isotropic and not right isotropic. The idempotent $e$ is a zero divisor, and the element $e+e^*$ is not idempotent, since $ee^*\neq0$.

**Example (the transpose over the complex numbers).** Let $A=M_2(\mathbb{C})$ with the plain transpose $X^*=X^{\mathsf T}$, and let

$$
e=\begin{pmatrix}1&0\\ i&0\end{pmatrix}, \qquad e^2=e .
$$

Then $e^*e=0$ and $ee^*=\begin{pmatrix}1&i\\ i&-1\end{pmatrix}\neq0$. The example uses no conjugate: the transpose alone produces isotropic idempotents over a field containing a square root of $-1$. With the conjugate transpose instead, $e^*e$ is positive semidefinite and nonzero for $e\neq0$, so no nonzero example exists.

**Example (the symplectic matrix algebra).** In $M_2(F)$ with the symplectic involution, $e=E_{11}$ satisfies $e^*=1-e$, so $e^*e=ee^*=0$: this is the complete two-sided case, and $e+e^*=1$. The same idempotent is left isotropic, right isotropic and complementary; the three notions overlap in this example but are not equivalent in general.

**Example (a domain).** If $A$ has no zero divisors, then $e^*e=0$ forces $e=0$ or $e^*=0$, hence $e=0$; a nonzero idempotent of a domain is necessarily $1$. So a domain has no nontrivial isotropic idempotent, and its only idempotents are $0$ and $1$. The dual numbers are not a domain, but they also have no nontrivial idempotent in characteristic not two; the example is *Roots of the Identity, Split Algebras and Nontrivial Idempotents*.

## The Three Relations Together

### The table

The three classes are summarized in the following table. The column "$\sigma$-image" records what the involution does to the condition; the column "name" is the one used in the article.

| Condition | Name | Equivalent form | $\sigma$-image |
|---|---|---|---|
| $e^*=e$ | Hermitian | $e\in A^+$ | the same condition |
| $e^*=1-e$ | complementary | $e+e^*=1$, $e^*e=ee^*=0$ | the same condition |
| $e^*e=0$ | left isotropic | $e^*\in Af$; a nonzero $e$ is a left zero divisor | $ee^*=0$ (right isotropic) |
| $e^*e=ee^*=0$ | two-sided isotropic | $e+e^*$ idempotent (if $2\neq0$) | the same condition |

The first two rows are the fixed-point classes of the Klein four action; the third and fourth are orthogonality conditions. The implications are

$$
\text{complementary}\ \Longrightarrow\ \text{two-sided isotropic}\ \Longrightarrow\ \text{left isotropic},
$$

and neither implication reverses: a two-sided isotropic idempotent with $e+e^*\neq1$ is not complementary, and a left isotropic idempotent with $ee^*\neq0$ is not two-sided. The complementary case is the complete two-sided isotropic case, $e+e^*=1$.

**Example (a two-sided isotropic idempotent that is not complementary).** Let $A=M_3(\mathbb{C})$ with the transpose, and let $u=(1,i,0)^{\mathsf T}$, $v=(1,-i,0)^{\mathsf T}$. Then $u^{\mathsf T}u=v^{\mathsf T}v=0$ and $v^{\mathsf T}u=2$. The rank-one matrix

$$
e=\frac{u v^{\mathsf T}}{v^{\mathsf T}u}
$$

is an idempotent with $e^*=v u^{\mathsf T}/(v^{\mathsf T}u)$, and $e^*e=ee^*=0$; but $e+e^*$ has rank two, so it is not $1$. The idempotent is two-sided isotropic and not complementary.

**Proposition.** The involution preserves the Hermitian and the complementary classes and exchanges the left and the right isotropic classes:

$$
e^*=e\ \Longrightarrow\ (e^*)^*=e^*, \qquad
e^*=1-e\ \Longrightarrow\ (e^*)^*=1-e^*, \qquad
e^*e=0\ \Longleftrightarrow\ e\,e^*=0\ \text{for } e^*.
$$

*Proof.* The first is $\sigma^2=\mathrm{id}$; the second is $(e^*)^*=e=1-e^*$ because $e^*=1-e$; the third is $(e^*)^*e^*=ee^*$, which vanishes exactly when the right square of $e$ vanishes.

**Remark.** The proposition is the precise sense in which the involution does not preserve the one-sided isotropic class: it maps a left isotropic idempotent to a right isotropic one. The two-sided class, being the conjunction of the two, is preserved.

## Examples

**Example (the matrix algebra with the transpose).** In $M_n(F)$ with $X^*=X^{\mathsf T}$, the Hermitian idempotents are the symmetric idempotents. A complementary idempotent satisfies $e+e^{\mathsf T}=1$; writing $e=\tfrac12 I+N$ gives $N^{\mathsf T}=-N$ and $N^2=\tfrac14 I$. Over $\mathbb{C}$ the $2\times2$ example

$$
e=\begin{pmatrix}1/2&i/2\\-i/2&1/2\end{pmatrix}, \qquad
e^{\mathsf T}=\begin{pmatrix}1/2&-i/2\\i/2&1/2\end{pmatrix}=1-e,
$$

is a complementary idempotent, so the class is nonempty over a field containing a square root of $-1$. Over $\mathbb{R}$ there is no such $N$: a real skew-symmetric matrix has no real eigenvalue, while $N^2=\tfrac14 I$ forces the eigenvalues $\pm\tfrac12$. The complementary idempotents are therefore not the symmetric idempotents; the symmetric ones are the Hermitian class, and the complementary class is a different class, empty over $\mathbb{R}$ for the transpose and nonempty over $\mathbb{C}$. The isotropic idempotents exist when $F$ contains a square root of $-1$ and $n\geq2$, as the $2\times2$ example above shows.

**Example (the symplectic matrix algebra).** In $M_2(F)$ with the symplectic involution, every nontrivial idempotent is complementary. Indeed a nontrivial idempotent of $M_2(F)$ has rank one, with a one-dimensional image $L$ and a one-dimensional kernel $K$, and the symplectic involution exchanges the two lines; the computation on $E_{11}$ is the model, and the general case is the same computation in a symplectic basis. The Hermitian idempotents are only $0$ and $1$, since a rank-one idempotent has $e^*=1-e\neq e$.

**Example (the split algebra and its products).** In $F\times F$ with the exchange involution, the nontrivial idempotents $(1,0)$ and $(0,1)$ are complementary and two-sided isotropic, and the only Hermitian idempotents are $0,1$. In $F\times F$ with the componentwise involution $(a,b)^*=(a,b)$, every idempotent is Hermitian, and there are no nontrivial complementary or isotropic idempotents. The two involutions on the same algebra therefore realize the two extreme behaviours.

**Example (a Hermitian idempotent and an isotropic one in the same algebra).** In $M_2(\mathbb{C})$ with the transpose, $E_{11}$ is Hermitian and $e=\begin{pmatrix}1&0\\ i&0\end{pmatrix}$ is left isotropic. The two idempotents have the same rank, so neither the rank nor the algebra determines the class; the involution and the idempotent together do.

## Summary

An involution $\sigma$ acts on the idempotents of $A$ by $e\mapsto e^*$, preserving orthogonality, completeness, primitivity and centrality. The complement map $e\mapsto1-e$ commutes with $\sigma$, and the two generate a Klein four action whose orbit of $e$ is contained in $\{e,e^*,1-e,1-e^*\}$. Three relations are distinguished, together with the two-sided form of the third. The **Hermitian** idempotents are the fixed points $e^*=e$; their Peirce corners are $*$-stable, the diagonal corners are $*$-subalgebras and the mixed corners are exchanged. The **complementary** idempotents are the fixed points of the conjugate complement, $e^*=1-e$; equivalently $e+e^*=1$ and $e^*e=ee^*=0$, and when $2$ is invertible they are in bijection with the skew roots of the identity by $e\mapsto2e-1$. The **left isotropic** idempotents satisfy $e^*e=0$; a nonzero one is a zero divisor, is not Hermitian, and the involution exchanges the left and the right forms. The **two-sided isotropic** idempotents satisfy $e^*e=ee^*=0$; when $2$ is invertible this is equivalent to $e+e^*$ being an idempotent, and the sum $e+e^*$ is then a Hermitian idempotent whose corner contains $e$ and $e^*$ as complementary idempotents. The complementary class is the complete two-sided isotropic class. The matrix algebras with the transpose, the conjugate transpose, the hyperbolic involution and the symplectic involution, and the split algebra with the exchange involution, are the worked examples. No form, norm or positivity is used.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $e,f$ | idempotent and its complement $f=1-e$ |
| $e^*$ | $\sigma(e)$, the image of $e$ under the involution |
| $A^+$ | the symmetric elements $\{a:a^*=a\}$ |
| $A^-$ | the skew elements $\{a:a^*=-a\}$ |
| $\operatorname{Idem}(A)$ | the set of idempotents of $A$ |
| $\tau(e)=1-e$ | the complement map |
| $\sigma\tau(e)=1-e^*$ | the conjugate complement |
| $e^*=e$ | Hermitian idempotent |
| $e^*=1-e$ | complementary idempotent |
| $e^*e=0$ | left isotropic idempotent |
| $e^*e=ee^*=0$ | two-sided isotropic idempotent |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for idempotents, Peirce decompositions and the matrix examples.
- Nathan Jacobson, *Basic Algebra II* (Freeman, 1989), for involutions, Hermitian elements and the classical matrix algebras.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the classification of involutions and the role of the symmetric and skew elements.
- Israel Gohberg, Peter Lancaster and Leiba Rodman, *Indefinite Linear Algebra and Applications* (Birkhäuser, 2005), for the indefinite and symplectic matrix examples and the isotropic idempotents they carry.
