# __The Axis-Free Construction of the Biquaternion Algebra__

## Introduction

**The claim.** The biquaternion algebra is fixed by the same four units as the quaternion algebra, one central imaginary $i$, and the same ten statements on the units, read with complex coefficients. The three vector units enter the data in the same way, the scalar $i$ is central and names no direction, and the construction therefore names no axis.

**The route it improves on.** The doubling of *The Cayley–Dickson Construction of the Biquaternion Algebra* builds the algebra as a stack of three layers: $\mathbb{R}$ to $\mathbb{C}$ by adjoining $\vec e_z$, $\mathbb{C}$ to $\mathbb{H}$ by adjoining $\vec e_x$ with the twist, and $\mathbb{H}$ to $\mathbb{B}$ by a scalar extension with $i$. That stack is correct and complete. It also fixes a rank at its first rung and keeps it at the second, and it presents the central imaginary $i$ as a third layer, added to a construction that already carries a direction. This article declares the four units and the scalar $i$ at once, and obtains the table directly.

**Why the order is worth a separate article.** A reader of the stack learns that one direction is a field and another is a generator, and then that a complex scalar is stacked on top. The algebra teaches neither. The three squares are equal, the cyclic symmetry of the table is exact, no vector unit is a coefficient field, and $i$ commutes with everything. The axis-free route states all four at the start. The cost of the stack is not an error but a misplaced emphasis: a reader cannot tell which features are the algebra's and which are the way the algebra was reached.

**What is left over, and what it costs.** One bit, the same one as for the quaternion algebra: the table needs a cyclic order of the three vector units, and a cyclic order is an orientation and not a direction. The central imaginary adds a second two-element choice, the sign of $i$, and that one is absorbed by the coefficientwise conjugation, which is an automorphism of the algebra and exchanges $i$ with $-i$. Neither bit costs anything. §*What Is Free and What Is Fixed* proves both absorptions.

**The tensor product becomes a theorem.** The base article *Introduction to the Algebra of Biquaternions* defines $\mathbb{B}$ as $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ and derives the table from the tensor product. This article runs the argument the other way: it declares the table, proves the algebra axioms, and then derives the tensor product from the coefficient rule. The two routes reach the same object, and the second shows that the tensor product is a consequence of the coefficient field and not a construction step.

**What the article contains.** §*The Data* states the four units and the central scalar. §*The Product* gives the rule and shows that complex bilinearity is the whole of the difference from the quaternion algebra. §*The Table* prints the sixteen products. §*The Tensor Product as a Theorem* derives the tensor product. §*Associativity* proves associativity from the four left multipliers, now complex matrices, and records what that display says about the algebra. §*The First Properties* gives the centre, the four conjugations, the two sectors, the norm, the zero divisors, the idempotents and the commutator. §*What Is Free and What Is Fixed* accounts for the two bits. §*The Contrast with the Stack* sets the two constructions side by side.

**The overlap, declared.** The table, the ten statements and several of the properties below overlap *Introduction to the Algebra of Biquaternions* and the doubling article. A construction must produce the object those articles use. What this article adds is the order of the argument, the associativity proof inside the coefficient display, the derivation of the tensor product, and the accounting of what is chosen and what is forced.

**Boundaries.** The algebra as a structure, with its scalar extension, its centre, its structure map and the absence of division, is *Introduction to the Algebra of Biquaternions*, above this article in this category. The stack of three layers is *The Cayley–Dickson Construction of the Biquaternion Algebra*, beside this one. The element, its three coordinate systems and the four conjugations are *The Element, the Coordinates and the Conjugations in the Biquaternion Algebra*; the annihilators and the unit criterion are *Zero Divisors and Invertibles in the Biquaternion Algebra*; the forms and their algebraic norms are *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*; the square of an element and its roots are *The Square of an Element in the Biquaternion Algebra*. The real case of this construction is *The Axis-Free Construction of the Quaternion Algebra*, in the Quaternions category.

## The Data

### The Four Units

**One unit to a direction, and one scalar to the coefficient field.** The algebra is written on a complex vector space with four units, exactly as the quaternion algebra is written on a real one:

$$
e_t=1,\qquad \vec e_x,\qquad \vec e_y,\qquad \vec e_z ,
$$

with the three vector units square to $-e_t$ and anticommuting in pairs, as in §*The Ten Statements*. The coefficients are complex, and the generic element is

$$
\tilde Q=Q_t e_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z=\sum_{\mu\in\{t,x,y,z\}} Q_\mu e_\mu,
\qquad Q_\mu=q_\mu+iq'_\mu ,
$$

with a real part $q_\mu$ and an imaginary part $q'_\mu$ for each of the four. A pure element is one with $Q_t=0$, and it is written $\vec Q$.

**The names are still labels.** The letters $x,y,z$ name three directions of a three-dimensional space, and no invertible element of $V$ is spent on the coefficient field. In particular $\vec e_z$ is not the imaginary unit of the scalars: the scalar imaginary is $i$, it is central, and it appears only as a coefficient.

### The Central Scalar

**The declaration.** The algebra carries one extra element, the central imaginary $i$, declared by

$$
i^2=-e_t,\qquad i\tilde Q=\tilde Q i \ \text{ for every } \tilde Q .
$$

**What the declaration says and what it does not say.** It says that the coefficient field is $\mathbb{C}=\mathbb{R}[i]$ and that the field lies in the centre. It does not say that $i$ is a vector unit: $i$ has no direction, it multiplies no direction label, and it is written on the coefficient and never on an invertible element. The table below contains no $i$, and that absence is the statement that the coefficient field is central.

