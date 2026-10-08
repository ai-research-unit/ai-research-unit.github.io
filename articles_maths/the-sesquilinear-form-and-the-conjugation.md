# __The Sesquilinear Form and the Conjugation__

## Introduction

A form of the layer is a function of two variables, and the compatibility of *Topological Sesqualgebras with a Form*, §*The Identity and Its Equivalent* is a condition on it. On a unital algebra the condition determines the form from its values on the pairs whose second entry is the unit, that is, from a single linear functional $\varphi$, through the identity

$$
h(x,y) = h(y^{*}x, 1) = \varphi(y^{*}x) .
$$

The form is therefore the datum of the involution together with a functional, and the compatibility is not a restriction on the class of forms but a normalisation of it: the compatible forms are exactly the forms $h_{\varphi}$ for a functional $\varphi$, and the classifications of the forms are classifications of the functionals. This article proves the correspondence, reads the three kinds of form as three conditions on $\varphi$, identifies the involution that the conjugation induces on the space of forms, and reads the failure of the dictionary in characteristic two.

The functional form of a compatible form organises the layer. The Hermitian forms are the forms $h_{\varphi}$ with $\varphi$ real for the involution, that is $\varphi(z^{*}) = \varsigma(\varphi(z))$; the skew-Hermitian forms are the forms with $\varphi$ anti-real; the alternating forms are the forms with $\varphi$ vanishing on the Hermitian squares $xx^{*}$, which for invertible $2$ is the vanishing of $\varphi$ on the symmetric part $A^{+}$. The radical is the annihilator $A^{\perp} = \{x : \varphi(Ax) = 0\}$, which is why it is a left ideal, and its image under the involution is $\{x : \varphi(Ax^{*}) = 0\}$. The conjugation acts on the forms themselves by $h \mapsto h^{\dagger}$, $h^{\dagger}(x,y) = \varsigma(h(y,x))$, an involution whose fixed forms are the Hermitian ones and whose anti-fixed forms are the skew-Hermitian ones, and it corresponds to the involution $\varphi \mapsto \varsigma\circ\varphi\circ{}^{*}$ of the functionals; when $2$ is invertible the two eigenspaces are complementary and every compatible form splits uniquely into a Hermitian and a skew-Hermitian part, and when $2$ is not invertible the split fails and the kinds merge. The collapse at $\varsigma = \mathrm{id}$ is the bilinear theory of *Bilinear Forms*, and the field case is the Hermitian geometry of *Unitary Geometry over a Field with Involution*.

The article proves the correspondence and the reconstruction, computes the radical, establishes the dictionary of the kinds and the splitting, treats the field case and the collapse, and works the examples. The algebraic theory of the forms of the layer is *Hermitian Forms on a Sesqualgebra*, the positivity and the norm are *Positivity and the Positive Cone of a Hermitian Form* and *The Norm Defined by a Form*, the adjoint of an operator *The Adjoint under a Hermitian Form*, the pairings of the layer *The Sesquilinear Adjoint Operator*, the involution as the adjoint of a multiplication *Adjoints in a Commutative Involutive Algebra*, and the general theory of involutive algebras *Involutive Algebras*; the continuity of the involution is Part II's, in *The Continuity of the Involution*. Throughout, $A$ is a unital associative $R$-algebra over a commutative ring $R$ with $1$, $\varsigma$ is an involution of $R$, $*$ is a $\varsigma$-semilinear involution of $A$ with $(xy)^{*} = y^{*}x^{*}$ and $*^{2} = \mathrm{id}$, the forms are those of the entry, $h(\lambda x,y) = \lambda h(x,y)$ and $h(x,\lambda y) = \varsigma(\lambda)h(x,y)$, and $2$ is invertible whenever the article says so.

## The Functional of a Form

### The Reconstruction

**Definition.** The **functional** of a form $h$ is the map

$$
\varphi : A \longrightarrow R, \qquad \varphi(x) = h(x,1) .
$$

It is $R$-linear when $h$ is a form, being the restriction of $h$ to the second argument equal to $1$.

**Theorem (the reconstruction).** Let $h$ be a form compatible with the product, $h(xy,z) = h(y,x^{*}z)$ for all $x,y,z$. Then

$$
h(x,y) = h(y^{*}x, 1) = \varphi(y^{*}x) \qquad \text{for all } x, y \in A .
$$

*Proof.* Put $a = y^{*}$, $b = x$ and $c = 1$ in the compatibility: it reads $h(y^{*}x, 1) = h(x, (y^{*})^{*}1) = h(x, y1) = h(x,y)$, the last equality by the unit. $\square$

**Corollary (the unit recovers the form).** A compatible form is determined by its values $h(x,1)$, and a compatible form vanishing on all the pairs $(x,1)$ is zero.

*Proof.* The reconstruction expresses $h(x,y)$ through $\varphi(y^{*}x)$, and $\varphi$ is the restriction to the pairs $(x,1)$; if all of them vanish then $\varphi = 0$ and $h = 0$. $\square$

