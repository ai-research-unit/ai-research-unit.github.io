# __Hermitian Forms on a Sesqualgebra__

## Introduction

An algebra with an involution carries a form of degree two that costs nothing: the two-variable map $h_c(x,y) = c(x)y$ attached to an anti-involution $c$, whose Hermitian property is the definition of $c$ and nothing else, is the form of *Hermitian Forms on a Hermitian Algebra with Hermitian Adjoint*. A sesqualgebra carries such a form twice over. Its product is the derived operation $x \star y = xy^{*}$ of an associative algebra with a $\varsigma$-semilinear involution $*$, and the product itself, read as a two-variable map, is Hermitian:

$$
\Phi(x,y) = xy^{*}, \qquad \Phi(y,x) = yx^{*} = (xy^{*})^{*} = \Phi(x,y)^{*} .
$$

The conjugate map

$$
\Psi(x,y) = y^{*}x
$$

is Hermitian as well, and it is the one whose scalar reductions are the compatible forms of *The Sesquilinear Form and the Conjugation*: a compatible form is $h_{\varphi}(x,y) = \varphi(y^{*}x) = \varphi(\Psi(x,y))$ for one $R$-linear functional $\varphi$, so $\Psi$ is the universal form of the layer and the scalar theory is its reduction by functionals.

Two facts organise the article. **The $A$-valued form is read by the annihilators.** The radical of $\Psi$ is the left annihilator $\{x : Ax = 0\}$ and the radical of $\Phi$ is the right annihilator $\{x : xA = 0\}$ of *Left and Right Multiplication in a Ring*, §*The annihilators*, and the involution carries each onto the other, so the two vanish together and the nondegeneracy of the two forms is a single condition; that condition is one of the three clauses in the definition of the objects of full type of *Sesqualgebras*, §*The Collapse at the Identity*, so full type gives the nondegeneracy of both forms, and the converse fails, the clause being only one of the three. And **the two forms are exchanged by the involution**,

$$
\Psi(x,y) = \Phi(y^{*},x^{*}), \qquad \Phi(x,y) = \Psi(y^{*},x^{*}),
$$

so the pair $(\Phi,\Psi)$ is a single object read through the involution: $\Psi$ is the form in the convention of the sesqualgebra, linear in the first slot and $\varsigma$-semilinear in the second, and the convention of the cited sibling, semilinear in the first slot, is the same form with the two arguments exchanged.

The article defines the $A$-valued Hermitian form and the two orientations of its slots, proves the Hermitian property, the diagonal proposition and the exchange relation, identifies the product with the form and the scalar forms with the reductions, computes the two radicals and their identification with the annihilators, treats the form induced on a quotient by an invariant ideal, and compares the result with the bilinear layer, with the collapse at $\varsigma = \mathrm{id}$ closing the article. The scalar forms and their three kinds are *The Sesquilinear Form and the Conjugation*, the compatibility and its radical *Sesqualgebras with a Form*, the positivity of the diagonal *Positivity and the Positive Cone of a Hermitian Form*, the operator that the form adjoints *The Adjoint under a Hermitian Form*, the ternary product *Algebraic J\*-Algebras*, and the layer without a form *Topological Sesqualgebras*. Throughout, $A$ is an associative $R$-algebra with $1$ and a $\varsigma$-semilinear involution $*$, and $(A,\star)$ is the sesqualgebra $x \star y = xy^{*}$ of *Sesqualgebras*.

## The Form Carried by the Algebra

### The Definition

**Definition.** Let $A$ be an associative $R$-algebra with a $\varsigma$-semilinear involution $*$. An $A$-**valued sesquilinear form** on $A$ is a biadditive map $\Psi : A \times A \to A$ with

$$
\Psi(\lambda x, y) = \lambda\,\Psi(x,y), \qquad \Psi(x, \lambda y) = \varsigma(\lambda)\,\Psi(x,y)
$$

for all $\lambda \in R$ and all $x, y \in A$. It is **Hermitian** when $\Psi(y,x) = \Psi(x,y)^{*}$ for all $x, y$, and its **radical** is

$$
\operatorname{rad}(\Psi) = \{x \in A : \Psi(x,y) = 0 \text{ for all } y \in A\} .
$$