**The choice of sign.** The declaration of $i$ is a two-element choice, $i$ or $-i$, and the coefficientwise conjugation of §*The Four Conjugations* exchanges the two. The choice is therefore invisible, and cheaper than the choice of an orientation: it is absorbed by an automorphism, where the orientation is absorbed only by an anti-automorphism.

### The Vector Part and Its Two Data

**The splitting.** The underlying complex space is

$$
\mathbb{B}=\mathbb{C}e_t\oplus V_{\mathbb{C}},\qquad V_{\mathbb{C}}=\mathbb{C}\otimes_{\mathbb{R}}V=\operatorname{span}_{\mathbb{C}}\{\vec e_x,\vec e_y,\vec e_z\},
$$

of complex dimension $1+3=4$ and real dimension $8$.

**The two data on the vector part.** The three units of $V_{\mathbb{C}}$ are declared orthonormal for the complex-bilinear form

$$
(\vec e_\eta,\vec e_\zeta)=\delta_{\eta\zeta},
$$

extended $\mathbb{C}$-bilinearly, and the cyclic order $x\to y\to z\to x$ is declared as the orientation, exactly as in the real case. The first datum is complex bilinear and not Hermitian: $(\lambda\vec u,\vec v)=\lambda(\vec u,\vec v)$, with no conjugate on the scalar. That is the whole difference from the real case, and it is the reason the norm of §*The Norm* is complex and can vanish.

**The cross product.** The cross product is the one the orientation defines,

$$
\vec e_x\times\vec e_y=\vec e_z,\qquad
\vec e_y\times\vec e_z=\vec e_x,\qquad
\vec e_z\times\vec e_x=\vec e_y,
$$

extended by antisymmetry and $\mathbb{C}$-bilinearity.

### What the Data Do Not Contain

**No axis.** The three vector units occur in the ten statements in the same way, and $i$ occurs in none of them.

**No base field inside the vector part.** The construction does not begin with $\mathbb{C}=\mathbb{R}[\vec e_z]$; there is a coefficient field, but it is $\mathbb{R}[i]$ and it is central. This is the difference the doubling cannot make, because its first rung must use a vector unit for the field it adjoins.

**No stack.** The four units and the scalar are declared in one act. There is no intermediate algebra, no second step that doubles the first, and no third step that extends scalars.

**No root of $-e_t$ named.** The roots of $-e_t$ in $\mathbb{B}$ form two complex quadrics together with the pair $\pm ie_t$, and the construction names no member of either.

## The Product

### The Rule

**Definition.** For $\lambda,\mu\in\mathbb{C}$ and $\vec u,\vec v\in V_{\mathbb{C}}$, the product is

$$
(\lambda e_t+\vec u)(\mu e_t+\vec v)=(\lambda\mu-(\vec u,\vec v))\,e_t+\lambda\vec v+\mu\vec u+\vec u\times\vec v ,
$$

extended by $\mathbb{C}$-bilinearity.

**The rule is the real rule with complex scalars.** The formula is that of *The Axis-Free Construction of the Quaternion Algebra*, read with $\mathbb{C}$ in place of $\mathbb{R}$ and the complex-bilinear form in place of the real one. No term is added, no term is removed and no sign changes. The central imaginary enters only through the coefficients $\lambda$ and $\mu$, and it passes through the four terms untouched because it commutes with every element.

**Bilinearity.** The right side is $\mathbb{C}$-linear in each argument separately, so the rule extends to a $\mathbb{C}$-bilinear map $\mathbb{B}\times\mathbb{B}\to\mathbb{B}$, and by that extension it is defined on the whole algebra.

### The Rule on the Invertibles

**Proposition.** On two pure elements the rule reads $\vec u\vec v=-(\vec u,\vec v)e_t+\vec u\times\vec v$, and the products of the four units are

$$
e_te_\mu=e_\mu e_t=e_\mu,\qquad
\vec e_\eta^2=-e_t,\qquad
\vec e_\eta\vec e_\zeta=-\vec e_\zeta\vec e_\eta\ \ (\eta\neq\zeta),
$$

together with the three cyclic products $\vec e_x\vec e_y=\vec e_z$, $\vec e_y\vec e_z=\vec e_x$ and $\vec e_z\vec e_x=\vec e_y$.

*Proof.* The first display is the rule with $\lambda=\mu=0$; it gives the square from $(\vec e_\eta,\vec e_\eta)=1$, the anticommutation from the antisymmetry of the cross product, and the cyclic products from the declared orientation. ∎

**The central scalar nowhere.** No entry of the list above contains $i$. The list is the ten statements of the quaternion algebra, letter for letter.

### The Ten Statements

**The equivalence.** The product rule is equivalent to ten statements on the units — the unit axiom, the three squares, the three anticommutations and the three cyclic products — read with $\mathbb{C}$-bilinear extension.

*Proof.* The rule gives the ten statements on the unit pairs. Conversely the ten statements fix all sixteen products, and a $\mathbb{C}$-bilinear map is fixed by its values on the sixteen pairs of a $\mathbb{C}$-basis. ∎

**The same asymmetry.** Seven of the ten statements are invariant under every permutation of the three vector units, and the three cyclic products are invariant under the cyclic group alone. The count and the reason are those of the quaternion algebra, and the central scalar changes neither: it is in none of the ten statements.