### The Correspondence

**Theorem (the correspondence).** The map

$$
\varphi \longmapsto h_{\varphi}, \qquad h_{\varphi}(x,y) = \varphi(y^{*}x) ,
$$

is a bijection from the $R$-linear functionals $\varphi : A \to R$ onto the forms compatible with the product, and its inverse is $h \mapsto (x \mapsto h(x,1))$.

*Proof.* Let $\varphi$ be $R$-linear. The form $h_{\varphi}$ is biadditive, because $\varphi$ is additive and the product and the involution are; it is $R$-linear in the first variable,

$$
h_{\varphi}(\lambda x, y) = \varphi(y^{*}(\lambda x)) = \varphi(\lambda(y^{*}x)) = \lambda\,\varphi(y^{*}x) = \lambda\,h_{\varphi}(x,y) ,
$$

the second equality being the $R$-bilinearity of the product and the third the $R$-linearity of $\varphi$; it is $\varsigma$-semilinear in the second,

$$
h_{\varphi}(x, \lambda y) = \varphi((\lambda y)^{*}x) = \varphi(\varsigma(\lambda)(y^{*}x)) = \varsigma(\lambda)\,\varphi(y^{*}x) = \varsigma(\lambda)\,h_{\varphi}(x,y) ,
$$

the second equality being the semilinearity of the involution; and it is compatible, because

$$
h_{\varphi}(xy,z) = \varphi(z^{*}(xy)) = \varphi((z^{*}x)y) = h_{\varphi}(y, x^{*}z) ,
$$

where the middle equality is the associativity of the product and the last is the definition read with $(x^{*}z)^{*} = z^{*}x$. So the map is well defined into the compatible forms, it is injective because $\varphi(x) = h_{\varphi}(x,1)$, and it is surjective by the reconstruction, whose $R$-linear functional is the given $\varphi$ because a form is $R$-linear in its first variable. $\square$

**Corollary (the compatibility is a normalisation).** On a unital algebra the compatible forms are exactly the forms determined by a functional; a form is compatible if and only if it is $h_{\varphi}$ for some $R$-linear $\varphi$. In particular the compatibility of the entry is automatic for every form of the shape $h(x,y) = \varphi(y^{*}x)$ and it is exactly the statement that the form is of that shape.

*Proof.* Both directions are the theorem. $\square$

**Corollary (the pairings of the entry article).** Let $\tau : A \to R$ be an $R$-linear functional and let $\tau$ also denote the form $\tau(xy^{*})$ of the entry, §*The Model*. Then

$$
\tau(y^{*}x) = \tau(xy^{*}) \qquad \text{for all } x, y ,
$$

as soon as $\tau$ is central on products, $\tau(uv) = \tau(vu)$; so the entry's trace pairings are the forms $h_{\tau}$ of the correspondence, and the matrix model $h(X,Y) = \operatorname{tr}(XY^{*})$ is $h_{\varphi}$ with $\varphi = \operatorname{tr}$, since $\operatorname{tr}(Y^{*}X) = \operatorname{tr}(XY^{*})$ by the trace property. The functional of the model is the trace and the compatibility is the cyclicity.

*Proof.* The cyclicity of $\tau$ gives $\tau(y^{*}x) = \tau(xy^{*})$; the model is the case $\tau = \operatorname{tr}$, whose cyclicity is the trace property used in the model of *Topological Sesqualgebras with a Form*, §*The Model*. $\square$

**The topological form of the correspondence.** When the product and the involution are continuous, the correspondence restricts to the continuous functionals and the continuous forms; that is Part II's, in *The Continuity of the Involution* and *Topology on Sesqualgebras with a degree-2 form*, and it is named here rather than developed.

### The Radical

**Theorem (the radical is an annihilator).** Let $h = h_{\varphi}$ be compatible. Then the radical of the entry, §*The Definition*, is

$$
A^{\perp} = \{x \in A : \varphi(Ax) = 0\} ,
$$

the set of the elements annihilated by the functional on all their right multiples, and its image under the involution is $(A^{\perp})^{*} = \{x : \varphi(Ax^{*}) = 0\}$. The radical is a left ideal, and it is zero exactly when for every $x \neq 0$ there is $a \in A$ with $\varphi(ax) \neq 0$.

*Proof.* The form is $h(x,y) = \varphi(y^{*}x)$; the condition $h(x,y) = 0$ for every $y$ is $\varphi(y^{*}x) = 0$ for every $y$, and $y \mapsto y^{*}$ is a bijection, so it is $\varphi(Ax) = 0$. For $a \in A$ and $x \in A^{\perp}$ one has $A(ax) \subseteq Ax$, so $\varphi(A(ax)) = 0$ and $ax \in A^{\perp}$: the radical is a left ideal, which is the ideal property of the entry, §*The Radical Is an Ideal*. Applying the involution, $\varphi(Ax^{*}) = 0$ is the condition that $x^{*}$ lies in the annihilator with the roles read through $*$, and $(A^{\perp})^{*} = \{x : \varphi(Ax^{*}) = 0\}$. $\square$