The definition is that of the entry's sesquilinear form with the scalars $R$ replaced by the algebra $A$ as the target, so the form is a rule that multiplies and not a rule that takes a length; the two slot rules are those of a sesqualgebra product, and the Hermitian property is read with the involution of $A$ in place of the involution $\varsigma$ of the base.

**Proposition (the two forms of the algebra).** The maps

$$
\Psi(x,y) = y^{*}x, \qquad \Phi(x,y) = xy^{*}
$$

are $A$-valued sesquilinear forms on $A$, both Hermitian, and they satisfy

$$
\Psi(x,y) = \Phi(y^{*},x^{*}), \qquad \Phi(x,y) = \Psi(y^{*},x^{*}) .
$$

*Proof.* In the first slot, $\Psi(\lambda x,y) = y^{*}(\lambda x) = \lambda(y^{*}x)$ by the $R$-bilinearity of the product, and $\Psi(x,\lambda y) = (\lambda y)^{*}x = \varsigma(\lambda)y^{*}x$ by the semilinearity of the involution; the two computations for $\Phi$ are the same with the roles of the slots exchanged, $\Phi(\lambda x,y) = (\lambda x)y^{*} = \lambda(xy^{*})$ and $\Phi(x,\lambda y) = x(\lambda y)^{*} = \varsigma(\lambda)(xy^{*})$, so $\Phi$ is $\varsigma$-semilinear in the second slot as required. The Hermitian property is $\Psi(y,x) = x^{*}y$ against $\Psi(x,y)^{*} = (y^{*}x)^{*} = x^{*}y$, using $(uv)^{*} = v^{*}u^{*}$ and $*^{2} = \mathrm{id}$, and $\Phi(y,x) = yx^{*}$ against $\Phi(x,y)^{*} = (xy^{*})^{*} = yx^{*}$. The exchange relation is $\Phi(y^{*},x^{*}) = y^{*}(x^{*})^{*} = y^{*}x = \Psi(x,y)$ and the second identity is the first read with $x, y$ replaced by $x^{*}, y^{*}$. $\square$

**Remark (the two orientations).** The two forms carry the same datum in the two conventions of the two slots: $\Psi$ is linear in the first slot and $\varsigma$-semilinear in the second, $\Phi$ likewise, and the exchange relation says that applying the involution to both arguments turns one into the other. The convention of the sesqualgebra is the one of $\Psi$ and $\Phi$, and the convention of *Hermitian Forms on a Hermitian Algebra with Hermitian Adjoint*, in which the form $h_c(x,y) = c(x)y$ is semilinear in the first slot, is the same convention read with the arguments exchanged: with $c = *$ that form is $x^{*}y = \Psi(y,x)$.

### The Diagonal

**Proposition (the diagonal).** For every $x$ the elements

$$
\Psi(x,x) = x^{*}x, \qquad \Phi(x,x) = xx^{*} = x \star x
$$

are Hermitian, $\Psi(x,x)^{*} = \Psi(x,x)$ and $\Phi(x,x)^{*} = \Phi(x,x)$.

*Proof.* $(y^{*}x)^{*} = x^{*}y = \Psi(y,x)$ with $y = x$ gives the first, and $(xx^{*})^{*} = xx^{*} = \Phi(x,x)$ gives the second; the identification $x \star x = xx^{*}$ is the derived product with equal arguments, so the second diagonal is the Hermitian square of *Hermitian Squares and the Algebraic Positive Cone*. $\square$

**Proposition (polarisation).** For all $x, y$,

$$
\Psi(x+y,x+y) = \Psi(x,x) + \Psi(x,y) + \Psi(y,x) + \Psi(y,y),
$$

and the same identity holds with $\Phi$ in place of $\Psi$.

*Proof.* The form is additive in each variable, so the left side expands into the four terms, and the two mixed terms are the values of the form on the mixed pairs. $\square$

**Remark.** The polarisation displays the two summands $\Psi(x,y)$ and $\Psi(y,x) = \Psi(x,y)^{*}$ into which a scalar form would split, and it is the reason the symmetrised and the antisymmetrised forms of the two slots are the natural companions of the diagonal. A scalar reduction of the identity is the polarisation of the quadratic form of the next section, and the scalar form of the layer is the one of *The Sesquilinear Form and the Conjugation*.

### The Form Is the Product