### The Scalar–Vector Form

**Corollary.** For two general elements,

$$
\tilde Q\tilde P=(Q_tP_t-(\vec Q,\vec P))\,e_t+Q_t\vec P+P_t\vec Q+\vec Q\times\vec P ,
$$

with all terms complex.

*Proof.* Expand the rule and collect. ∎

**The reading.** The two products of the vector part are the complex-bilinear form and the cross product, and the coefficient field enters only through the coefficients. The complexification changes the scalars and nothing else, so every structural statement about the quaternion algebra that uses only the ten statements carries over without change. That is the content of the next four sections.

## The Table

### The Sixteen Products

**The table.** The rows give the left factor and the columns the right factor.

| | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
|---|---|---|---|---|
| $e_t$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
| $\vec e_x$ | $\vec e_x$ | $-e_t$ | $\vec e_z$ | $-\vec e_y$ |
| $\vec e_y$ | $\vec e_y$ | $-\vec e_z$ | $-e_t$ | $\vec e_x$ |
| $\vec e_z$ | $\vec e_z$ | $\vec e_y$ | $-\vec e_x$ | $-e_t$ |

### The Table Is the Quaternion Table

**The statement.** Every entry is invertible with a real sign. The table is the table of *The Axis-Free Construction of the Quaternion Algebra* and of *Introduction to the Algebra of Biquaternions*, entry for entry.

**Why this is the central fact of the construction.** A complex algebra of dimension four needs a table of sixteen complex numbers. This one needs sixteen integers. The coefficient field has enlarged and the multiplication has not changed, which is possible only because the new scalar is central. A reader who wants one sentence for the whole construction has it: the biquaternion algebra is the quaternion algebra with complex coefficients.

**The check.** The sixteen entries were evaluated from the rule and compared with the table, with no mismatch; the products were also computed against the coefficientwise rule $\sum_{\mu\nu}Q_{1\mu}Q_{2\nu}e_\mu e_\nu$, with a largest residual of $2.0\times10^{-15}$ over one hundred random complex pairs.

### The Three Identities

**The scalar half.** The three squares and the triple product are one value,

$$
\vec e_x^2=\vec e_y^2=\vec e_z^2=\vec e_x\vec e_y\vec e_z=-e_t ,
$$

and the anti-cyclic triple product is $+e_t$. The identities are those of the quaternion algebra, and their proofs are the same proofs.

**The check.** The triple product in both cyclic orders was evaluated on the units, exactly, with no mismatch.

### What the Table Fixes and What It Leaves

**Fixed.** The sixteen products, hence the product of any two elements, hence associativity by §*Associativity*. The central scalar, hence the coefficient field and the complex dimension. The three squares, hence the form of the norm.

**Left open.** The cyclic order, one bit. The sign of $i$, one bit, absorbed by an automorphism. The names of the three units, which are labels.

## The Tensor Product as a Theorem

**Theorem.** The algebra built above is isomorphic, as an $\mathbb{R}$-algebra, to $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, and the isomorphism carries $i$ to $i\otimes1$.

*Proof.* Write every element as $\tilde Q=\tilde q+i\tilde p$ with $\tilde q,\tilde p\in\mathbb{H}$, the quaternion algebra of real coefficients in the same four units; the decomposition is unique because the four units are $\mathbb{C}$-linearly independent. The map

$$
\tilde q+i\tilde p\longmapsto \tilde q\otimes1+\tilde p\otimes i
$$

is $\mathbb{R}$-linear and bijective, both sides being of real dimension eight. It is multiplicative: on the left,

$$
(\tilde q_1+i\tilde p_1)(\tilde q_2+i\tilde p_2)=\tilde q_1\tilde q_2-\tilde p_1\tilde p_2+i(\tilde q_1\tilde p_2+\tilde p_1\tilde q_2),
$$

using the centrality of $i$ and $i^2=-e_t$; on the right, the tensor rule $(a\otimes b)(a'\otimes b')=aa'\otimes bb'$ with $b,b'\in\{1,i\}$ gives

$$
(\tilde q_1\otimes1+\tilde p_1\otimes i)(\tilde q_2\otimes1+\tilde p_2\otimes i)
=\tilde q_1\tilde q_2\otimes1+\tilde q_1\tilde p_2\otimes i+\tilde p_1\tilde q_2\otimes i-\tilde p_1\tilde p_2\otimes1 ,
$$

and the two agree term by term. ∎

**The check.** The two expansions were compared on one hundred random complex pairs, largest residual $2.0\times10^{-15}$.

**The reading.** The tensor product is a theorem here and a definition in *Introduction to the Algebra of Biquaternions*. Both statements are true and they are not rivals: the definition there answers the question what the algebra is made of, and the theorem here answers the question what the algebra built from the table turns out to be. The reverse reading is the useful one for this article, because a construction that begins with a tensor product has already chosen which factor is a field.

**What the theorem does not say.** It does not say that $\mathbb{H}$ is the important factor or that $\mathbb{C}$ is an added layer. The tensor product is symmetric as a set of data, and the choice of the quaternion factor as the one with the vector units is a description, not a construction step.

## Associativity

### The Left Multipliers

**The display.** Left multiplication by $\tilde Q$ is the $\mathbb{C}$-linear map $X\mapsto\tilde QX$. Read on the basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$, it is the matrix