**Example (the rank-one functional on the matrices).** Let $A = M_n(R)$ and $\varphi(Z) = \operatorname{tr}(ZC)$ for a fixed matrix $C$. The coefficient of $A_{ij}$ in $\operatorname{tr}(AxC) = \sum_{p,q,r}A_{pq}x_{qr}C_{rp}$ is $\sum_{r}x_{jr}C_{ri} = (xC)_{ji}$, so the radical is $\{x : xC = 0\}$, a left ideal of $A$, and for $C = E_{11}$ it is the set of matrices whose first column is zero; its image under the conjugate transpose is the set of matrices whose first row is zero. The example is the one of the entry, §*The Radical Is an Ideal*, read through the functional.

*Proof.* The expansion $\operatorname{tr}(AxC) = \sum_{i,j,k}A_{ij}x_{jk}C_{ki}$ shows that the functional on $A$ is a nondegenerate pairing with the entries of $xC$, so it vanishes for every $A$ exactly when $xC = 0$; the set of such $x$ is closed under left multiplication, $(ax)C = a(xC)$, so it is a left ideal as the theorem requires. For $C = E_{11}$ the condition $xC = 0$ is $x_{j1} = 0$ for every $j$, the first column of $x$ being zero, which is the example of the entry, §*The Radical Is an Ideal*. $\square$

## The Dictionary of the Kinds

### Hermitian, Skew-Hermitian and Alternating

**Definition.** A form $h$ is **Hermitian** when $h(y,x) = \varsigma(h(x,y))$ and **skew-Hermitian** when $h(y,x) = -\varsigma(h(x,y))$ for all $x,y$, and **alternating** when $h(x,x) = 0$ for every $x$; the definitions, the diagonal proposition and the ideal property of the radical are the entry, §*The Definition* and §*The Radical Is an Ideal*. The first two are the $\varepsilon$-conditions of *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint*, §*Hermitian Forms over a Ring with Involution*, with $\varepsilon = 1$ for the Hermitian and $\varepsilon = -1$ for the skew-Hermitian, called symplectic there; the alternating condition is the vanishing of the diagonal, which is the $\varepsilon = -1$ class when the base involution is the identity and $2$ is invertible.

**Theorem (the dictionary).** Let $h = h_{\varphi}$ be compatible and let $\varphi$ be its $R$-linear functional. Then

$$
h \text{ is Hermitian} \iff \varphi(z^{*}) = \varsigma(\varphi(z)) \ \text{ for all } z \in A,
$$
$$
h \text{ is skew-Hermitian} \iff \varphi(z^{*}) = -\varsigma(\varphi(z)) \ \text{ for all } z \in A,
$$
$$
h \text{ is alternating} \iff \varphi(xx^{*}) = 0 \ \text{ for all } x \in A .
$$

*Proof.* The three are computations on the correspondence. For the Hermitian condition, $h(y,x) = \varphi(x^{*}y)$ and $\varsigma(h(x,y)) = \varsigma(\varphi(y^{*}x))$; putting $z = y^{*}x$, whose adjoint is $z^{*} = x^{*}y$, the condition for all $x,y$ reads $\varphi(z^{*}) = \varsigma(\varphi(z))$, and every $z$ arises, $x = 1$ giving $z = y^{*}$. The skew-Hermitian condition is the same computation with the sign. The alternating condition is $h(x,x) = \varphi(x^{*}x) = 0$, and $x^{*}x$ with $xx^{*}$ are exchanged by the involution, so the condition for every $x$ may be written $\varphi(xx^{*}) = 0$. $\square$

**Corollary (the diagonal).** Let $h = h_{\varphi}$ be Hermitian. Then $h(x,x) = \varphi(x^{*}x)$ lies in the fixed ring $R^{\varsigma}$ for every $x$, and it is $\varphi(xx^{*})$ when $\varphi$ is central on products; if $h$ is skew-Hermitian then $h(x,x)$ is anti-fixed, $\varsigma(h(x,x)) = -h(x,x)$. The first statement is the diagonal proposition of the entry and the second is its companion, and the second does not vanish in general: it vanishes when $2$ is invertible and $\varsigma = \mathrm{id}$, and it need not vanish otherwise, the skew form with functional $\varphi(z) = cz_{11}$, $\varsigma(c) = -c$, having a nonzero diagonal.

*Proof.* The two statements are the dictionary on the pair $(x,x)$, $h(x,x)$ being $\varphi(x^{*}x)$ with $(x^{*}x)^{*} = x^{*}x$. For the last clause, the skew-Hermitian form with functional $\varphi(z) = cz_{11}$ on the matrices, $\varsigma(c) = -c$, has $h(X,X) = c\sum_{k}\varsigma(x_{k1})x_{k1}$ nonzero for $c \neq 0$ and $X$ with a nonzero first column; and at $\varsigma = \mathrm{id}$ the condition is $h(x,x) = -h(x,x)$, that is $2h(x,x) = 0$. $\square$