**Proposition (the compatibility is an identity).** The $A$-valued form $\Psi$ is compatible with the product, in the sense of *Sesqualgebras with a Form*, §*The Compatibility*:

$$
\Psi(xy,z) = \Psi(y, x^{*}z)
$$

for all $x, y, z \in A$.

*Proof.* Both sides are the same element of $A$: $\Psi(xy,z) = z^{*}(xy) = z^{*}xy$ and $\Psi(y,x^{*}z) = (x^{*}z)^{*}y = z^{*}xy$, the middle equality being the associativity of the underlying product and the semilinearity of the involution. $\square$

**Proposition (the forms and the products coincide).** Let $A$ be an associative $R$-algebra with a $\varsigma$-semilinear involution $*$. Then the derived operation is the $A$-valued form $\Phi$,

$$
x \star y = xy^{*} = \Phi(x,y) ,
$$

and every sesquilinear product $\circ$ on $A$ with the Hermitian property $(x \circ y)^{*} = y \circ x$ is an $A$-valued Hermitian form, and conversely every $A$-valued Hermitian form is a product with that property.

*Proof.* The derived operation is $x \star y = xy^{*}$ by definition, which is $\Phi$; it is additive in each variable and satisfies the two slot rules, so it is an $A$-valued sesquilinear form, and it is Hermitian because $(x \star y)^{*} = (xy^{*})^{*} = yx^{*} = y \star x$. For the converse, a product $\circ$ additive in each variable and satisfying the two slot rules is an $A$-valued sesquilinear form by the definition, and the Hermitian property is exactly the condition displayed, so the two notions coincide. $\square$

**Remark.** The theorem is the sense in which a sesqualgebra carries a form and not merely a product: the product **is** the form $\Phi$, the compatibility of the entry holds for the companion $\Psi$ as an identity of the algebra and not as a hypothesis, and the two derivations of the layer, the algebraic one of *Sesqualgebras* and the form-theoretic one, are the same derivation. The sibling statement for the scalar layer is the correspondence of *The Sesquilinear Form and the Conjugation*, and the two are related by the reduction of the next section.

## The Reduction to the Scalars

### The Compatible Forms

**Proposition (the reduction, quoted from *The Sesquilinear Form and the Conjugation*).** Let $\varphi : A \to R$ be $R$-linear. Then

$$
h_{\varphi}(x,y) = \varphi(\Psi(x,y)) = \varphi(y^{*}x)
$$

is a sesquilinear form on $A$, compatible with the product in the sense $h_{\varphi}(xy,z) = h_{\varphi}(y,x^{*}z)$, and every compatible form arises from exactly one functional in this way. The passage $\varphi \mapsto \varphi \circ \Psi$ is therefore a bijection from the $R$-linear functionals onto the compatible forms.

*Proof.* The form $h_{\varphi}$ is the composite of the $A$-valued form $\Psi$ with the $R$-linear functional $\varphi$, so it is additive in each variable and inherits the two slot rules from the proposition, and the rest is the correspondence of *The Sesquilinear Form and the Conjugation*, §*The Correspondence*: the injectivity is $\varphi(x) = h_{\varphi}(x,1)$, and the surjectivity is the reconstruction $h(x,y) = h(y^{*}x,1)$ of §*The Reconstruction*. The statement is quoted and not reproved, the theory of the scalar forms being that article's. $\square$

**Remark.** The proposition separates the two layers of the article: the $A$-valued form $\Psi$ is the universal object, the scalar functional is the measuring device, and the compatible forms of the entry are its scalar reductions. A theory of the scalar forms is therefore a theory of the functionals, which is the reason the classification of *The Sesquilinear Form and the Conjugation* reads on $\varphi$ and not on $h$.

### The Central Case

**Proposition.** The two reductions of the two $A$-valued forms agree,

$$
\varphi(\Phi(x,y)) = \varphi(\Psi(x,y))
$$

for all $x, y$, exactly when $\varphi$ is central on products, $\varphi(uv) = \varphi(vu)$.

*Proof.* The identity for all $x, y$ is $\varphi(xy^{*}) = \varphi(y^{*}x)$, and since $y \mapsto y^{*}$ is a bijection of $A$, writing $v = y^{*}$ turns it into $\varphi(xv) = \varphi(vx)$ for all $x, v$, which is the centrality; conversely the centrality gives the identity by the same substitution. $\square$