$$
L(\tilde Q)=
\begin{pmatrix}
Q_t&-Q_x&-Q_y&-Q_z\\
Q_x&Q_t&-Q_z&Q_y\\
Q_y&Q_z&Q_t&-Q_x\\
Q_z&-Q_y&Q_x&Q_t
\end{pmatrix},
$$

the matrix $L_{\mathrm{axf}}(\tilde Q)$ of *Matrix Representations Conventions* with complex entries, and the four generators are

$$
L_x=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},\qquad
L_y=\begin{pmatrix}0&0&-1&0\\0&0&0&1\\1&0&0&0\\0&-1&0&0\end{pmatrix},\qquad
L_z=\begin{pmatrix}0&0&0&-1\\0&0&-1&0\\0&1&0&0\\1&0&0&0\end{pmatrix},
$$

with $L_t=\mathrm I_4$. The four generators are the four generators of the real case, unchanged, with real integer entries.

**The two things the display shows at once.** The coefficient field does not appear in the generators: the four matrices are integer matrices, and the complex scalars enter only through the combination $\tilde Q\mapsto L(\tilde Q)$. The display therefore carries the same information as the table and no more, and it names no direction: each generator is a signed permutation with zero diagonal and determinant $+1$.

### Associativity

**Proposition.** $L_x^2=L_y^2=L_z^2=-\mathrm I_4$ and $L_xL_y=L_z$, $L_yL_z=L_x$, $L_zL_x=L_y$.

*Proof.* Direct multiplication of the printed integer arrays. ∎

**Corollary.** $L_{e_\mu}L_{e_\nu}=L_{e_\mu e_\nu}$ for all sixteen pairs of invertibles.

*Proof.* Seven pairs involve $L_t=\mathrm I_4$; of the remaining nine, three are the squares and three are the cyclic products, and the last three are the negatives of cyclic products, as in the real case. ∎

**Theorem.** The multiplication is associative.

*Proof.* The map $\tilde Q\mapsto L(\tilde Q)$ is $\mathbb{C}$-linear and multiplicative on the basis by the corollary, hence multiplicative everywhere by $\mathbb{C}$-bilinearity of both sides; so $L(\tilde Q)L(\tilde P)=L(\tilde Q\tilde P)$, and

$$
(\tilde Q\tilde P)\tilde R=L(\tilde Q\tilde P)\tilde R=L(\tilde Q)L(\tilde P)\tilde R=L(\tilde Q)(\tilde P\tilde R)=\tilde Q(\tilde P\tilde R). 
$$

**What the proof does not use.** It does not use the tensor product, the central scalar, or any array of a matrix model. It uses the sixteen products and the four integer generators. The complexification therefore preserves associativity for a structural reason: the table is real, and the proof reads only the table.

**The check.** The sixty-four triples of basis elements were checked in integer arithmetic, with no mismatch. One hundred random complex triples gave a largest residual of $1.1\times10^{-14}$.

### The Algebra Axioms

**Theorem.** With this multiplication $\mathbb{B}$ is a four-dimensional associative unital non-commutative algebra over $\mathbb{C}$, of real dimension eight, and it is not a division algebra.

*Proof.* Associativity is the theorem above; the unit is $e_t$; non-commutativity is $\vec e_x\vec e_y=-\vec e_y\vec e_x\neq\vec e_y\vec e_x$; the dimensions are the declared basis over $\mathbb{C}$ and its realification. The failure of division is §*The Zero Divisors and the Absence of Division*. ∎

**The centre of the display.** The matrix $L(\tilde Q)$ has trace $4Q_t$ and determinant $\langle\tilde Q\rangle_{\natural}^{2}$, the square of the norm of §*The Norm*, so the display separates the scalar part from the rest by its trace and detects the zero divisors by its determinant.

**The check.** The trace identity held exactly on one hundred random complex elements, and the determinant identity to $7.7\times10^{-14}$. The rank of $L(\tilde Q)$ was $4$ on an invertible element and $2$ on the zero divisor $e_t+i\vec e_x$, which is the rank statement behind the annihilator dimension of *Zero Divisors and Invertibles in the Biquaternion Algebra*.

## The First Properties

### The Unit and the Centre

**Theorem.** The centre of $\mathbb{B}$ is the complex line $\mathbb{C}e_t$.

*Proof.* The line is central. Conversely let $\tilde Q$ commute with every element. It commutes with each vector unit, so by $[\tilde Q,\vec e_\eta]=2\vec Q\times\vec e_\eta$ and the argument of the real case, its vector part vanishes. It is therefore a complex multiple of $e_t$. ∎

**The check.** The commutation with all four units held exactly on one hundred random elements of the line.

**The reading.** The centre is a field, $\mathbb{C}$, of real dimension two; it is not the scalar line of the quaternion algebra. The difference is the whole of the difference between the two algebras at the level of structure, and the next subsection is its source.

### The Four Conjugations

**The four maps.** The algebra carries four involutions:

$$
\tilde Q^{\natural}=Q_te_t-Q_x\vec e_x-Q_y\vec e_y-Q_z\vec e_z,\qquad
\bar{\tilde Q}=\bar Q_te_t+\bar Q_x\vec e_x+\bar Q_y\vec e_y+\bar Q_z\vec e_z,
$$

$$
\tilde Q^{\ast}=\bar{\tilde Q}^{\natural}=\bar Q_te_t-\bar Q_x\vec e_x-\bar Q_y\vec e_y-\bar Q_z\vec e_z ,
$$