### Alternating and the Symmetric Part

**Theorem (alternating forms and the symmetric part).** Suppose $2$ invertible in $R$. Then a compatible form $h = h_{\varphi}$ is alternating if and only if

$$
\varphi(z + z^{*}) = 0 \qquad \text{for all } z \in A ,
$$

if and only if $\varphi$ vanishes on the symmetric part $A^{+} = \{z : z = z^{*}\}$; and an alternating form is anti-symmetric, $h(x,y) = -h(y,x)$.

*Proof.* The polarised form of a biadditive $h$ is $h(x+y,x+y) = h(x,x) + h(x,y) + h(y,x) + h(y,y)$. If $h$ is alternating the two diagonal terms vanish and $h(x,y) + h(y,x) = 0$, which is the anti-symmetry; in the functional, $h(x,y) + h(y,x) = \varphi(y^{*}x) + \varphi(x^{*}y) = \varphi(z + z^{*})$ with $z = y^{*}x$, and $z$ runs over $A$ because $x = 1$ gives $z = y^{*}$. Conversely, if $\varphi(z+z^{*}) = 0$ for every $z$ then $h(x,x) = \varphi(x^{*}x) = \tfrac12\varphi(2x^{*}x) = \tfrac12\varphi\bigl(x^{*}x + (x^{*}x)^{*}\bigr) = 0$, the element $x^{*}x$ being symmetric, and $h$ is alternating. Finally, $\varphi$ vanishes on $A^{+}$ exactly when $\varphi(z+z^{*}) = 0$ for every $z$, because $z + z^{*} \in A^{+}$ and a symmetric element $s$ is $\tfrac12(s + s^{*})$; the two conditions coincide. $\square$

**Corollary (the classical cases).** Suppose $2$ invertible. If $\varsigma = \mathrm{id}$ the alternating compatible forms are exactly the skew-Hermitian ones; if in addition $* = \mathrm{id}$ then the alternating compatible forms are zero. On the complex matrices with the conjugate transpose the alternating compatible forms are zero.

*Proof.* At $\varsigma = \mathrm{id}$ the conditions $\varphi(z^{*}) = -\varphi(z)$ and $\varphi(z + z^{*}) = 0$ are the same condition, so the skew-Hermitian and the alternating classes coincide by the dictionary. If $* = \mathrm{id}$ then $A^{+} = A$ and an alternating form has $\varphi = 0$, hence $h = 0$; this is the statement of *Bilinear Forms*, §*Symmetric, Alternating and Skew-Symmetric Forms*, that a symmetric alternating form vanishes when $2$ is invertible, read through the correspondence. On $M_n(\mathbb{C})$ with the conjugate transpose the alternating compatible forms are zero: the condition is $\varphi(XX^{*}) = 0$ for every $X$, the matrices $XX^{*}$ range over the positive semi-definite matrices, every Hermitian matrix is a difference of two of them and every matrix is $H + iK$ with $H$ and $K$ Hermitian, so $\varphi$ vanishes on a set whose $\mathbb{C}$-span is all of $M_n(\mathbb{C})$ and $\varphi = 0$ by its $\mathbb{C}$-linearity. $\square$

**Example (a nonzero alternating form).** Let $A = R \times R$ with the componentwise product, the involution $(a,b)^{*} = (b,a)$, the base involution $\varsigma = \mathrm{id}$ and the functional $\varphi(a,b) = a - b$. Then $\varphi$ is $R$-linear, its form is

$$
h(x,y) = \varphi(y^{*}x) = \varphi\bigl((d,c)(a,b)\bigr) = da - cb \qquad \text{for } x = (a,b), \ y = (c,d) ,
$$

it is alternating, $\varphi(xx^{*}) = \varphi(ab,ab) = 0$, it is skew-Hermitian, $h(y,x) = cb - da = -h(x,y)$, and it is nonzero, $h((1,0),(0,1)) = 1$. The example is the smallest: with $\varsigma = \mathrm{id}$ a module of rank one over the base forces $* = \mathrm{id}$, since the $\varsigma$-semilinearity gives $*(x) = *(1)x$, the two conditions $*(1)^{2} = *(1)$ and $*(1)^{2} = 1$ force $*(1) = 1$, and then $\varphi(xx^{*}) = 0$ at $x = 1$ gives $\varphi = 0$, so the algebra involution must be nontrivial and rank two is enough. The anti-symmetry of an alternating form is compatible with the skew-Hermitian condition, and at the trivial base involution the two classes are the same class.