**Remark.** The two $A$-valued forms therefore agree on the scalar side exactly on the central functionals, which is the class for which the trace pairing $\varphi(x,y) = \tau(xy^{*})$ of *The Sesquilinear Adjoint Operator*, §*The Two Parities* coincides with the reduction $h_{\tau}(x,y) = \tau(y^{*}x)$, the sesqui-symmetry $\varphi(y,x) = \varsigma(\varphi(x,y))$ of that section being the Hermitian property read on the pairing; the trace of the matrix model is the model of the class.

## Nondegeneracy

### The Two Radicals

**Theorem (the radicals are the annihilators).** The radicals of the two $A$-valued forms are

$$
\operatorname{rad}(\Psi) = \{x : Ax = 0\}, \qquad \operatorname{rad}(\Phi) = \{x : xA = 0\} ,
$$

the left and the right annihilators of the algebra. Consequently $\Psi$ is nondegenerate exactly when $A$ has no nonzero left annihilator, and $\Phi$ exactly when it has no nonzero right annihilator.

*Proof.* The condition $\Psi(x,y) = y^{*}x = 0$ for every $y$ reads $zx = 0$ for every $z$, because $y \mapsto y^{*}$ is a bijection of $A$, which is $\{x : Ax = 0\}$; the condition $\Phi(x,y) = xy^{*} = 0$ for every $y$ reads $xz = 0$ for every $z$, which is $\{x : xA = 0\}$. The two sets are the annihilators of the statement. $\square$

**Remark.** The radical of $\Psi$ is the left annihilator, and it is a two-sided ideal: if $Ax = 0$ then $A(xa) = 0$ and $A(ax) = (Aa)x \subseteq Ax = 0$ for every $a$. The radical of $\Phi$ is the right annihilator and is two-sided on the same computation. The two are interchanged by the involution, since $\{x : xA = 0\}^{*} = \{x^{*} : xA = 0\} = \{u : u^{*}A = 0\}$, and the last condition is $\{u : Au = 0\}$ read through the anti-multiplicativity of $*$: the two radicals are the two halves of one set under $*$.

### Full Type and the Converse

**Corollary.** An object of full type in the sense of *Sesqualgebras*, §*The Collapse at the Identity* has no nonzero annihilator, so its two forms $\Psi$ and $\Phi$ are nondegenerate; in particular the forms of a unital $R$-algebra with an involution are nondegenerate.

*Proof.* Full type is faithfulness over $R$, generation of $A$ by the products and the vanishing of the annihilator, the clause quoted in the entry as "no nonzero element of $A$ annihilates $A$ on the left". That clause is the vanishing of $\{x : xA = 0\} = \operatorname{rad}(\Phi)$, and the remark above shows that the image of this set under $*$ is $\{u : Au = 0\} = \operatorname{rad}(\Psi)$; since $*$ is a bijection, the two sets vanish together and each of the two forms is nondegenerate. For a unital algebra, taking $z = 1$ in $zx = 0$ and in $xz = 0$ gives $x = 0$ in both cases, so both annihilators are zero. $\square$

**Remark (the naming of the two annihilators).** The two sets are named in opposite directions by two usages of the corpus, and the coincidence of their vanishing is what makes the ambiguity harmless. In the sense of *Left and Right Multiplication in a Ring*, §*The annihilators*, the left annihilator is the kernel of the left multiplication, $\{x : Ax = 0\} = \operatorname{rad}(\Psi)$, and the right annihilator is $\{x : xA = 0\} = \operatorname{rad}(\Phi)$; the phrase "no nonzero element of $A$ annihilates $A$ on the left" names the second set by the side on which the multiplication is written, and the two sets are carried onto each other by the involution. Only the vanishing is used below, and it is a property of both forms at once, so nothing depends on which of the two names is read.