and the identity. The first negates the vector part and fixes the coefficients; the second conjugates the coefficients and fixes the invertibles; the third does both.

**Proposition.** The four maps form a group isomorphic to $\mathbb{Z}_2\times\mathbb{Z}_2$. The natural conjugation ${}^{\natural}$ is $\mathbb{C}$-linear and reverses the order of a product; the coefficientwise conjugation $\bar{\ }$ is $\mathbb{C}$-antilinear and preserves the order; the Hermitian conjugation ${}^{\ast}$ is $\mathbb{C}$-antilinear and reverses the order.

*Proof.* Each map is an involution and the three commute, so the group is $\mathbb{Z}_2\times\mathbb{Z}_2$ with ${}^{\natural}\bar{\ }={}^{\ast}$. The order behaviour of ${}^{\natural}$ is that of the quaternion conjugation, extended $\mathbb{C}$-linearly; the order behaviour of $\bar{\ }$ is that of a field automorphism applied to the coefficients; and ${}^{\ast}$ composes the two. ∎

**The check.** The involution, the commutation, the order behaviour of each of the three and the identity ${}^{\ast}={}^{\natural}\bar{\ }$ were checked on one hundred random complex pairs, with largest residuals between $9.9\times10^{-16}$ and $2.0\times10^{-15}$.

**What the coefficient field buys.** In the quaternion algebra only one of the four is an anti-automorphism. Here two are, and the coefficientwise conjugation is an automorphism. That is the exact sense in which the complex scalar doubles the symmetries of the algebra: the field contributes a map, and the product respects it because the coefficients are central.

### The Two Sectors

**Definition.** The two sectors are the eigenspaces of the Hermitian conjugation,

$$
\mathbb{B}_{\Psi}=\{\tilde Q:\tilde Q^{\ast}=\tilde Q\},\qquad
\mathbb{B}_{\Phi}=\{\tilde Q:\tilde Q^{\ast}=-\tilde Q\},
$$

with projections $\tilde Q_{\Psi}=\tfrac12(\tilde Q+\tilde Q^{\ast})$ and $\tilde Q_{\Phi}=\tfrac12(\tilde Q-\tilde Q^{\ast})$.

**Proposition.** Both sectors are real subspaces of real dimension four, and $\mathbb{B}=\mathbb{B}_{\Psi}\oplus\mathbb{B}_{\Phi}$ as a real space, not as a complex one.

*Proof.* The map ${}^{\ast}$ is $\mathbb{C}$-antilinear and involutive, so its eigenspaces are real subspaces and their direct sum is the whole real space. In coordinates, $\mathbb{B}_{\Psi}$ is carried by $e_t$ and $i\vec e_x$, $i\vec e_y$, $i\vec e_z$, which are four real parameters, and $\mathbb{B}_{\Phi}$ by $ie_t$ and $\vec e_x$, $\vec e_y$, $\vec e_z$. ∎

**The check.** The two projections sum to the identity and land in the two sectors, with residual $0$ on one hundred random elements.

**The reading.** The splitting is not a splitting over $\mathbb{C}$: an element of a sector multiplied by $i$ passes to the other sector. The two sectors are therefore the real halves of the algebra, and no vector unit is needed to define them, since ${}^{\ast}$ uses the coefficient conjugation and the vector part and nothing else.

### The Norm

**Definition.** The quaternionic norm is $\langle\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}$.

**Proposition.** $\langle\tilde Q\rangle_{\natural}=\tilde Q^{\natural}\tilde Q=Q_t^2+Q_x^2+Q_y^2+Q_z^2$, a complex central element, and it is multiplicative.

*Proof.* The product is computed from the scalar–vector form; the vector part vanishes and the scalar part is the sum of four squares. Multiplicativity is the computation of the real case, which uses only the order reversal of ${}^{\natural}$ and the centrality of the value. ∎

**The difference from the real case.** The value is complex, so it can vanish at a nonzero element; it is not a norm in the sense of a distance, and the corpus writes it as an algebraic norm and not as $\lvert\tilde Q\rvert$. Its vanishing set is a cone of complex dimension three, and it is the subject of *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*.

**The check.** The sum-of-squares reading held to $1.8\times10^{-15}$ on one hundred random elements, and multiplicativity to $5.9\times10^{-14}$ on one hundred random pairs.

### The Zero Divisors and the Absence of Division

**Theorem.** The element $\tilde Q$ is invertible if and only if $\langle\tilde Q\rangle_{\natural}\neq0$, and then $\tilde Q^{-1}=\tilde Q^{\natural}/\langle\tilde Q\rangle_{\natural}$. The algebra is not a division algebra.

*Proof.* If the norm does not vanish, the two products of $\tilde Q$ with $\tilde Q^{\natural}/\langle\tilde Q\rangle_{\natural}$ are the unit, since the norm is central and nonzero. If the norm vanishes, $\tilde Q$ kills a nonzero element: for every real unit vector $\vec u$,

$$
(e_t+i\vec u)(e_t-i\vec u)=e_t-(i\vec u)^{2}=e_t+\vec u^{2}=0 ,
$$

because $\vec u^2=-e_t$ and $i^2=-e_t$, so both factors are nonzero and both are zero divisors. ∎

**The family of zero divisors.** The identity above holds for every real unit $\vec u$, so the sphere of real unit vectors is a two-dimensional family of zero divisors with their annihilators. Two of them are $e_t\pm i\vec e_z$, the pair the corpus writes in its frames; the construction distinguishes neither, and the sphere is where the pair sits.