**Remark (the rank of an alternating form on the matrices).** An alternating form on a free module of finite rank has even rank, by *Bilinear Forms*, §*Alternating Forms Have Even Rank*, over a field in every characteristic and over a ring in which $2$ is invertible; the statement is about the form alone and does not use the compatibility, so it applies to the alternating forms of the layer. On $A = M_n(R)$ the underlying module is free of rank $n^{2}$, which is odd for odd $n$, so an alternating compatible form on the matrix algebra of odd size is necessarily degenerate when the base is a field or $2$ is invertible, whatever the involution. The example above lives on a module of rank two and has rank two.

### The Conjugation on the Space of Forms

**Definition.** The **adjoint form** of a form $h$ is

$$
h^{\dagger}(x,y) = \varsigma\bigl(h(y,x)\bigr) .
$$

**Proposition (the adjoint form is a form, and an involution).** If $h$ is a form then $h^{\dagger}$ is a form; the assignment $h \mapsto h^{\dagger}$ is additive, $R$-linear and of order two, so it is an involution of the $R$-module of forms; it preserves the compatible forms; and its fixed forms are the Hermitian ones and its anti-fixed forms the skew-Hermitian ones. The forms of *The Sesquilinear Adjoint Operator*, §*The Transposed Pairing*, are the same construction read as a pairing.

*Proof.* For the semilinearity, $h^{\dagger}(\lambda x,y) = \varsigma(h(y,\lambda x)) = \varsigma(\varsigma(\lambda)h(y,x)) = \lambda h^{\dagger}(x,y)$ and $h^{\dagger}(x,\lambda y) = \varsigma(h(\lambda y,x)) = \varsigma(\lambda h(y,x)) = \varsigma(\lambda)h^{\dagger}(x,y)$. Additivity and $R$-linearity are those of $h$ and of $\varsigma$; the order two is $\varsigma^{2} = \mathrm{id}$ and the symmetry of the two arguments. The fixed forms satisfy $h(y,x) = \varsigma(h(x,y))$, which is the Hermitian condition, and the anti-fixed satisfy the skew-Hermitian one. If $h = h_{\varphi}$ is compatible then $h^{\dagger}$ is $h_{\varsigma\varphi{}^{*}}$ by the next theorem, hence compatible. $\square$

**Theorem (the correspondence is equivariant).** Let $\varphi$ be an $R$-linear functional and let $T\varphi = \varsigma\circ\varphi\circ{}^{*}$, that is $(T\varphi)(z) = \varsigma(\varphi(z^{*}))$. Then $T$ is an involution of the $R$-module of functionals, and

$$
h_{\varphi}^{\dagger} = h_{T\varphi} .
$$

*Proof.* For the involution, $T(T\varphi)(z) = \varsigma\bigl(\varsigma(\varphi((z^{*})^{*}))\bigr) = \varphi(z)$, and $T$ is additive and $R$-linear because $\varsigma$ and $*$ are and $\varphi$ is. For the identity, $h_{\varphi}^{\dagger}(x,y) = \varsigma(h_{\varphi}(y,x)) = \varsigma(\varphi(x^{*}y)) = \varsigma(\varphi((y^{*}x)^{*})) = (T\varphi)(y^{*}x) = h_{T\varphi}(x,y)$. $\square$

**Theorem (the splitting).** Suppose $2$ invertible in $R$. Then every compatible form splits uniquely as the sum of a Hermitian and a skew-Hermitian compatible form,

$$
h = h^{+} + h^{-}, \qquad h^{\pm}(x,y) = \tfrac12\bigl(h(x,y) \pm \varsigma(h(y,x))\bigr) = \tfrac12\bigl(h \pm h^{\dagger}\bigr)(x,y) ,
$$

and correspondingly every $R$-linear functional splits as $\varphi = \varphi^{+} + \varphi^{-}$ with $\varphi^{\pm} = \tfrac12(\varphi \pm T\varphi)$ real and anti-real. The space of compatible forms is the direct sum of the two eigenspaces of the adjoint involution.

*Proof.* The two projections $\tfrac12(\mathrm{id} \pm {}^{\dagger})$ are $R$-linear idempotents with images the fixed and the anti-fixed forms, and they sum to the identity, so the splitting exists; it is unique because a form both Hermitian and skew-Hermitian satisfies $h = -h$ and is zero when $2$ is invertible. The functional statement is the same computation through the equivariance, and the direct sum is the same statement. $\square$

### The Failure When $2$ Is Not Invertible

**Theorem (the degeneration in characteristic two).** Let $R = \mathbb{F}_{2}$ with the identity involution, let $A = \mathbb{F}_{2}$ with the identity involution, and let $\varphi$ be the identity, so that $h(x,y) = xy$. Then $h$ is Hermitian, $h(y,x) = xy = h(x,y)$, and skew-Hermitian, $-1 = 1$ in $\mathbb{F}_{2}$, and it is not alternating, $h(1,1) = 1$; the involution $T$ of the functionals is the identity, so the two eigenspaces of the splitting coincide with the whole space and there is no splitting; and the only alternating compatible form is zero, $\varphi(xx^{*}) = \varphi(x^{2}) = \varphi(1) = 0$ forcing $\varphi = 0$.