**Remark (the converse fails).** Nondegeneracy of the two forms does not give full type, because the forms read only one of the three clauses: they record the vanishing of the annihilator and see neither the faithfulness over $R$ nor the generation of $A$ by the products. The clause that fails in the smallest **unital** example is the faithfulness: let $R = \mathbb{Z}$, let $A = \mathbb{Z}/2\mathbb{Z}$ be the two-element ring as a unital $\mathbb{Z}$-algebra, with the ordinary product, the identity involution and $\varsigma = \mathrm{id}$. The products generate $A$ and the annihilator vanishes, since $xy = 0$ with $y = 1$ forces $x = 0$, so the forms $\Psi(x,y) = yx$ and $\Phi(x,y) = xy$ are nondegenerate; while $2 \cdot A = 0$ with $2 \neq 0$, so $\operatorname{ann}_{R}(A) = 2\mathbb{Z} \neq 0$ and $A$ is not faithful over $R$, hence not of full type. The generation clause is the one that fails only when $A$ is allowed to be non-unital: the ideal $(x)$ of $K[x]$ over a field $K$, with the ordinary product and the identity involution, has products generating the proper ideal $(x^{2})$ and its two forms are nondegenerate as well. The independence of the scalar layer is a different statement: the nondegenerate form of the zero product of *Sesqualgebras with a Form*, §*Full Type and Nondegeneracy* is the scalar form $h(z,w) = z\varsigma(w)$, whose radical vanishes because $h(z,1) = z$, while the $A$-valued form of the same object is the zero form, the annihilator being all of $A$; the scalar and the $A$-valued nondegeneracy are therefore genuinely different conditions, and it is the scalar one that is independent of full type.

### The Induced Form on a Quotient

**Theorem.** Let $J$ be a two-sided ideal of $A$ with $J^{*} = J$. Then the two forms descend to $A/J$ and make it an associative $R$-algebra with the induced involution and the induced $A/J$-valued Hermitian forms, and the radical of the descended form is the annihilator of the quotient,

$$
\operatorname{rad}(\Psi_{A/J}) = \{x + J : (A/J)(x + J) = 0\} .
$$