**The check.** The product $(e_t+i\vec u)(e_t-i\vec u)$ was evaluated exactly, with no mismatch, and the inverse identity held to $1.2\times10^{-15}$ on one hundred random elements of nonzero norm.

### The Idempotents

**Proposition.** For every real unit vector $\vec u$, the element $\tilde\Pi_{\mathrm{id},+}=\tfrac12(e_t+i\vec u)$ is an idempotent, Hermitian, of zero norm, and $\tilde\Pi_{\mathrm{id},-}=\tfrac12(e_t-i\vec u)$ is its orthogonal companion, with $\tilde\Pi_{\mathrm{id},+}\tilde\Pi_{\mathrm{id},-}=0$ and $\tilde\Pi_{\mathrm{id},++}\tilde\Pi_{\mathrm{id},-}=e_t$.

*Proof.* Expanding, $\tilde\Pi_{\mathrm{id},+}^2=\tfrac14(e_t+2i\vec u+(i\vec u)^2)=\tfrac14(e_t+2i\vec u+e_t)=\tfrac12(e_t+i\vec u)$, using the centrality of $i$, $(i\vec u)^2=i^2\vec u^2=+e_t$. The Hermitian property is the reality of $\vec u$, and the vanishing of the norm is $\tfrac14(1-(\vec u,\vec u))=0$, the vector being a real unit. The companion statements follow by the change of sign of $i$ and by the identity of the zero divisors above. ∎

**The check.** The idempotent, Hermitian and null properties held on one hundred random real unit vectors, largest residual $1.1\times10^{-16}$.

**The sphere of idempotents.** The idempotents of this form are indexed by the unit sphere of the real vector part, and the rotations of that sphere are automorphisms of the algebra, so no one of them is distinguished. The corpus writes one pair, $\tfrac12(e_t\pm i\vec e_z)$, because a frame is needed for the physics; the algebra supplies a sphere. The full classification of the idempotents, which is wider than this family, is *The Square of an Element in the Biquaternion Algebra*.

### The Classes of Element

**The roots of $-e_t$.** An element satisfies $\tilde\zeta^2=-e_t$ exactly when either $\tilde\zeta=\pm ie_t$, or $\tilde\zeta$ is pure with $B^2=(\vec\zeta,\vec\zeta)=1$; the second alternative is a complex quadric of complex dimension two.

*Proof.* The square is $(Q_t^2-B^2)e_t+2Q_t\vec\zeta$. The vanishing of the vector part leaves $Q_t=0$ or $\vec\zeta=0$; the first gives $-B^2=-1$, the second $Q_t^2=-1$. ∎

**The roots of $+e_t$.** The same computation with the other sign gives either $\tilde\zeta=\pm e_t$ or $\tilde\zeta$ pure with $B^2=-1$.

**The one imaginary that is central.** The pair $\pm ie_t$ is the pair of central roots, and it is the sign choice of §*The Central Scalar*. The quadric $B^2=1$ is the family of vector roots, and it contains the real unit sphere of the quaternion algebra: the real roots of $-e_t$ are the real points of the complex quadric, and the complex algebra adds the rest.

**The classes, in one table.**

| class | equation | the set |
|---|---|---|
| units | $\langle\tilde Q\rangle_{\natural}\neq0$ | the complement of the null cone |
| zero divisors | $\langle\tilde Q\rangle_{\natural}=0$ | the null cone, of real dimension six |
| idempotents | $\tilde Q^2=\tilde Q$ | a sphere of Hermitian idempotents, and more |
| roots of $-e_t$ | $\tilde Q^2=-e_t$ | $\{\pm ie_t\}$ and the quadric $B^2=1$ |
| roots of $+e_t$ | $\tilde Q^2=+e_t$ | $\{\pm e_t\}$ and the quadric $B^2=-1$ |

**The check.** One hundred random points of the quadric $B^2=1$ squared to $-e_t$ to $4.4\times10^{-16}$, and the two central roots were checked exactly.

### The Commutator

**Proposition.** For two elements with pure parts, $[\vec Q_1,\vec Q_2]=2\,\vec Q_1\times\vec Q_2$, and for two general elements $[\tilde Q_1,\tilde Q_2]=2\,\vec Q_1\times\vec Q_2$.

*Proof.* The commutator cancels the symmetric terms of the scalar–vector form. ∎

**The check.** The identity held exactly on one hundred random complex pairs.

**The reading.** The bracket is the complex-bilinear cross product, so the vector part with the bracket is the complex Lie algebra $\mathfrak{so}(3,\mathbb{C})$, of complex dimension three. The central scalar does not enter the bracket, and it does not enlarge it: the bracket of the algebra is the bracket of the quaternion algebra read over $\mathbb{C}$.

## What Is Free and What Is Fixed

### The One Bit of the Table

**The invariance.** Seven of the ten statements are invariant under every permutation of the three vector units, and the three cyclic products are the orientation. The argument is that of the real case, and it is unchanged: the central scalar is in none of the ten statements, so it can neither enlarge nor reduce the symmetry.

**The residue.** One bit, and it is absorbed by the natural conjugation, which reverses the order and is an isomorphism onto the opposite algebra.

### The One Bit of the Scalar

**The sign of $i$.** The declaration of $i$ is the choice between $i$ and $-i$, and the coefficientwise conjugation exchanges the two. It is an automorphism of the algebra, so the choice is absorbed without even reversing the product. This bit is strictly cheaper than the orientation bit, and it is the reason the complex scalar adds no freedom to the construction.