*Proof.* The assertions are the computations displayed, $\varsigma = \mathrm{id}$ and $* = \mathrm{id}$ giving $T = \mathrm{id}$ and $z^{*} = z$; the splitting of the theorem above needs $\tfrac12$ and there is none in $\mathbb{F}_{2}$; the last statement is the dictionary at $x = 1$. $\square$

**Remark (the boundary of the classification).** The theorem is the algebra-level form of the exception that *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint*, §*Hermitian Forms over a Ring with Involution*, and *Unitary Geometry over a Field with Involution*, §*Definition and Matrices*, both record: in characteristic two the Hermitian, the skew-Hermitian and the alternating classes are not related by a splitting, the skew-Hermitian forms need not be alternating when the base involution is nontrivial, and the classical statement that a skew-Hermitian form is alternating, which is the case $\varsigma = \mathrm{id}$ of the corollary above, is a statement about $2$ being invertible.

## The Field Case

### The Forms on a Field

**Theorem (the forms on a field).** Let $K$ be a field with an involution $\varsigma$, let $A = K$ with the involution $* = \varsigma$, and let $h$ be a compatible form with functional $\varphi$. Then $\varphi$ is $K$-linear, so $\varphi(z) = cz$ for $c = \varphi(1) = h(1,1)$, and

$$
h(x,y) = c\,x\,\varsigma(y) , \qquad c \in K .
$$

Such a form is Hermitian exactly when $c \in K^{\varsigma}$, skew-Hermitian exactly when $\varsigma(c) = -c$, and alternating exactly when $c = 0$; the form with $c = 1$ is the trace form $h(x,y) = x\varsigma(y)$ of *Unitary Geometry over a Field with Involution*, §*Definition and Matrices*, whose norm is $x\varsigma(x)$.

*Proof.* A $K$-linear functional on the one-dimensional space $K$ is $z \mapsto cz$ with $c = \varphi(1)$, so $h(x,y) = \varphi(\varsigma(y)x) = c\,\varsigma(y)x = cx\varsigma(y)$; the involution of $K$ is the identity on $K^{\varsigma}$ and a nontrivial automorphism of order two otherwise. The Hermitian condition is $h(y,x) = cy\varsigma(x)$ equal to $\varsigma(cx\varsigma(y)) = \varsigma(c)\varsigma(x)y$ for all $x,y$, which is $c = \varsigma(c)$; the skew-Hermitian condition is $\varsigma(c) = -c$; and the alternating condition is $cx\varsigma(x) = 0$ for all $x$, which at $x = 1$ gives $c = 0$, and in particular the alternating forms are zero, since a field is an integral domain. $\square$

### The Two Kinds of Involution

**Remark (the two parts of the field and the kinds of involution).** The anti-fixed elements of a field with a nontrivial involution are nonzero as soon as $2$ is invertible, $t - \varsigma(t) \neq 0$ for $t$ outside the fixed field, so there are skew-Hermitian forms with nonzero diagonal, the diagonal of the theorem of §*The Dictionary of the Kinds*, and there are no alternating ones: on a field the alternating class is the zero class while the skew-Hermitian class is not. The Hermitian forms take their value in the fixed field, which is the field of scalars of the Hermitian geometry, and the classification of the involutions of a field into the trivial kind, the orthogonal geometry, and the nontrivial kind, the Hermitian geometry, is the one of *Unitary Geometry over a Field with Involution*, §*Definition and the Two Kinds*; the correspondence exhibits the forms of the layer as the fixed elements of that classification.

## The Collapse at the Trivial Involution

### The Bilinear Reading

**Theorem (the collapse).** Let $\varsigma = \mathrm{id}$ and suppose $2$ invertible. Then a compatible form is Hermitian exactly when it is symmetric, $h(y,x) = h(x,y)$; it is the bilinear form $h(x,y) = \varphi(yx)$ of the functional $\varphi$; and if $* = \mathrm{id}$ then the alternating compatible forms are zero and the Hermitian compatible forms are the symmetric bilinear forms $h(x,y) = \varphi(yx)$, which are the forms $h(x,y) = \varphi(xy)$ for a functional $\varphi$ central on products. The layer is then the bilinear degree-two layer: its objects are those of *Algebras with a degree-2 form*, its algebraic theory is *Bilinear Forms*, and the equivalence is the collapse of the entry, §*The Collapse at the Trivial Involution*.

*Proof.* At $\varsigma = \mathrm{id}$ the form is $R$-bilinear, $h(x,y) = \varphi(yx)$, and the Hermitian condition $h(y,x) = \varsigma(h(x,y)) = h(x,y)$ is the symmetry; the alternating forms are zero by the corollary of §*Alternating and the Symmetric Part* when $* = \mathrm{id}$, and the symmetric bilinear forms of the layer are exactly the forms $h(x,y) = \varphi(yx)$ whose functional is central on products, $\varphi(xy) = \varphi(yx)$, which is the correspondence at $* = \mathrm{id}$ read with the symmetry; the identification of the categories is the entry's collapse, whose objects are the involutive algebras with a compatible symmetric form. $\square$