*Proof.* The value $\Psi(x+j,y) = y^{*}(x+j) = y^{*}x + y^{*}j$ lies in $\Psi(x,y) + J$ because $J$ is a right ideal, and $\Psi(x,y+j') = (y+j')^{*}x = y^{*}x + (j')^{*}x$ lies in $\Psi(x,y) + J$ because $J^{*} = J$ and $J$ is a left ideal, so the descended map is well defined; it is sesquilinear and Hermitian because the operations of $A/J$ are. Its radical is the set of the classes $x + J$ with $(y + J)^{*}(x + J) = 0$ for every $y$, and $(y+J) \mapsto (y+J)^{*}$ is a bijection of the quotient because $J^{*} = J$, so the condition reads $zx = 0$ in $A/J$ for every $z$, which is the stated annihilator. $\square$

**Remark.** The hypothesis $J^{*} = J$ is what makes the descent possible and is not automatic: for a general two-sided ideal the classes of $x$ and of $x + j$ have different images under $\Psi$, because $y^{*}j$ need not lie in $J$. The invariant ideals are the ones for which the quotient of the entry, §*The Radical Is an Ideal* carries the form, and the radical of the entry, a left ideal of $A$ whose image under $*$ is a right ideal, is exactly the set that must be divided out to make the scalar form nondegenerate.

## The Bilinear Comparison

### The Form of an Anti-Involution

**Proposition.** Let $c$ be an anti-involution of $A$ and let $h_c(x,y) = c(x)y$ be the Hermitian form of *Hermitian Forms on a Hermitian Algebra with Hermitian Adjoint*, §*The Form Attached to an Anti-Involution*. Then $h_*$ is the exchange of the $A$-valued form $\Psi$,

$$
h_*(x,y) = x^{*}y = \Psi(y,x),
$$

and the two differ only by the order of the arguments, which is the difference between the convention of *Hermitian Algebras*, semilinear in the first slot, and the sesqualgebra convention, linear in the first.

*Proof.* The sibling's definition with $c = *$ is $h_*(x,y) = x^{*}y$, and $\Psi(y,x) = x^{*}y$ is the proposition at the top of the article. $\square$

**Remark.** The comparison locates the new content of the sesqualgebra layer: the sibling's forms are attached to an arbitrary anti-involution of a ring and need no sesquilinear product, whereas the forms of this article are attached to the involution of an algebra that carries the sesquilinear product, and the exchange relation is the passage between the two. The three forms of the sibling, reversion, Clifford conjugation and the dagger, are the three anti-involutions of a Clifford algebra; the two forms of this article are the two orientations of the single involution.

### The Collapse

**Theorem.** Let $\varsigma = \mathrm{id}$ and $* = \mathrm{id}$. Then the two $A$-valued forms are the two products

$$
\Psi(x,y) = yx, \qquad \Phi(x,y) = xy,
$$

both $A$-bilinear, and the reduction $\varphi \circ \Psi$ is the bilinear form $\varphi(yx)$ of *Bilinear Forms* associated with the functional $\varphi$; the two radicals are the two annihilators of the algebra.

*Proof.* With $\varsigma = \mathrm{id}$ the two slot rules coincide and the forms are $A$-bilinear; with $* = \mathrm{id}$ the involution is the identity, so $\Psi(x,y) = yx$ and $\Phi(x,y) = xy$, the two orientations of the multiplication. The reduction is the composite of the product with $\varphi$, which is the form $\varphi(yx)$ of the bilinear layer, and the radicals are the theorem of the previous section with $* = \mathrm{id}$. $\square$

**Remark.** The collapse is total at the level of the forms: the pair $(\Phi,\Psi)$ becomes the two products of the algebra, the Hermitian property becomes the commutativity of the two orientations, which holds only when $A$ is commutative, and the scalar forms become the forms $\varphi(yx)$ of the bilinear layer. The one thing the collapse does not remove is the asymmetry of the two slots: over a noncommutative algebra the two forms $\Phi$ and $\Psi$ are the two products $xy$ and $yx$, and they agree exactly when the algebra is commutative, which is the bilinear shadow of the exchange relation.

## Examples

### The Matrices

**Example (the matrix algebra, verdict: the form is nondegenerate and its diagonal is the positive cone).** Let $A = M_n(\mathbb{C})$, let $*$ be the conjugate transpose and let $\varsigma$ be the conjugation. Then

$$
\Psi(X,Y) = Y^{*}X, \qquad \Psi(X,X) = X^{*}X,
$$

the diagonal is a positive semi-definite matrix, of trace $\operatorname{tr}(X^{*}X) = \sum_{i,j} \lvert X_{ij}\rvert^{2}$, and the form is nondegenerate: if $X \neq 0$ then $X^{*}X \neq 0$, because the trace of $X^{*}X$ is a sum of squares of moduli, so the left annihilator vanishes. The diagonal at $n=2$ is

$$
X=\begin{pmatrix}1&i\\0&2\end{pmatrix},\qquad X^{*}X=\begin{pmatrix}1&i\\-i&5\end{pmatrix},\qquad \operatorname{tr}(X^{*}X)=6=\lvert1\rvert^{2}+\lvert i\rvert^{2}+\lvert0\rvert^{2}+\lvert2\rvert^{2},
$$

the matrix Hermitian with the positive diagonal $(1,5)$. The verdict: the $A$-valued form of the matrix algebra is the matrix-valued inner product of the sibling *Hermitian Forms on a Hermitian Algebra with Hermitian Adjoint*, its diagonal is the cone of *Hermitian Squares and the Algebraic Positive Cone*, and its nondegeneracy is the properness of that cone read on the algebra.

### The Field and the Split Algebra

**Example (the field with an involution, verdict: nondegenerate and anisotropic).** Let $A = K$ be a field with an involution $\varsigma$ and let $* = \varsigma$ on $K$. Then $\Psi(x,y) = \varsigma(y)x$, the diagonal is $\varsigma(x)x \in K^{\varsigma}$, and the form is nondegenerate: the radical is $\{x : Kx = 0\} = 0$, since $K$ is a field and $y \mapsto \varsigma(y)$ is a bijection. The form is anisotropic as well, $\varsigma(x)x = 0$ forcing $x = 0$, because $\varsigma(x)x = 0$ with $x \neq 0$ would exhibit $x$ as a zero divisor; for $\mathbb{C}$ with the conjugation the diagonal is $\lvert x\rvert^{2}$, and the scalar reductions are $h_{\varphi}(x,y) = \varphi(\varsigma(y)x)$. The verdict: on a field the $A$-valued form is nondegenerate and anisotropic at once, in contrast with the split algebra below, where the two properties separate.

**Example (the split algebra, verdict: nondegenerate and isotropic, the two conditions differ).** Let $A = R \times R$ with the componentwise product and the swap involution $(a,b)^{*} = (b,a)$. Then

$$
\Psi\bigl((a,b),(c,d)\bigr) = (d,c)(a,b) = (da, cb),
$$

so the radical is $\{(a,b) : da = 0 \text{ for all } d,\ cb = 0 \text{ for all } c\} = \{0\}$ and the form is nondegenerate; but the diagonal

$$
\Psi\bigl((a,b),(a,b)\bigr) = (b,a)(a,b) = (ab, ab)
$$

vanishes for every zero divisor, $a = 0$ or $b = 0$. The verdict: an $A$-valued form can be nondegenerate and carry nonzero isotropic vectors, so nondegeneracy and anisotropy are different conditions already on the smallest algebra, and the isotropic set is the union of the two coordinate axes, the zero divisors of the split algebra.

### The Biquaternion Algebra

**Example (the biquaternion algebra).** Let $A = \mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ with the star ${}^{*}$ of *Introduction to the General Plain Sesqualgebra of Biquaternions* and let $\varsigma$ be the conjugation. Then $\Psi(P,Q) = Q^{*}P$, the diagonal is $Q^{*}Q$, of scalar part $\sum_{\mu} \lvert Q_{\mu}\rvert^{2}$, and the form is nondegenerate because the algebra is unital and its unit annihilates nothing on the left: the left annihilator vanishes. The verdict: the corpus's own algebra carries the $A$-valued form $\Psi$, whose diagonal is the Hermitian form of *Biquaternion Norm and Invertibility*, with the sum of the modulus squares for scalar part, and whose scalar reduction by the scalar part is the form $\mathrm{Sc}(Q^{*}Q')$ of *The Form on the Biquaternion Algebra as a General Plain Sesquilinear Form*.