**The comparison with the doubling.** The stack needs a root of $-e_t$ in a vector direction and then the scalar $i$ as a further layer. Here the scalar sits in the centre from the first line and the vector units are untouched, so there is no direction in the choice at all.

### The Automorphisms

**Proposition.** A rotation of the real vector part, extended $\mathbb{C}$-linearly and by the identity on $e_t$ and on $i$, is an automorphism. A reflection of the real vector part, extended in the same way, satisfies $T(\tilde Q\tilde P)=T(\tilde P)T(\tilde Q)$ and is not an automorphism.

*Proof.* The rule of §*The Product* is preserved by a map that preserves the complex-bilinear form, the cross product and the central scalar. A rotation preserves the cross product, since $Ru\times Rv=(\det R)R(u\times v)$ and $\det R=1$; a reflection reverses it, and the reversal is the sign that turns the identity into the anti-automorphism, as in the real case. ∎

**The check.** A rotation gave an automorphism with a largest residual of $4.8\times10^{-15}$ over one hundred random complex pairs, and a transposition of two units gave an anti-automorphism with a largest residual of $1.8\times10^{-15}$; the same transposition read as an automorphism failed with a residual of $16.3$.

**Where the rest of the group is.** The $\mathbb{C}$-linear automorphisms of $\mathbb{B}$ are more numerous than the rotations of the vector part. The algebra is central simple over $\mathbb{C}$, so every $\mathbb{C}$-linear automorphism is inner, of the form $\tilde Q\mapsto\tilde U\tilde Q\tilde U^{-1}$ for an invertible element $\tilde U$, by the Skolem–Noether theorem; the group, its real forms and the derivation algebra are *Biquaternion Automorphisms and Derivations*. This article uses only the subfamily of rotations, because that is the subfamily its own symmetries produce, and the real case is *Quaternion Automorphisms and Derivations*.

### No Axis, and No Vector Root Distinguished

**The account.** The data are four units, one central scalar, one complex-bilinear form and one orientation. The three vector units occur in the ten statements in the same way, the central scalar occurs in none of them, the roots of $-e_t$ form two quadrics and a central pair with no member singled out, the idempotents form a sphere, and the two bits that remain are absorbed, one by an anti-automorphism and one by an automorphism.

## The Contrast with the Stack

### The Three Layers

**The stack in one paragraph.** The doubling of *The Cayley–Dickson Construction of the Biquaternion Algebra* runs the doubling twice and then extends the scalars: $\mathbb{R}$ to $\mathbb{C}$ by adjoining $\vec e_z$, $\mathbb{C}$ to $\mathbb{H}$ by adjoining $\vec e_x$ with the twist, and $\mathbb{H}$ to $\mathbb{B}$ by adjoining $i$ as a central scalar. Two of the three steps spend a vector unit, and the third adds the field.

**What the stack proves and this article assumes.** The stack proves that each rung is forced: that the twist is the only rule without zero divisors, that the third unit is computed, and that the fourth layer is a scalar extension and not a fourth rung of the ladder. Those are results, and this article takes them as given. Its table is the stack's table, and a reader who wants the reasons for the signs must read the stack.

**The asymmetry.** In the stack, the first rung names $\vec e_z$ inside a conjugation and the second names $\vec e_x$ outside it, and the third names $i$. Three different roles for one product. Here the ten statements name no unit differently from another, and the field is declared in the centre.

### The Two Choices, Compared

| | the stack | the axis-free construction |
|---|---|---|
| declared first | $\mathbb{C}=\mathbb{R}[\vec e_z]$ | the four units and the central $i$ |
| the role of $\vec e_z$ | the imaginary unit of the base | one of three units |
| the role of $\vec e_x$ | the doubling unit | one of three units |
| the role of $\vec e_y$ | computed, $\vec e_z\vec e_x$ | one of three units |
| the role of $i$ | a third layer, added last | a central scalar, declared first |
| what is derived | the squares, the anticommutations, the cycle, the tensor product | the table, then the tensor product |
| what is chosen | a root of $-e_t$, a transverse unit, a sign | an orientation and a sign of $i$ |
| the size of the choice | a point of a sphere, a direction, a sign | two bits, both absorbed |
| what is proved | the twist is forced, the layers are the only ones | associativity, the algebra axioms, the first properties |

**The reading of the table.** The two routes answer different questions. The stack answers why the algebra has this table and why the ladder stops where it does. The axis-free construction answers what the table is, with data that match the symmetry of the object, and it is the route to take when the table is the starting point.

### What the Stack Is For

**The exclusion of the plain rule.** The stack is the only route that exhibits the alternative: under the plain rule the element $\vec e_z\vec e_x$ squares to $+e_t$ and the algebra acquires two idempotents and zero divisors. The axis-free construction never has the plain rule in view, so it cannot make that argument, and the doubling article's is the one to read.

**The scalar extension as a rung.** The stack also shows why the fourth layer is not a fourth rung: the Cayley–Dickson step at that rung would produce the octonions or a split algebra, and the scalar extension produces neither. That identification is the content of *The Cayley–Dickson Construction of the Biquaternion Algebra*, §*The Three Layers*, and it has no counterpart here.