**Remark.** The collapse is total: with $\varsigma = \mathrm{id}$ the conjugation disappears from the second slot, the two kinds Hermitian and skew-Hermitian become the symmetric and the alternating, the adjoint involution $h \mapsto h^{\dagger}$ becomes the transposition $h \mapsto h^{\intercal}$, $h^{\intercal}(x,y) = h(y,x)$, and the splitting of the forms becomes the classical decomposition of a bilinear form into its symmetric and its alternating parts. What does not collapse is the involution of the algebra: with $*$ nontrivial and $\varsigma = \mathrm{id}$ the Hermitian forms are the symmetric bilinear forms for which the multiplication is self-adjoint up to the involution, $h(xy,z) = h(y,x^{*}z)$, and that is the bilinear theory of *Bilinear Forms* with an involution in the algebra, not the trivial theory.

## Examples

### The Trace Pairing on the Matrices

**Example (the complex matrices, verdict: the trace pairing is the correspondence at $\varphi = \operatorname{tr}$).** Let $A = M_n(\mathbb{C})$, the involution the conjugate transpose, the base involution the conjugation, $\varphi = \operatorname{tr}$ and $h(X,Y) = \operatorname{tr}(XY^{*})$. Then $\varphi$ is real, $\varphi(Z^{*}) = \operatorname{tr}(Z^{*}) = \overline{\operatorname{tr}(Z)} = \varsigma(\varphi(Z))$, so $h$ is Hermitian by the dictionary; $h = h_{\varphi}$ because $\operatorname{tr}(Y^{*}X) = \operatorname{tr}(XY^{*})$; the diagonal is $\operatorname{tr}(XX^{*}) = \sum_{ij}\lvert X_{ij}\rvert^{2}$, in the fixed field $\mathbb{R}$; the radical is zero, $\operatorname{tr}(XX^{*}) = 0$ forcing $X = 0$; and the alternating compatible forms are zero, $\varphi(XX^{*}) = 0$ for every $X$ forcing $\varphi = 0$ on the positive semi-definite matrices, whose $\mathbb{C}$-span is all of $M_n(\mathbb{C})$, the functional being $\mathbb{C}$-linear. The verdict: the model of the layer is the correspondence at the trace, and the three kinds are the three conditions on the trace.

### The Field and the Split Algebra

**Example (the sesquilinear field, verdict: the forms are the multiples of the trace form).** Let $K = \mathbb{C}$ with the conjugation, $A = K$ and $h$ compatible. Then $h(x,y) = cx\bar y$ with $c = h(1,1)$ by the field theorem; $h$ is Hermitian exactly when $c \in \mathbb{R}$, skew-Hermitian exactly when $c \in i\mathbb{R}$, and alternating exactly when $c = 0$. The forms of the sesquilinear field are therefore the real multiples of $x\bar y$ and the purely imaginary multiples of it; the second family is the skew-Hermitian one and none of its members is alternating, the diagonal being $c\lvert x\rvert^{2} \neq 0$ for $c \neq 0$ and $x \neq 0$. The verdict: on a field the conjugation produces a two-parameter family of forms and the alternating class is the single zero form.

**Example (the alternating form of the split algebra, verdict: the alternating class is not zero).** Let $A = R \times R$ with the swap involution, $\varsigma = \mathrm{id}$, $\varphi(a,b) = a-b$ and $h(x,y) = da - cb$ as in §*Alternating and the Symmetric Part*. The form is skew-Hermitian, alternating and nonzero, and its rank is two. The verdict: as soon as the algebra involution is nontrivial the alternating class is larger than the zero form, and the example is the smallest one; it is the algebra-level companion of the skew-symmetric forms of *Bilinear Forms*, §*Symmetric, Alternating and Skew-Symmetric Forms*.

### The Characteristic-Two Degeneration

**Example (the characteristic two degeneration, verdict: the kinds merge and the splitting fails).** Over $\mathbb{F}_{2}$ with the identity involution, $A = \mathbb{F}_{2}$, $\varphi = \mathrm{id}$ and $h(x,y) = xy$: Hermitian, skew-Hermitian, not alternating, with $T = \mathrm{id}$ so that the splitting of §*The Conjugation on the Space of Forms* has no content. The verdict: the classification of the forms is a classification of the functionals only when $2$ is invertible, and in characteristic two the three classes must be distinguished without the splitting.

## Summary