### The Characteristic-Two Case

**Example (the identity involution in characteristic two, verdict: the two forms coincide).** Let $R = \mathbb{F}_{2}$, let $A = \mathbb{F}_{2}$ with the identity involution and let $\varsigma = \mathrm{id}$. Then $\Psi(x,y) = yx = xy = \Phi(x,y)$, the two orientations coincide because the algebra is commutative, the diagonal is $x^{2} = x$, every element is Hermitian, and the form is $\Psi(x,y) = xy$, nondegenerate on the field. The verdict: in characteristic two with the identity datum the two $A$-valued forms are one form and it is the product, so the pair $(\Phi,\Psi)$ has no independent content there, exactly as the two kinds of scalar form merge in *The Sesquilinear Form and the Conjugation*, §*The Failure When $2$ Is Not Invertible*.

## Summary

An associative $R$-algebra $A$ with a $\varsigma$-semilinear involution $*$ carries two $A$-**valued Hermitian forms**, the form of the sesqualgebra $\Psi(x,y) = y^{*}x$ and the form of the product $\Phi(x,y) = xy^{*} = x \star y$, both biadditive, $R$-linear in the first slot and $\varsigma$-semilinear in the second, both Hermitian, $\Psi(y,x) = \Psi(x,y)^{*}$ and the same for $\Phi$, and exchanged by the involution applied to both arguments, $\Psi(x,y) = \Phi(y^{*},x^{*})$. The product of the sesqualgebra **is** the form $\Phi$, so the compatibility of the entry is an identity of the algebra for the companion form and not an extra axiom, and the pair is a single object read through the involution, in the two conventions of the two slots: $\Psi$ is the sesqualgebra convention, linear in the first slot, and the convention of *Hermitian Forms on a Hermitian Algebra with Hermitian Adjoint*, which is the same form with the arguments exchanged, is semilinear in the first slot: with the anti-involution $c = *$ that sibling's form is $h_*(x,y) = x^{*}y = \Psi(y,x)$.

The scalar forms of the layer are the reductions of $\Psi$ by the $R$-linear functionals, $h_{\varphi}(x,y) = \varphi(y^{*}x) = \varphi(\Psi(x,y))$, and the passage $\varphi \mapsto \varphi \circ \Psi$ is a bijection onto the compatible forms, with inverse $h \mapsto h(\cdot,1)$; the two $A$-valued forms have the same reduction exactly for the functionals central on products, which is the class for which the trace pairing $\varphi(x,y) = \tau(xy^{*})$ of *The Sesquilinear Adjoint Operator*, §*The Two Parities* agrees with the reduction $h_{\tau}$. **The diagonals** are $\Psi(x,x) = x^{*}x$ and $\Phi(x,x) = xx^{*} = x \star x$, both Hermitian, and the polarisation of the form splits into the two mixed terms $\Psi(x,y)$ and $\Psi(x,y)^{*}$.