**The division property.** Both routes prove that the quaternion algebra divides and that the biquaternion algebra does not. The axis-free route proves it in one line from the norm, because the norm is a sum of four squares of coefficients; the stack proves it from the norm of a doubled element. The two proofs are the same proof read at different depths.

## Summary

The biquaternion algebra is fixed by four units, one central imaginary, and the ten statements of the quaternion algebra read with complex coefficients. The product rule is

$$
(\lambda e_t+\vec u)(\mu e_t+\vec v)=(\lambda\mu-(\vec u,\vec v))\,e_t+\lambda\vec v+\mu\vec u+\vec u\times\vec v ,
$$

with $\lambda,\mu$ complex and the form complex bilinear. Complex bilinearity is the whole of the difference from the quaternion algebra: no term is added, no sign changes, and the table has the same sixteen integer entries. The central scalar appears in no entry, and that absence is what makes the table real and the algebra complex.

Associativity is proved inside the coefficient display, whose four generators are integer signed permutations with zero diagonal and determinant one; the complex scalars enter only through the combination. The tensor product with $\mathbb{C}$ is a theorem of this route and a definition of the base article, and the two readings agree term by term.

The first properties follow in a few lines each: the centre is the complex line; four involutions form a Klein group, with two $\mathbb{C}$-linear maps and two antilinear ones, two of them reversing the order; the two sectors are real four-dimensional halves given by the Hermitian conjugation; the norm is a complex central quadratic form, multiplicative and vanishing on a cone, so the algebra is not a division algebra and its units are the complement of the cone; the zero divisors include the whole sphere $(e_t+i\vec u)(e_t-i\vec u)=0$ over the real unit vectors; the Hermitian idempotents are the same sphere, $\tfrac12(e_t+i\vec u)$; the roots of $\pm e_t$ are a central pair and a complex quadric each; and the commutator of two elements is twice the complex cross product of their vector parts.

Two bits are left over and both are absorbed: the orientation of the three vector units by the natural conjugation, and the sign of $i$ by the coefficientwise conjugation. No direction is named, no vector unit is spent on a field, and no layer is stacked.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}e_t\oplus V_{\mathbb{C}}$ | the biquaternion algebra, a complex scalar line plus a three-dimensional complex vector part |
| $e_t=1$ | the scalar unit, the two-sided identity |
| $\vec e_x,\vec e_y,\vec e_z$ | the three vector units, orthonormal and positively oriented |
| $i$ | the central imaginary, $i^2=-e_t$, the coefficient field $\mathbb{C}=\mathbb{R}[i]$ |
| $\tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ | the generic biquaternion, coefficients complex |
| $\vec Q$ | the vector part, a pure element |
| $(\vec Q_1,\vec Q_2)$ | the complex-bilinear form of the vector part |
| $B^2=(\vec Q,\vec Q)$ | the quadratic value of a vector part |
| $\vec Q_1\times\vec Q_2$ | the complex cross product the orientation fixes |
| $^{\natural}$ | the natural conjugation, $\mathbb{C}$-linear, order reversing |
| $\bar{\ }$ | the coefficientwise conjugation, antilinear, order preserving |
| ${}^{\ast}={}^{\natural}\bar{\ }$ | the Hermitian conjugation, antilinear, order reversing |
| $\mathbb{B}_{\Psi},\mathbb{B}_{\Phi}$ | the two sectors, the eigenspaces of ${}^{\ast}$ |
| $\langle\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}=\sum_\mu Q_\mu^2$ | the quaternionic norm, complex and central |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}$ | the complex-bilinear form $\mathrm{Sc}(\tilde Q_1\tilde Q_2^{\natural})$ |
| $L(\tilde Q)$, $L_x,L_y,L_z$ | left multiplication and its four generators, the axis-free display |
| $\tilde\Pi_{\mathrm{id},\pm}=\tfrac12(e_t\pm i\vec u)$ | the Hermitian idempotents over the real unit vectors |

## Further Reading

- [The Biquaternion Algebra](introduction-to-the-algebra-of-biquaternions.html), for the algebra as a tensor product, its table, its axioms, its centre and the absence of division.
- [The Cayley–Dickson Construction of the Biquaternion Algebra](the-cayley-dickson-construction-of-the-biquaternion-algebra.html), for the stack of three layers and the proof that the third is a scalar extension.
- [The Axis-Free Construction of the Quaternion Algebra](the-axis-free-construction-of-the-quaternion-algebra.html), for the real case, the ten statements and the associativity proof this article repeats.
- [The Element, the Coordinates and the Conjugations](the-element-the-coordinates-and-the-conjugations-in-the-biquaternion-algebra.html), for the four conjugations, their group and the three coordinate systems.
- [Zero Divisors and Invertibles](zero-divisors-and-invertibles-in-the-biquaternion-algebra.html), for the annihilators, their dimension two, and the unit criterion.
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the norm as a form, its conjugates and its vanishing set.
- [The Square of an Element](the-square-of-an-element-in-the-biquaternion-algebra.html), for the roots of a general element and the full classification of the idempotents.
- [Matrix Representations Conventions](matrix-representations-conventions.html), for the axis-free array and the reason the coefficient basis is the one that names no direction.
- [Biquaternion Automorphisms and Derivations](biquaternion-automorphisms-and-derivations.html), for the full automorphism group, its two connected components, the derivation algebra and the role of Skolem–Noether.
- [Quaternion Automorphisms and Derivations](quaternion-automorphisms-and-derivations.html), for the real case of the same three objects.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the doubling ladder and the complexification of a composition algebra.