A compatible form on a unital algebra is determined by its functional, $\varphi(x) = h(x,1)$, through $h(x,y) = \varphi(y^{*}x) = h(y^{*}x,1)$; the correspondence $\varphi \mapsto h_{\varphi}$ is a bijection from the $R$-linear functionals onto the compatible forms, inverse to $h \mapsto h(\cdot,1)$, and its continuous form, when the product and the involution are continuous, is Part II's. The compatibility of the entry is therefore a normalisation and not a restriction, and the pairings of the entry, $\tau(xy^{*})$ with $\tau$ central, are the forms $h_{\tau}$. The dictionary reads the kinds of the form on the functional: Hermitian is $\varphi(z^{*}) = \varsigma(\varphi(z))$, skew-Hermitian is $\varphi(z^{*}) = -\varsigma(\varphi(z))$, alternating is $\varphi(xx^{*}) = 0$; the diagonal of a Hermitian form is $h(x,x) = \varphi(x^{*}x)$, in the fixed ring, and it is $\varphi(xx^{*})$ when the functional is central on products, while the diagonal of a skew-Hermitian one is anti-fixed and need not vanish. With $2$ invertible an alternating form is anti-symmetric and its functional vanishes on the symmetric part $A^{+}$; with $\varsigma = \mathrm{id}$ the alternating and the skew-Hermitian classes coincide, with $* = \mathrm{id}$ they are the zero class, and with a nontrivial algebra involution the alternating class contains the form $h(x,y) = da - cb$ of the split algebra. The conjugation acts on the forms by $h^{\dagger}(x,y) = \varsigma(h(y,x))$, an involution whose fixed forms are the Hermitian ones and whose anti-fixed forms are the skew-Hermitian ones, and it corresponds to the involution $T\varphi = \varsigma\circ\varphi\circ{}^{*}$ of the functionals; with $2$ invertible every compatible form splits uniquely into a Hermitian and a skew-Hermitian part, and in characteristic two the split fails, the two kinds merge and the alternating class is strictly smaller, the form $h(x,y) = xy$ over $\mathbb{F}_{2}$ being Hermitian and skew-Hermitian and not alternating. On a field the compatible forms are the multiples $cx\varsigma(y)$ of the trace form, Hermitian exactly for $c$ in the fixed field and alternating only for $c = 0$. The radical is the annihilator $\{x : \varphi(Ax) = 0\}$, a left ideal whose image under the involution is $\{x : \varphi(Ax^{*}) = 0\}$. At $\varsigma = \mathrm{id}$ the forms are the bilinear forms $\varphi(yx)$, the involution $h \mapsto h^{\dagger}$ is the transposition, the splitting is the classical one, and the layer is the bilinear degree-two layer of *Bilinear Forms* and *Algebras with a degree-2 form*.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\varphi(x) = h(x,1)$ | the functional of a form |
| $h(x,y) = \varphi(y^{*}x) = h(y^{*}x,1)$ | the reconstruction of a compatible form |
| $\varphi \mapsto h_{\varphi}$ | the correspondence between functionals and compatible forms |
| $\varphi(z^{*}) = \pm\varsigma(\varphi(z))$ | the Hermitian, respectively skew-Hermitian, condition on the functional |
| $\varphi(xx^{*}) = 0$ | the alternating condition on the functional |
| $A^{+} = \{z : z = z^{*}\}$ | the symmetric part, on which an alternating functional vanishes when $2$ is invertible |
| $A^{\perp} = \{x : \varphi(Ax) = 0\}$ | the radical, a left ideal |
| $h^{\dagger}(x,y) = \varsigma(h(y,x))$ | the adjoint form, an involution of the space of forms |
| $T\varphi = \varsigma\circ\varphi\circ{}^{*}$ | the corresponding involution of the functionals |
| $\tfrac12(h \pm h^{\dagger})$, $\tfrac12(\varphi \pm T\varphi)$ | the Hermitian and the skew-Hermitian parts, when $2$ is invertible |
| $h(x,y) = cx\varsigma(y)$ | the compatible forms on a field, with $c = h(1,1)$ |
| $\varsigma = \mathrm{id}$ | the collapse to the bilinear forms $\varphi(yx)$ of *Bilinear Forms* |

## Further Reading

- Nicolas Bourbaki, *Algebra I*, Chapters 1–3 (Springer, 1989), for the sesquilinear and Hermitian forms, the involutions of a field and the classification of the forms.
- Winfried Scharlau, *Quadratic and Hermitian Forms*, Grundlehren der mathematischen Wissenschaften 270 (Springer, 1985), for the Hermitian forms over a field with involution and the exceptional characteristic.
- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings*, Grundlehren der mathematischen Wissenschaften 294 (Springer, 1991), for the $\varepsilon$-Hermitian forms over a ring with involution, the radical and the trace form.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for the algebras with involution and the forms they carry.
- Tsit-Yuen Lam, *Introduction to Quadratic Forms over Fields*, Graduate Studies in Mathematics 67 (American Mathematical Society, 2005), for the symmetric and the alternating forms and the role of $2$.
- Jean Dieudonné, *La géométrie des groupes classiques* (Springer, 1971), for the unitary and the symplectic geometries over fields with involution.
- Sterling K. Berberian, *Baer \*-Rings*, Grundlehren der mathematischen Wissenschaften 195 (Springer, 1972), for the real and the anti-real functionals and the involution they carry.