**The radicals are the annihilators**, $\operatorname{rad}(\Psi) = \{x : Ax = 0\}$ and $\operatorname{rad}(\Phi) = \{x : xA = 0\}$, the left and the right annihilators of the algebra in the sense of *Left and Right Multiplication in a Ring*, §*The annihilators*, two-sided ideals carried onto each other by the involution, so that their vanishing — and hence the nondegeneracy of the two forms — is a single condition; the vanishing of the annihilator is one clause of the objects of **full type**, so full type gives the nondegeneracy of both forms and the converse fails, the two-element ring $\mathbb{Z}/2\mathbb{Z}$ over $R = \mathbb{Z}$ with the identity involution being nondegenerate and not of full type because it is not faithful over $R$, and the ideal $(x)$ of $K[x]$ being the non-unital variant; the nondegeneracy of the *scalar* forms is the independent condition, as the zero product shows. A **$*$-invariant two-sided ideal** $J$, $J^{*} = J$, is exactly what is needed to descend the two forms to the quotient $A/J$ and to keep the algebra and the involution on it, and the radical of the descended form is the annihilator of the quotient. At $\varsigma = \mathrm{id}$ and $* = \mathrm{id}$ the pair collapses to the two products $\Psi(x,y) = yx$ and $\Phi(x,y) = xy$ and the scalar forms are the bilinear forms $\varphi(yx)$ of *Bilinear Forms*, the two orientations agreeing only on a commutative algebra.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\Psi(x,y) = y^{*}x$ | the Hermitian form of the sesqualgebra, linear in the first slot and $\varsigma$-semilinear in the second |
| $\Phi(x,y) = xy^{*} = x \star y$ | the conjugate form, the derived operation read as a form |
| $\Psi(y,x) = \Psi(x,y)^{*}$ | the Hermitian property, and its analogue for $\Phi$ |
| $\Psi(x,y) = \Phi(y^{*},x^{*})$ | the two forms exchanged by the involution |
| $\Psi(x,x) = x^{*}x$, $\Phi(x,x) = xx^{*}$ | the diagonals, Hermitian elements |
| $h_{\varphi}(x,y) = \varphi(y^{*}x) = \varphi(\Psi(x,y))$ | the scalar reduction, the compatible form of a functional $\varphi$ |
| $\operatorname{rad}(\Psi) = \{x : Ax = 0\}$ | the left annihilator, a two-sided ideal |
| $\operatorname{rad}(\Phi) = \{x : xA = 0\}$ | the right annihilator, a two-sided ideal |
| $J^{*} = J$ | the invariant ideal for which the forms descend to $A/J$ |
| $h_c(x,y) = c(x)y$ | the form of the bilinear layer of *Hermitian Forms on a Hermitian Algebra with Hermitian Adjoint* |
| $\varsigma = \mathrm{id}$, $* = \mathrm{id}$ | the collapse: $\Psi(x,y) = yx$, $\Phi(x,y) = xy$ |

## Further Reading

- Sterling K. Berberian, *Baer \*-Rings* (Springer, 1972), for the algebra-valued form $h(x,y) = x^{*}y$, the annihilators and the one-sided ideals they generate.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the involutions of an algebra with a nontrivial involution and the forms they carry.
- Winfried Scharlau, *Quadratic and Hermitian Forms* (Springer, 1985), for the scalar Hermitian forms and the invariants of their diagonal.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, volume 1 (Academic Press, 1983), for the two-sided ideals of an involutive algebra and the annihilators of the regular representation.
- Irving Kaplansky, *Rings of Operators* (Benjamin, 1968), for the linear and the conjugate-linear parts of an involutive algebra and the forms they carry.
- Cho-Ho Chu, *Jordan Structures in Geometry and Analysis* (Cambridge University Press, 2012), for the Hermitian square and the ternary product, whose algebraic reading is *Algebraic J\*-Algebras*.
